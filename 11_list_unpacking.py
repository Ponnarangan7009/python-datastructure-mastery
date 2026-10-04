# Python List Mastery
# Topic: List Unpacking

# List unpacking allows us to assign the elements
# of a list to individual variables.

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30


# Unpacking works based on position.

languages = ["Python", "Java", "C++"]

language1, language2, language3 = languages

print(language1)
print(language2)
print(language3)

# Output:
# Python
# Java
# C++


# The number of variables normally needs to match
# the number of elements in the list.

numbers = [10, 20, 30]

a, b, c = numbers

print(a, b, c)


# Extended unpacking
#
# The * operator collects multiple remaining elements
# into a list.

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


# First two elements + remaining elements

numbers = [10, 20, 30, 40, 50]

first, second, *remaining = numbers

print(first)
print(second)
print(remaining)

# Output:
# 10
# 20
# [30, 40, 50]


# Remaining elements + last element

numbers = [10, 20, 30, 40, 50]

*beginning, last = numbers

print(beginning)
print(last)

# Output:
# [10, 20, 30, 40]
# 50


# The * operator can collect the middle elements.

numbers = [1, 2, 3, 4, 5, 6]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 1
# [2, 3, 4, 5]
# 6


# Automation-style example

test = [
    "test_login",
    "Pixel",
    "Android 16",
    "PASS",
    "2.5s"
]

test_name, device, version, result, execution_time = test

print(f"Test: {test_name}")
print(f"Device: {device}")
print(f"Version: {version}")
print(f"Result: {result}")
print(f"Execution time: {execution_time}")


# List unpacking is also used with tuples and other iterables,
# but here we are focusing on its use with lists.


# Connection with zip()
#
# When we write:
#
# for device, version, result in zip(devices, versions, results):
#
# Python is also unpacking each item returned by zip()
# into the variables device, version, and result.
