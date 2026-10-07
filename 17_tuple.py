"""
TUPLES - PYTHON LEARNING NOTES
==============================

A tuple is an ordered collection of values.

Main properties:
- Ordered
- Immutable
- Allows duplicate values
- Supports indexing
- Supports slicing
"""


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)


# ============================================================
# 2. TUPLE CAN CONTAIN DIFFERENT DATA TYPES
# ============================================================

test = ("login", "PASS", 120, "Chrome")

print(test)


# ============================================================
# 3. DUPLICATE VALUES ARE ALLOWED
# ============================================================

results = ("PASS", "FAIL", "PASS", "PASS")

print(results)


# ============================================================
# 4. INDEXING
# ============================================================

test = ("login", "PASS", 120, "Chrome")

print(test[0])
print(test[1])
print(test[-1])


# ============================================================
# 5. SLICING
# ============================================================

test = ("login", "PASS", 120, "Chrome", "Android")

print(test[1:4])
print(test[-2:])


# ============================================================
# 6. TUPLES ARE IMMUTABLE
# ============================================================

test = ("login", "PASS", 120)

# test[1] = "FAIL"
# ❌ TypeError

# Existing tuple elements cannot be changed.


# ============================================================
# 7. SINGLE-ELEMENT TUPLE
# ============================================================

value = (10,)

print(type(value))


# Without the comma, this is an integer:

value = (10)

print(type(value))


# ============================================================
# 8. len()
# ============================================================

test = ("login", "PASS", 120, "Chrome")

print(len(test))


# ============================================================
# 9. count()
# ============================================================

results = ("PASS", "FAIL", "PASS", "PASS", "FAIL")

print(results.count("PASS"))


# ============================================================
# 10. index()
# ============================================================

results = ("PASS", "FAIL", "PASS", "PASS", "FAIL")

print(results.index("FAIL"))


# ============================================================
# 11. MEMBERSHIP - in
# ============================================================

statuses = ("PASS", "FAIL", "SKIPPED")

print("PASS" in statuses)
print("BLOCKED" in statuses)


# ============================================================
# 12. ITERATING THROUGH A TUPLE
# ============================================================

statuses = ("PASS", "FAIL", "SKIPPED")

for status in statuses:
    print(status)


# ============================================================
# 13. TUPLE CONCATENATION
# ============================================================

test = ("login", "PASS")

test = test + (120, "Chrome")

print(test)


# ============================================================
# 14. TUPLE REPETITION
# ============================================================

data = ("PASS", "FAIL")

result = data * 2

print(result)

# Output:
# ("PASS", "FAIL", "PASS", "FAIL")


# ============================================================
# 15. += WITH A TUPLE
# ============================================================

test = ("login", "PASS", 120)

test += ("Chrome",)

print(test)

# This creates a NEW tuple and reassigns it to test.
#
# It does NOT modify the original tuple.


# ============================================================
# 16. TUPLE UNPACKING
# ============================================================

test = ("login", "PASS", 120)

name, status, time = test

print(name)
print(status)
print(time)


# ============================================================
# 17. STARRED UNPACKING
# ============================================================

test = ("login", "PASS", 120, "Chrome")

name, status, *details = test

print(name)
print(status)
print(details)

# Output:
# login
# PASS
# [120, "Chrome"]
#
# The starred variable receives the remaining values
# as a LIST.


# ============================================================
# 18. NESTED TUPLES
# ============================================================

test_results = (
    ("login", "PASS"),
    ("search", "FAIL"),
    ("checkout", "PASS")
)

print(test_results[1])
print(test_results[1][0])
print(test_results[1][1])


# ============================================================
# 19. LIST TO TUPLE
# ============================================================

data = ["login", "PASS", 120]

result = tuple(data)

print(result)


# ============================================================
# 20. TUPLE TO LIST
# ============================================================

data = ("login", "PASS", 120)

result = list(data)

print(result)


# ============================================================
# 21. MUTABLE OBJECT INSIDE A TUPLE
# ============================================================

data = ("login", ["PASS", "FAIL"])

data[1].append("SKIPPED")

print(data)

# Output:
# ("login", ["PASS", "FAIL", "SKIPPED"])
#
# The tuple itself is immutable.
# But the list inside the tuple is mutable.


# ============================================================
# 22. TUPLE AS A DICTIONARY KEY
# ============================================================

test_results = {
    ("login", "Chrome"): "PASS",
    ("login", "Firefox"): "FAIL"
}

print(test_results[("login", "Chrome")])

# Tuples can be dictionary keys when all their
# elements are hashable.


# ============================================================
# 23. HASHABILITY
# ============================================================

"""
Hashable objects can be used as dictionary keys
and elements of a set.

Common hashable types:
- int
- float
- str
- bool
- tuple (if all elements are hashable)

Common unhashable types:
- list
- set
- dict
"""


# This works:

data = {
    (1, 2): "value"
}

print(data)


# This does NOT work:

# data = {
#     (1, [2, 3]): "value"
# }
#
# ❌ TypeError: unhashable type: 'list'


# ============================================================
# 24. LIST vs TUPLE
# ============================================================

"""
LIST
-----
- Ordered
- Mutable
- Allows duplicates
- Supports indexing
- Supports slicing

TUPLE
-----
- Ordered
- Immutable
- Allows duplicates
- Supports indexing
- Supports slicing
"""


# ============================================================
# 25. AUTOMATION EXAMPLE
# ============================================================

test_case = ("login", "valid_user", "PASS")

name, test_data, status = test_case

print(name)
print(test_data)
print(status)


# ============================================================
# 26. AUTOMATION EXAMPLE - TEST CONFIGURATION
# ============================================================

test_config = ("Chrome", "Android", "production")

browser, platform, environment = test_config

print(browser)
print(platform)
print(environment)


# ============================================================
# 27. IMPORTANT INTERVIEW POINTS
# ============================================================

"""
Remember:

1. Tuple is ORDERED.

2. Tuple is IMMUTABLE.

3. Tuple allows DUPLICATE values.

4. Tuple supports INDEXING.

5. Tuple supports SLICING.

6. A single-element tuple requires a comma:
       (10,)

7. count() counts occurrences.

8. index() returns the first matching index.

9. Tuples support unpacking.

10. *variable during unpacking collects remaining
    values into a LIST.

11. Tuple can contain mutable objects such as lists.

12. A tuple can be a dictionary key if all its
    elements are hashable.

13. tuple(list) converts a list to a tuple.

14. list(tuple) converts a tuple to a list.

15. += with a tuple creates a new tuple and
    reassigns the variable.
"""
