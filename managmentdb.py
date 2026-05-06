# This is the code to interact with the MySQL database
# Author: Loic Bagnoud

# We start by importing out pymysql package
import pymysql

conn = None

# This is our connector and here we're just following the documentation
def connect():
    global conn
    conn = pymysql.connect(host="localhost", 
                           user="root", 
                           password="root", 
                           db="appdbproj", 
                           cursorclass=pymysql.cursors.DictCursor)

# This function allows us to check for a specific attendee and get their name. This will be useful for Option 4
def search_attendeeid_get_name(attendeeID):
    global conn

    if conn is None:
        connect()

    query = '''
            SELECT attendeeName
            FROM attendee
            WHERE attendeeID = %s
            '''

    cursor = conn.cursor()
    cursor.execute(query, (attendeeID,))
    result = cursor.fetchone()
    cursor.close()

    if result is None:
        return None

    return result["attendeeName"]


# This functions allows us to basically see if a company exists or not. Useful for error
# checking in option 2
def display_company_name(company_id):
    global conn

    if conn is None:
        connect()

    query = '''
            SELECT companyName
            FROM company
            WHERE companyID = %s
            '''

    cursor = conn.cursor()
    cursor.execute(query, (company_id,))
    result = cursor.fetchone()
    cursor.close()

    # This allows us to get nothing in case the user puts a company ID that doesn't exist
    if result is None:
        return None

    return result["companyName"]

    
# The function below searches the database based on name entered. Useful for option 1, which checks on name
# and we need it to catch non-existing names.
def search_database(name):
    global conn 

# We make the connection
    if conn is None:
        connect()

# The SQL query for selection
    query = '''
            SELECT s.speakerName, s.sessionTitle, r.roomName 
            FROM session s 
            INNER JOIN room r ON s.roomID = r.roomID 
            WHERE s.speakerName LIKE (%s)
            '''


# We excute what's been stored and used in the function above and then close it
    
    search_value = "%" + name + "%"
    
    cursor = conn.cursor()
    cursor.execute(query, (search_value,))
    results = cursor.fetchall()

    if len(results) == 0:
            print("No speakers found of that name.\n")
    else:
        print("Speaker Name | Session Title | Room Name\n")
        for s in results:     

            # I wasn't sure how to separate properly, until I found the "sep" function
            print(s["speakerName"], s["sessionTitle"], s["roomName"], sep="  |  ")

    cursor.close()

# This function searches the database based on the ID the user has entered. It's the main
# core of Option 2.
def company_search(company_id):
    global conn 


    if conn is None:
        connect()

    query = '''
            SELECT 
                a.attendeeName, 
                a.attendeeDOB, 
                s.sessionTitle, 
                s.speakerName, 
                s.sessionDate,
                r.roomName
            FROM attendee a
            INNER JOIN registration reg
                ON a.attendeeID = reg.attendeeID
            INNER JOIN session s
                ON reg.sessionID = s.sessionID
            INNER JOIN room r
                ON s.roomID = r.roomID
            WHERE a.attendeeCompanyID = %s
            ORDER BY a.attendeeName
            '''
        
    cursor = conn.cursor()
    cursor.execute(query, (company_id,))
    results = cursor.fetchall()

    if len(results) == 0:
            print(f"No attendees found for {display_company_name(company_id)}.\n")
    else:
        print("Attendee Name | DOB | Name of Session | Speaker Name | Session Date | Room Name\n")
        for s in results:     
            print(s["attendeeName"], s["attendeeDOB"], s["sessionTitle"], s["speakerName"], s["sessionDate"], s["roomName"], sep="  |  ") 
    cursor.close()


# This is for Option 3. We have all the details we need to insert into the database
def insert_attendee(attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID):
    global conn 

    if conn is None:
        connect()


    query = '''
            INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
            VALUES (%s, %s, %s, %s, %s)
            '''

    cursor = conn.cursor()
    cursor.execute(query, (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID))
    conn.commit()
    cursor.close()

    print ("Attendee successfully added")
    print ("---------------------------")


# This is for Option 6. It's the MySQL to get the Rooms based on the room ID.
def view_rooms():
    global conn 

    if conn is None:
        connect()

    query = '''
            SELECT roomID, roomName, capacity
            FROM room
            ORDER BY roomID
            '''

    cursor = conn.cursor()
    cursor.execute(query)

    # Was constantly getting an error here that I didn't understand, until I discovered that "fetchone" 
    # goes through one record. "Fetchall" is the correct one here since it gets me all the rows.
    result = cursor.fetchall()

    
    print("RoomID | RoomName | Capacity\n")

    for r in result:     
        print(r["roomID"], r["roomName"], r["capacity"], sep="  |  ") 

    cursor.close()




    # References:
    # For the "|" separator: https://www.geeksforgeeks.org/python/python-sep-parameter-print/
    # For the differences between fetchone vs fetchall - https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/