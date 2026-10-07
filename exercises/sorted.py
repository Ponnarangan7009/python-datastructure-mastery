# ============================================
# SORTED() — EXERCISES
# ============================================


# Exercise 1
# Sort the numbers in ascending order.

numbers = [40, 10, 30, 20, 50]

# Expected:
# [10, 20, 30, 40, 50]


# Exercise 2
# Use sorted() and store the result in a new variable.
# Check whether the original list changes.

numbers = [40, 10, 30, 20]

# Expected:
# numbers -> [40, 10, 30, 20]
# result  -> [10, 20, 30, 40]


# Exercise 3
# Sort the numbers in descending order using reverse=True.

numbers = [40, 10, 30, 20]

# Expected:
# [40, 30, 20, 10]


# Exercise 4
# Sort these names alphabetically.

names = ["Charlie", "Alice", "Bob", "David"]

# Expected:
# ["Alice", "Bob", "Charlie", "David"]


# Exercise 5
# Sort the names by their length using key=len.

names = ["Alexander", "Bob", "John", "David"]

# Expected:
# ["Bob", "John", "David", "Alexander"]


# Exercise 6
# Sort the names by length using lambda.

names = ["Alexander", "Bob", "John", "David"]

# Use:
# key=lambda ...


# Exercise 7
# Sort the tests by execution time (second element).

tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300]
]

# Expected:
# [
#     ["search", 80],
#     ["login", 120],
#     ["checkout", 300],
#     ["payment", 450]
# ]


# Exercise 8
# Sort the same tests by execution time,
# but from slowest to fastest.

tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300]
]

# Use reverse=True.


# Exercise 9
# Create a normal function called get_time()
# that returns the execution time.
# Use it as the key for sorted().

def get_time(test):
    # your code


tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80]
]


# Exercise 10
# Sort these names by length from longest to shortest.

names = ["Alexander", "Bob", "Christopher", "Dan"]

# Use:
# key=len
# reverse=True


# Exercise 11
# Sort the tests by execution time from
# highest to lowest.

tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300]
]

# Use lambda and reverse=True.


# Exercise 12
# Use the get_time() function from Exercise 9.
# Sort the tests from highest execution time
# to lowest execution time.

# Use reverse=True.


# Exercise 13
# Sort these tests by execution time.

tests = [
    ["search", "PASS", 80],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300]
]

# Hint:
# execution time is test[2]


# Exercise 14
# Sort first by status and then by execution time.

tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300]
]

# Use:
# key=lambda test: (test[1], test[2])


# Exercise 15
# We want PASS tests first and FAIL tests second.
# Within each status, sort by execution time.

tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300]
]

status_order = {
    "PASS": 0,
    "FAIL": 1
}

# Use status_order inside the key.


# ============================================
# FINAL CHALLENGE
# ============================================

# Keep only PASS tests,
# sort them by execution time,
# then convert their names to uppercase.

tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "PASS", 300],
    ["profile", "FAIL", 200]
]

# Use:
# filter()
# sorted()
# map()
# lambda
