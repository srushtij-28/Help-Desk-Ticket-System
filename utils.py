from datetime import datetime


def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_id(items, prefix):
    if not items:
        return f"{prefix}001"

    numbers = []

    for item in items:
        item_id = item.get("id", "")

        if item_id.startswith(prefix):
            try:
                number = int(item_id[len(prefix):])
                numbers.append(number)
            except ValueError:
                pass

    next_number = max(numbers, default=0) + 1

    return f"{prefix}{next_number:03d}"


def find_by_id(items, item_id):
    for item in items:
        if item.get("id", "").lower() == item_id.lower():
            return item

    return None
