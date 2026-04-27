# The following is a Python Application where a user is able to interact with a menu and interact
# with a MySQL and Neo4j database
# Author: Loic Bagnoud

# First, we import the modules we need, including our managmentdb module that interacts with the Database

import managmentdb


# This functions displayed the menu that allows the user to make his choice of operations
def show_menu():
    print()
    print("Conference Management")
    print("---------------------\n")
    print("Menu")
    print("====")
    print("1 - View Speakers & Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Atendee")
    print("4 - View Connected Atendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit Application")


# Must explain this as I've found in Stack Overflow
def speaker_search():
    while True:
        speaker_name = input("Enter speaker name: ").strip()

        if speaker_name == "":
            print("Please enter a speaker name.")
        elif any(char.isdigit() for char in speaker_name):
            print("Invalid input. Speaker name cannot contain numbers.")
        else:
            return speaker_name

def company_search():
    companyID = input(int("Enter Company ID: "))







def main():

    while True:
        show_menu()
        user_choice = input("Choice: ")

        if user_choice == "1":
            name_search = speaker_search()
            print(f"Session Details for: {name_search}")
            print("--------------------------------------------")
            managmentdb.search_database(name_search)


        elif user_choice == "2":
            company_id = company_search()
            print("Good try!")    


        elif user_choice == "x":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please select one of the options")



if __name__ == "__main__":
    main()

# References: 
# For the block on non string names: # Source - https://stackoverflow.com/a/39613634
# Posted by Dimitris Fasarakis Hilliard, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-27, License - CC BY-SA 3.0
