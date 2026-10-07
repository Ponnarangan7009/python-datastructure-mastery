```python
# Lambda Exercises
#
# Practice exercises for lambda functions.
# Try solving the questions first.
# Answers are provided at the bottom.


# ==================================================
# EXERCISE 1
# ==================================================
# Create a lambda function that takes a number
# and returns its square.

square = lambda x: x * x

print(square(6))


# ==================================================
# EXERCISE 2
# ==================================================
# Create a lambda function that takes two numbers
# and returns their sum.

add = lambda x, y: x + y

print(add(10, 25))


# ==================================================
# EXERCISE 3
# ==================================================
# Create a lambda function that returns True
# if a number is even, otherwise False.

is_even = lambda x: x % 2 == 0

print(is_even(8))
print(is_even(7))


# ==================================================
# EXERCISE 4
# ==================================================
# Use lambda with map() to multiply every number by 10.

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 10, numbers))

print(result)


# ==================================================
# EXERCISE 5
# ==================================================
# Use lambda with filter() to keep numbers
# greater than 15.

numbers = [5, 10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 15, numbers))

print(result)


# ==================================================
# EXERCISE 6
# ==================================================
# Use lambda with filter() to keep names
# that start with "A".

names = ["Alice", "Bob", "Andrew", "Charlie", "Amanda"]

result = list(filter(lambda x: x.startswith("A"), names))

print(result)


# ==================================================
# EXERCISE 7
# ==================================================
# Create a lambda that returns:
# "PASS" if score >= 50
# "FAIL" otherwise.

get_status = lambda x: "PASS" if x >= 50 else "FAIL"

print(get_status(75))
print(get_status(40))


# ==================================================
# EXERCISE 8
# ==================================================
# Use lambda with filter() to keep only
# failed tests.

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

result = list(
    filter(lambda x: x[1] == "FAIL", test_results)
)

print(result)


# ==================================================
# EXERCISE 9
# ==================================================
# Use filter() to select failed tests,
# then map() to return only their names
# in uppercase.

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

result = list(
    map(
        lambda x: x[0].upper(),
        filter(lambda x: x[1] == "FAIL", test_results)
    )
)

print(result)


# ==================================================
# EXERCISE 10
# ==================================================
# Create a lambda with two parameters
# that returns their product.

multiply = lambda x, y: x * y

print(multiply(5, 8))


# ==================================================
# EXERCISE 11
# ==================================================
# Keep only numbers that are:
# 1. Greater than 20
# 2. Even

numbers = [10, 15, 20, 25, 30, 35, 40]

result = list(
    filter(lambda x: x > 20 and x % 2 == 0, numbers)
)

print(result)


# ==================================================
# EXERCISE 12
# ==================================================
# Use lambda with map() to convert
# every name to uppercase.

names = ["alice", "bob", "charlie", "david"]

result = list(
    map(lambda x: x.upper(), names)
)

print(result)


# ==================================================
# EXERCISE 13
# ==================================================
# Keep only tests that:
# 1. Have status "PASS"
# 2
