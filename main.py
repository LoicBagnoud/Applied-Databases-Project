# The following is a Python Application where a user is able to interact with a menu and interact
# with a MySQL and Neo4j database
# Author: Loic Bagnoud

import mysql



def show_menu():
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


def speaker_search():
    speaker_name = input("Enter speaker name: ")




while True:
    show_menu()
    user_choice = input("Choice: ")

    if user_choice == "1":
        speaker_search()


    elif user_choice == "x":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please select one of the options")






def main():
    print("Yes")






if __name__ == "__main__":
    main()
