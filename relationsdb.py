# This is the code to interact with the Neo4j Database
# Author: Loic Bagnoud

# First we import the neo4j module
from neo4j import GraphDatabase

# Then we follow the documentation as to make the proper connection
driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"), max_connection_lifetime=1000)


# Next, we write our specific functions and queries. 
# The first one checks if a specific attendee ID exists in the neo4j database
def attendee_exists_tx(tx, attendee_id):
    query = """
            MATCH (a:Attendee {AttendeeID: $attendee_id})
            RETURN a.AttendeeID AS attendee_id
            """

    result = tx.run(query, attendee_id=int(attendee_id))
    record = result.single()

    return record is not None

# This one will check if there's any connections for that specific attendee ID
def get_id_relations_tx(tx, attendee_id):
    query = '''
            MATCH (a:Attendee {AttendeeID: $attendee_id})-[:CONNECTED_TO]-(s:Attendee) 
            RETURN s.AttendeeID AS connected_id
            '''

    ids = []
    results = tx.run(query, attendee_id=int(attendee_id))

    for result in results:
        ids.append(result["connected_id"])
        
    return ids

def create_connection_tx(tx, attendee_id_1, attendee_id_2):
    query = """
            MATCH (a:Attendee {AttendeeID: $attendee_id_1})
            MATCH (b:Attendee {AttendeeID: $attendee_id_2})
            MERGE (a)-[:CONNECTED_TO]->(b)
            RETURN a.AttendeeID AS attendee_id_1, b.AttendeeID AS attendee_id_2
            """

    result = tx.run(query, attendee_id_1=int(attendee_id_1), attendee_id_2=int(attendee_id_2))

    return result.single() is not None


# Afterwards, we execute those queries after we called them above. 
# I separated them between executions here and the cypher calls above.
def attendee_exists(attendee_id):
    global driver

    if driver is None:
        connect()

    with driver.session() as session:
        return session.execute_read(attendee_exists_tx, attendee_id)


def get_id_relations(attendee_id):
    global driver

    if driver is None:
        connect()

    with driver.session() as session:
        return session.execute_read(get_id_relations_tx, attendee_id)
    

def create_connection(attendee_id_1, attendee_id_2):
    global driver

    if driver is None:
        connect()

    with driver.session() as session:
        return session.execute_write(create_connection_tx, attendee_id_1, attendee_id_2)

# References:
# Neo4j documentation - https://neo4j.com/docs/api/python-driver/current/api.html