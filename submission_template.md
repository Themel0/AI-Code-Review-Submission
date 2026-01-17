# AI Code Review Assignment (Python)

## Candidate

- Name: Melike Uysal
- Approximate time spent: 1 hour 30 mins

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- In order to calculate the average of order value we need to find the count of valid orders (in this case they are the not cancelled ones). However in the original code, the division was made by the count of all orders which may include cancelled order's amount as well.

### Edge cases & risks

- There was not a division by 0 check for total/count calculation.
- order["amount"] and order["status"] are crash prone if order does not have that fields.

### Code quality / design issues

- It has some misleading variable naming such as the variable count was initialized as len(orders), but it was used as the divisor for a sum that filtered out items. There is a mismatch between what it actually stores and its purpose which causes a logic error.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added a validity check for the count of items.
- Implemented division by 0 check.
- Swapped crash prone indexing with functions who return None if the field does not exists.
- Added a a type check for the order's amount in case of erronous input for that field.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Test a list containing mixed statuses
- Test a list which is empty to check divide by zero.
- Test inputs with missing "amount" and "status" fields to ensure .get() handles them properly.
- Test with non-numeric data types in the "amount" field to verify the type check mechanism

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- Average calculation should use the number of orders which are not cancelled however the explanations suggests we should divide it by the total count.

### Rewritten explanation

- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing it by the number of valid orders. It correctly excludes cancelled orders and invalid entries from the calculation.

## 4) Final Judgment

- Decision: Reject
- Justification: It contains a fundamental mathematical error. Additionally, it lacks sufficient handling for missing keys or empty lists.
- Confidence & unknowns: High. The logic error is definitive and must be fixed.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- It lacks all the validity check a standard email checker should implement. It should abide by the official syntax defined in RFC 5322 (Section 3.4)

### Edge cases & risks

- In the AI generated function there is only one check implemented which is to see if it contains a "@". However, this allows cases such as "@", "@@@" or "@user".
- Apart from that there are rules such as the domain part should contain a "." or the username part cannot be empty.
- Again the checking the official documentation is recommended to see all the edge cases the AI generated version ignores.

### Code quality / design issues

- An external email checker library would be the more readable and solid answer to this problem. If external usage is not permitted another solution can be usage of regular expressions.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Implemented a practical subset of the official rules of the valid syntax for an email compatible with modern web standards.
- Included a "@" count checker which the original lacked.
- Added a check to see if username or domain fields are empty.
- Implemented a check to see if domain field contains a ".".

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?
The test scenarios for this function should include,

- Test inputs with missing usernames or missing domains.
- Test inputs with multiple separators ("@")
- Test domains without extensions

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- It is inaccurately claiming that it is "safely ignoring invalid entries" but it fails to consider most cases. It also implies a level of validation that does not exist in the code, instilling a false level of confidence.

### Rewritten explanation

-This function validates email syntax by performing structural checks. It verifies that each email contains exactly one "@" symbol, has non-empty username and domain sections, and includes a valid domain extension (indicated by a period).

## 4) Final Judgment

- Decision: Reject
- Justification: The original code is functionally incorrect. It relies on a single check which yields to a high false-positive rate, accepting erronous input.
- Confidence & unknowns: The complexity of the validity check may depend on the user intent.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- To calculate the average of valid measurements we need to find the count of valid value(excluding None). However in the original code, the division was made by the count of all values (including None) which may include invalid measurements as well.

### Edge cases & risks

- There is no division by zero check for total/count calculation.
- It does not check if the values are actually numbers(strings or objects could cause a crash).

### Code quality / design issues

- It contains misleading variable naming since count stores len(values) but it was used as the divisor for a sum that filtered out items. There is a mismatch between what it stores and how its functionality.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added a separate counter for valid values to ensure the average is calculated correctly.
- Included a divison-by-zero check.
- Implemented a type check for values.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Test with empty list to verify handling of divison by zero.
- Test with a list containing only invalid values.
- Test with list containing non-numeric values to check type handling.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- It does not safely handle mixed input types and the calculation error prevents it from getting an accurate average.

### Rewritten explanation

- This function calculates the average of valid measurements by ignoring missing (None) and non-numeric entries, and averaging the remaining values. It safely handles mixed input types, division-by-zero errors and ensures an accurate average.

## 4) Final Judgment

- Decision: Reject
- Justification: It contains a fundamental mathematical error (incorrect denominator) and fails to implement necessary type checks, making it crash prone.
- Confidence & unknowns: High.
