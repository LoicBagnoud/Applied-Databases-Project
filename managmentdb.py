# This is the code to interact with the MySQL database
# Author: Loic Bagnoud

import pymysql

conn = None

# This is our connector
def connect():
    global conn
    conn = pymysql.connect(host="localhost", 
                           user="root", 
                           password="root", 
                           db="appdbproj", 
                           cursorclass=pymysql.cursors.DictCursor)

# This functions allows us to basically see if a company exists or not
def display_company_name(company_id):
    global conn

    if conn is None:
        connect()

    query = """
        SELECT companyName
        FROM company
        WHERE companyID = %s
    """

    cursor = conn.cursor()
    cursor.execute(query, (company_id,))
    result = cursor.fetchone()
    cursor.close()

    # This allows us to get nothing in case the user puts a company ID that doesn't exist
    if result is None:
        return None

    return result["companyName"]

    
# The function below searches the database based on name entered
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

# This function searches the database based on the ID the user has entered
def company_search(company_id):
    global conn 

# We make the connection
    if conn is None:
        connect()

    query = """
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
            """
        
    cursor = conn.cursor()
    cursor.execute(query, (company_id,))
    results = cursor.fetchall()

    if len(results) == 0:
            print(f"No attendees found for {display_company_name(company_id)}.\n")
    else:
        print("Attendee Name | DOB | Name of Session | Speaker Name | Session Date | Room Name\n")
        for s in results:     
            print(s["attendeeName"], s["attendeeDOB"], s["sessionTitle"], s["speakerName"], s["sessionDate"], s["roomName"], sep="  |  ") 
    cursor.close ()


def insert_attendee():
    if conn is None:
        connect()

    query = '''
            INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
            VALUES (%s, %s, %s, %s, %s,)
            '''



    # References:
    # For the "|" separator: https://www.geeksforgeeks.org/python/python-sep-parameter-print/