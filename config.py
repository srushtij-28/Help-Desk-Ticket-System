import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

TICKET_FILE = os.path.join(DATA_DIR, "tickets.json")
USER_FILE = os.path.join(DATA_DIR, "users.json")

DEFAULT_STATUS = "Open"

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

STATUSES = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]
