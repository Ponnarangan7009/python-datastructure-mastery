# sorted() in Python
#
# sorted() returns a NEW list containing the items
# from an iterable in sorted order.


# ==================================================
# 1. Basic sorted()
# ==================================================

numbers = [30, 10, 50, 20]

result = sorted(numbers)

print(result)

# Output:
# [10, 20, 30, 50]


# ==================================================
# 2. sorted() Does Not Modify the Original List
# ==================================================

numbers = [30, 10, 50, 20]

result = sorted(numbers)

print("Original:", numbers)
print("Sorted:", result)


# ==================================================
# 3. reverse=True
# ==================================================

numbers = [10, 30, 20, 50]

result = sorted(numbers, reverse=True)

print(result)

# Output:
# [50, 30, 20, 10]


# ==================================================
# 4. Sorting Strings
# ==================================================

names = ["Charlie", "Alice", "Bob", "David"]

result = sorted(names)

print(result)

# Output:
# ['Alice', 'Bob', 'Charlie', 'David']


# ==================================================
# 5. key=
# ==================================================

# key tells sorted() what value to use
# when deciding the sorting order.

numbers = [10, 5, 30, 15]

result = sorted(numbers, key=lambda x: x)

print(result)


# ==================================================
# 6. key with len()
# ==================================================

names = ["John", "Alexander", "Bob", "Christopher"]

result = sorted(names, key=len)

print(result)

# Strings are sorted by their length.


# ==================================================
# 7. key with lambda
# ==================================================

names = ["John", "Alexander", "Bob", "Christopher"]

result = sorted(
    names,
    key=lambda name: len(name)
)

print(result)


# ==================================================
# 8. Sorting by String Length in Descending Order
# ==================================================

names = ["John", "Alexander", "Bob", "Christopher"]

result = sorted(
    names,
    key=lambda name: len(name),
    reverse=True
)

print(result)


# ==================================================
# 9. Sorting Nested Lists
# ==================================================

tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300]
]

result = sorted(
    tests,
    key=lambda test: test[1]
)

print(result)

# Output:
# [
#     ["search", 80],
#     ["login", 120],
#     ["checkout", 300],
#     ["payment", 450]
# ]


# ==================================================
# 10. Sorting Nested Lists in Descending Order
# ==================================================

result = sorted(
    tests,
    key=lambda test: test[1],
    reverse=True
)

print(result)


# ==================================================
# 11. Normal Function Instead of Lambda
# ==================================================

def get_execution_time(test):
    return test[1]


result = sorted(
    tests,
    key=get_execution_time
)

print(result)

# Lambda is simply a shorter way to write
# a small function.


# ==================================================
# 12. Automation Testing Example
# ==================================================

test_results = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300]
]

result = sorted(
    test_results,
    key=lambda test: test[2]
)

print(result)

# Sorted by execution time.


# ==================================================
# 13. Sort Tests by Status
# ==================================================

result = sorted(
    test_results,
    key=lambda test: test[1]
)

print(result)

# Python sorts based on the value returned
# by the key function.


# ==================================================
# 14. Complete sorted() Syntax
# ==================================================

# sorted(iterable, key=function, reverse=False)


# Example:

result = sorted(
    test_results,
    key=lambda test: test[2],
    reverse=True
)

print(result)


# ==================================================
# KEY TAKEAWAYS
# ==================================================

# sorted() returns a NEW sorted list.
#
# Basic:
# sorted(data)
#
# Descending:
# sorted(data, reverse=True)
#
# Custom sorting:
# sorted(data, key=function)
#
# Lambda:
# sorted(data, key=lambda item: ...)
#
# The key function tells Python:
# "What value should I use to determine the order?"
#
# key expects a callable/function.
#
# Examples:
#
# key=len
#
# key=lambda x: x[1]
#
# key=lambda x: len(x)
#
# A normal function can also be used:
#
# def get_value(item):
#     return item[1]
#
# sorted(data, key=get_value)
