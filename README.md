# Applied-Databases-Project

This project is a Python command-line application for managing conference information.  
It interacts with two databases:

- **MySQL**: stores conference data such as attendees, companies, rooms, sessions, and registrations.
- **Neo4j**: stores relationships between attendees using `CONNECTED_TO` relationships.

The program allows the user to view speakers and sessions, search attendees by company, add new attendees, view connected attendees, create new attendee connections, and view rooms.

No extra functionality was provided

## Features

The application menu provides the following options:

1. **View Speakers & Sessions**  
   Search for speakers and display their session details.

2. **View Attendees by Company**  
   Display attendees linked to a specific company.

3. **Add New Attendee**  
   Add a new attendee to the MySQL database.

4. **View Connected Attendees**  
   Enter an attendee ID and display all attendees connected to that attendee in Neo4j.

5. **Add Attendee Connection**  
   Create a `CONNECTED_TO` relationship between two existing attendees in Neo4j.

6. **View Rooms**  
   Display all rooms and their capacities.

---

## Project Files

The main files used in this project are:

```text
main.py
managmentdb.py
relationsdb.py
requirements.txt
```

## Some Important Notes

This project will be submitted as a zipped file containing the main Python files used by the program:

- `main.py` - the main menu file
- `managmentdb.py` - the MySQL interaction file
- `relationsdb.py` - the Neo4j interaction file

The packages needed to run this program should already be installed in your machine, but if not, a requirements.txt file is provided to be ran in order to get those installed.
More specifically, the Neo4j one which is not native to Python. 

To install the required packages, run:

```bash
pip install -r requirements.txt
```

I added the SQL database file as well as the neo4j Json command file. If these do not exist, please ensure that they have been properly imported into both MySQL and neo4j. 

The program also makes connections with those databases, this means that a couple of setups need to be ensured:

- MySQL needs to have the appdbproj.sql imported as one of it's databases
- Neo4j needs to have had the connection list imported as well AND needs to be running when executing the program, otherwise option 4 and 5 will fail to fetch anything.
- I tried to keep the same passwords that exist in the VM. As such, please ensure that those are not changed to be able to run this. 

Additional documentation is provided to correctly import the databases if need be:

- [MySQL Workbench SQL Data Import Wizard](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-management.html)
- [MySQL command-line import using SQL dump files](https://dev.mysql.com/doc/refman/9.4/en/import-table.html)
- [Neo4j Cypher Shell](https://neo4j.com/docs/operations-manual/current/cypher-shell/)

## References:

The following references exist within the files themselves to show where they were used.

1. For the block on non string names - # Source - https://stackoverflow.com/a/39613634
Posted by Dimitris Fasarakis Hilliard, modified by community. See post 'Timeline' for change history
Retrieved 2026-04-27, License - CC BY-SA 3.0

2. To check if something is a digit - https://www.w3schools.com/python/ref_string_isdigit.asp

3. For the Datetime format idea - # Source - https://stackoverflow.com/a/16870699
Posted by jamylak, modified by community. See post 'Timeline' for change history
Retrieved 2026-05-02, License - CC BY-SA 4.0

4. For the "|" separator: https://www.geeksforgeeks.org/python/python-sep-parameter-print/

5. For the differences between fetchone vs fetchall - https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/

6. For the LEFT JOIN SQL proposal - ChatGPT - https://chatgpt.com/share/69fcd369-74e4-8394-8556-45b5f8a09ca5

7. Neo4j documentation - https://neo4j.com/docs/api/python-driver/current/api.html

8. ChatGPT check connection proposal - https://chatgpt.com/share/69fcce3d-a9b0-8393-9e63-2698d5a8aaf4