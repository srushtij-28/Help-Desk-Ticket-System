import os

from config import DATA_DIR, TICKET_FILE, USER_FILE
from storage import save_data

from user_manager import (
    add_user,
    view_users,
    search_user,
    delete_user
)

from ticket_manager import (
    create_ticket,
    view_tickets,
    view_ticket_details,
    search_tickets,
    update_status,
    assign_ticket,
    add_comment,
    delete_ticket,
    ticket_statistics
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(TICKET_FILE):
        save_data(TICKET_FILE, [])

    if not os.path.exists(USER_FILE):
        save_data(USER_FILE, [])


def show_menu():
    print("\n")
    print("=" * 60)
    print("             HELP DESK TICKET SYSTEM")
    print("=" * 60)

    print("\nUSER MANAGEMENT")
    print("1. Add User")
    print("2. View Users")
    print("3. Search User")
    print("4. Delete User")

    print("\nTICKET MANAGEMENT")
    print("5. Create Ticket")
    print("6. View All Tickets")
    print("7. View Ticket Details")
    print("8. Search Tickets")
    print("9. Update Ticket Status")
    print("10. Assign Ticket")
    print("11. Add Comment")
    print("12. Delete Ticket")

    print("\nREPORTS")
    print("13. Ticket Statistics")

    print("\n14. Exit")

    print("=" * 60)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_user()

        elif choice == "2":
            view_users()

        elif choice == "3":
            search_user()

        elif choice == "4":
            delete_user()

        elif choice == "5":
            create_ticket()

        elif choice == "6":
            view_tickets()

        elif choice == "7":
            view_ticket_details()

        elif choice == "8":
            search_tickets()

        elif choice == "9":
            update_status()

        elif choice == "10":
            assign_ticket()

        elif choice == "11":
            add_comment()

        elif choice == "12":
            delete_ticket()

        elif choice == "13":
            ticket_statistics()

        elif choice == "14":
            print("Thank you for using Help Desk Ticket System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
