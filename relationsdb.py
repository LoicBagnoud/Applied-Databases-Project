# This is the code to interact with the Neo4j Database
# Author: Loic Bagnoud

from neo4j import GraphDatabase

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"), max_connection_lifetime=1000)


# This helps us check if a specific attendee ID exists or not
def attendee_exists_tx(tx, attendee_id):
    query = """
            MATCH (a:Attendee {AttendeeID: $attendee_id})
            RETURN a.AttendeeID AS attendee_id
            """

    result = tx.run(query, attendee_id=int(attendee_id))
    record = result.single()

    return record is not None

# This one checks the relations
def get_id_relations(tx, attendee_id):
    query = '''
            MATCH (a:Attendee {AttendeeID: $attendee_id})-[:CONNECTED_TO]-(s:Attendee) 
            RETURN s.AttendeeID AS connected_id
            '''

    ids = []
    results = tx.run(query, attendee_id=int(attendee_id))

    for result in results:
        ids.append(result["connected_id"])
    return ids


def main():
    connect()

    with driver.session() as session:
        values = session.execute_read(get_id_relations)
        

if __name__ == "__main__":
    main()


# References:
# Neo4j documentation - https://neo4j.com/docs/api/python-driver/current/api.html
# MUST NOT FORGET TO CHANGE PASSWORDS FOR THE VIRTUAL MACHINE