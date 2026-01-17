# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    count = len(orders)

    if count > 0:
        for order in orders:
            status = order.get("status")
            amount = order.get("amount")
            if status != "cancelled":
                total += amount

        return total/count

    return 0
