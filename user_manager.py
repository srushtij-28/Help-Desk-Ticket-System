from config import USER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_user():
    users = load_data(USER_FILE)

    name = input("Enter user name: ").strip()
    department = input("Enter department: ").strip()
    email = input("Enter email: ").strip()

    if not name or not department or not email:
        print("All fields are required.")
        return

    user = {
        "id": generate_id(users, "U"),
        "name": name,
        "department": department,
        "email": email
    }

    users.append(user)

    save_data(USER_FILE, users)

    print("\nUser added successfully.")
    print(f"User ID: {user['id']}")


def view_users():
    users = load_data(USER_FILE)

    if not users:
        print("No users found.")
        return

    print("\n" + "=" * 70)
    print("USERS")
    print("=" * 70)

    for user in users:
        print(f"ID         : {user['id']}")
        print(f"Name       : {user['name']}")
        print(f"Department : {user['department']}")
        print(f"Email      : {user['email']}")
        print("-" * 70)


def search_user():
    users = load_data(USER_FILE)

    keyword = input("Enter name, ID, or department: ").strip().lower()

    results = [
        user for user in users
        if keyword in user["id"].lower()
        or keyword in user["name"].lower()
        or keyword in user["department"].lower()
    ]

    if not results:
        print("No users found.")
        return

    print("\nSearch Results")

    for user in results:
        print(
            f"{user['id']} | "
            f"{user['name']} | "
            f"{user['department']} | "
            f"{user['email']}"
        )


def delete_user():
    users = load_data(USER_FILE)

    user_id = input("Enter User ID: ").strip()

    user = find_by_id(users, user_id)

    if not user:
        print("User not found.")
        return

    users.remove(user)

    save_data(USER_FILE, users)

    print("User deleted successfully.")
