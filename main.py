# The following is a Python Application where a user is able to interact with a menu and interact
# with a MySQL and Neo4j database
# Author: Loic Bagnoud

# First, we import the modules we need, including our managmentdb module that interacts with the Database

import managmentdb
import datetime
import pymysql

# Next, we start off with our main function which will show the menu and trigger the user's choice commands.
# For readibility, I put the functions below the main function as it was easier to read for me.
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
            company_name = managmentdb.display_company_name(company_id)

            if company_name == None:
                print(f"Company with ID {company_id} doesn't exist")

            else:
                print(f"{company_name} Attendees") 
                print("--------------------")
                managmentdb.company_search(company_id)

        elif user_choice == "3":
            print("Add new attendee")   
            print("----------------")   

            try:  
                attendee_id, attendee_name, attendee_dob, attendee_gender, attendee_company_id = add_attendee_details()
                managmentdb.insert_attendee(attendee_id, attendee_name, attendee_dob, attendee_gender, attendee_company_id)
            except pymysql.err.IntegrityError as e:
                print (f"***ERROR*** Attendee ID {attendee_id} already exists")
            except Exception as e:
                print("***ERROR*** An unkown error has occurred")


        # CURRENTLY WORKING ON THIS (DONT FORGET)
        elif user_choice == "4":
            chosen_attendee_id = input("Enter Attendee ID: ")












        elif user_choice == "5":
            print("Work in progress")

















        elif user_choice == "6":
            print("Rooms")
            print("-----")
            managmentdb.view_rooms()

        elif user_choice == "x":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please select one of the options")


# This helps validate that the user is using the proper datetime format
def validate_date(date_text):
        try:
            datetime.date.fromisoformat(date_text)
            return True
        except ValueError:
            return False

# This functions displays the menu that allows the user to make his choice of operations
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


# This function, has it was taken from Stack Overflow, basically makes it so the user doesn't use numbers for names. A name has letters 
# and this will prevent the user from making mistakes. 
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
    while True:
        companyID = input("Enter Company ID: ").strip()

        if companyID == "":
            print("Please enter a valid Company ID")

            # This checks if the ID entered is a digit through the isdigit function.
        elif not companyID.isdigit():
            print("Invalid input. Company ID must be a whole number.")
        else:
            return companyID

# Had to divide the error checks between here and above... Not sure how to put everything in one place for better organisation
def add_attendee_details():
    valid_genders = ["Male", "Female"]

    while True:
        attendee_id = input("Enter attendee ID: ").strip()

        if attendee_id == "":
            print("***ERROR*** Please enter a valid Attendee ID")
        elif not attendee_id.isdigit():
            print("***ERROR*** Invalid input. Attendee ID must be a whole number.")
        else:
            break

    while True:
        attendee_name = input("Enter attendee name: ").strip()

        if attendee_name == "":
            print("***ERROR*** Please enter a valid attendee name")
        elif any(char.isdigit() for char in attendee_name):
            print("***ERROR*** Invalid input. Attendee name cannot contain numbers.")
        else:
            break

    while True:
        attendee_dob = input("Enter attendee Date of Birth YYYY-MM-DD: ").strip()

        if attendee_dob == "":
            print("***ERROR*** Please enter a valid Date of Birth")
        elif not validate_date(attendee_dob):
            print("***ERROR*** Incorrect data format, date should be YYYY-MM-DD")
        else:
            break

    while True:
        attendee_gender = input("Enter attendee gender: ").strip()

        if attendee_gender == "":
            print("***ERROR*** Please enter a valid gender")
        elif attendee_gender not in valid_genders:
            print("***ERROR*** Invalid gender. Please enter Male or Female.")
        else:
            break

    while True:
        attendee_company_id = input("Enter attendee company ID: ").strip()

        if attendee_company_id == "":
            print("***ERROR*** Please enter a valid Company ID")
        elif not attendee_company_id.isdigit():
            print("***ERROR*** Invalid input. Company ID must be a whole number.")
        elif managmentdb.display_company_name(attendee_company_id) is None:
            print(f"***ERROR*** Company with ID {attendee_company_id} doesn't exist")
        else:
            break

    return attendee_id, attendee_name, attendee_dob, attendee_gender, attendee_company_id









if __name__ == "__main__":
    main()

# References: 
# For the block on non string names - # Source - https://stackoverflow.com/a/39613634
# Posted by Dimitris Fasarakis Hilliard, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-27, License - CC BY-SA 3.0

# To check if something is a digit - https://www.w3schools.com/python/ref_string_isdigit.asp

# For the Datetime format idea - # Source - https://stackoverflow.com/a/16870699
# Posted by jamylak, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-02, License - CC BY-SA 4.0
