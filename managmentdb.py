# This is the code to interact with the MySQL database
# Author: Loic Bagnoud

import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", 
                           user="root", 
                           password="root", 
                           db="appdbproj", 
                           cursorclass=pymysql.cursors.DictCursor)
    

def search_database(name):
    global conn 

# We make the connection
    if conn is None:
        connect()

# The SQL query for selection
    query = '''
            SELECT s.speakerName, s.sessionTitle, r.roomName 
            FROM session s 
            JOIN room r ON s.roomID = r.roomID 
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
            print(s["speakerName"], s["sessionTitle"], s["roomName"], sep="  |  ")
    cursor.close ()    



    # References:
    # For the "|" separator: https://www.geeksforgeeks.org/python/python-sep-parameter-print/