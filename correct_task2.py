# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    count = 0
    for email in emails:
        if email.count("@") != 1:
            continue
        username, domain = email.split("@")

        if not username or not domain:
            continue

        if "." not in domain:
            continue

        count += 1

    return count
