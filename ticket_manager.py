from config import (
    TICKET_FILE,
    USER_FILE,
    PRIORITIES,
    STATUSES
)

from storage import load_data, save_data
from utils import (
    generate_id,
    find_by_id,
    get_current_datetime
)


def create_ticket():
    tickets = load_data(TICKET_FILE)
    users = load_data(USER_FILE)

    if not users:
        print("Please create a user first.")
        return

    print("\nAvailable Users:")

    for user in users:
        print(
            f"{user['id']} - "
            f"{user['name']} - "
            f"{user['department']}"
        )

    user_id = input("\nEnter User ID: ").strip()

    user = find_by_id(users, user_id)

    if not user:
        print("User not found.")
        return

    title = input("Enter ticket title: ").strip()
    description = input("Enter problem description: ").strip()

    if not title or not description:
        print("Title and description are required.")
        return

    print("\nPriority")
    for index, priority in enumerate(PRIORITIES, start=1):
        print(f"{index}. {priority}")

    try:
        priority_choice = int(input("Select priority: "))
        priority = PRIORITIES[priority_choice - 1]
    except (ValueError, IndexError):
        print("Invalid priority.")
        return

    ticket = {
        "id": generate_id(tickets, "T"),
        "title": title,
        "description": description,
        "user_id": user["id"],
        "user_name": user["name"],
        "department": user["department"],
        "priority": priority,
        "status": "Open",
        "assigned_to": "",
        "created_at": get_current_datetime(),
        "updated_at": get_current_datetime(),
        "comments": []
    }

    tickets.append(ticket)

    save_data(TICKET_FILE, tickets)

    print("\nTicket created successfully.")
    print(f"Ticket ID: {ticket['id']}")


def view_tickets():
    tickets = load_data(TICKET_FILE)

    if not tickets:
        print("No tickets found.")
        return

    print("\n" + "=" * 90)
    print("ALL TICKETS")
    print("=" * 90)

    for ticket in tickets:
        print(f"ID          : {ticket['id']}")
        print(f"Title       : {ticket['title']}")
        print(f"User        : {ticket['user_name']}")
        print(f"Department  : {ticket['department']}")
        print(f"Priority    : {ticket['priority']}")
        print(f"Status      : {ticket['status']}")
        print(f"Assigned To : {ticket['assigned_to'] or 'Not Assigned'}")
        print(f"Created     : {ticket['created_at']}")
        print("-" * 90)


def view_ticket_details():
    tickets = load_data(TICKET_FILE)

    ticket_id = input("Enter Ticket ID: ").strip()

    ticket = find_by_id(tickets, ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    print("\n" + "=" * 70)
    print("TICKET DETAILS")
    print("=" * 70)

    print(f"ID          : {ticket['id']}")
    print(f"Title       : {ticket['title']}")
    print(f"Description : {ticket['description']}")
    print(f"User        : {ticket['user_name']}")
    print(f"Department  : {ticket['department']}")
    print(f"Priority    : {ticket['priority']}")
    print(f"Status      : {ticket['status']}")
    print(f"Assigned To : {ticket['assigned_to'] or 'Not Assigned'}")
    print(f"Created     : {ticket['created_at']}")
    print(f"Updated     : {ticket['updated_at']}")

    print("\nComments:")

    if not ticket["comments"]:
        print("No comments.")
    else:
        for comment in ticket["comments"]:
            print(
                f"- {comment['date']} | "
                f"{comment['user']}: "
                f"{comment['text']}"
            )


def search_tickets():
    tickets = load_data(TICKET_FILE)

    keyword = input(
        "Enter ticket ID, title, user, or department: "
    ).strip().lower()

    results = [
        ticket
        for ticket in tickets
        if keyword in ticket["id"].lower()
        or keyword in ticket["title"].lower()
        or keyword in ticket["user_name"].lower()
        or keyword in ticket["department"].lower()
    ]

    if not results:
        print("No tickets found.")
        return

    print("\nSearch Results")

    for ticket in results:
        print(
            f"{ticket['id']} | "
            f"{ticket['title']} | "
            f"{ticket['priority']} | "
            f"{ticket['status']}"
        )


def update_status():
    tickets = load_data(TICKET_FILE)

    ticket_id = input("Enter Ticket ID: ").strip()

    ticket = find_by_id(tickets, ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    print("\nStatus Options")

    for index, status in enumerate(STATUSES, start=1):
        print(f"{index}. {status}")

    try:
        choice = int(input("Select status: "))
        new_status = STATUSES[choice - 1]
    except (ValueError, IndexError):
        print("Invalid status.")
        return

    ticket["status"] = new_status
    ticket["updated_at"] = get_current_datetime()

    save_data(TICKET_FILE, tickets)

    print("Ticket status updated successfully.")


def assign_ticket():
    tickets = load_data(TICKET_FILE)

    ticket_id = input("Enter Ticket ID: ").strip()

    ticket = find_by_id(tickets, ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    technician = input("Enter technician name: ").strip()

    if not technician:
        print("Technician name cannot be empty.")
        return

    ticket["assigned_to"] = technician
    ticket["updated_at"] = get_current_datetime()

    save_data(TICKET_FILE, tickets)

    print("Ticket assigned successfully.")


def add_comment():
    tickets = load_data(TICKET_FILE)

    ticket_id = input("Enter Ticket ID: ").strip()

    ticket = find_by_id(tickets, ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    user = input("Enter your name: ").strip()
    text = input("Enter comment: ").strip()

    if not user or not text:
        print("User name and comment are required.")
        return

    comment = {
        "user": user,
        "text": text,
        "date": get_current_datetime()
    }

    ticket["comments"].append(comment)
    ticket["updated_at"] = get_current_datetime()

    save_data(TICKET_FILE, tickets)

    print("Comment added successfully.")


def delete_ticket():
    tickets = load_data(TICKET_FILE)

    ticket_id = input("Enter Ticket ID: ").strip()

    ticket = find_by_id(tickets, ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    tickets.remove(ticket)

    save_data(TICKET_FILE, tickets)

    print("Ticket deleted successfully.")


def ticket_statistics():
    tickets = load_data(TICKET_FILE)

    if not tickets:
        print("No ticket data available.")
        return

    total = len(tickets)

    open_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "Open"
    )

    progress_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "In Progress"
    )

    resolved_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "Resolved"
    )

    closed_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "Closed"
    )

    critical_count = sum(
        1 for ticket in tickets
        if ticket["priority"] == "Critical"
    )

    print("\n" + "=" * 50)
    print("TICKET STATISTICS")
    print("=" * 50)

    print(f"Total Tickets : {total}")
    print(f"Open          : {open_count}")
    print(f"In Progress   : {progress_count}")
    print(f"Resolved      : {resolved_count}")
    print(f"Closed        : {closed_count}")
    print(f"Critical      : {critical_count}")
