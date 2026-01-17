# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    valid_count = 0
    for order in orders:
        status = order.get("status")
        amount = order.get("amount")
        if status != "cancelled" and (amount, isinstance(int, float)):
            total += amount
            valid_count += 1

    if valid_count == 0:
        return 0

    return total/valid_count
