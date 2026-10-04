
# List Basic unpacking
numbers = [10, 20, 30]
# Unpack the list into:
# a
# b
# c
a, b, c = numbers
print(a, b, c)


# Strings
languages = ["Python", "Java", "C++"]
# Unpack them into:
# language1
# language2
# language3
language1, language2, language3 = languages

# Test data
# Given:
test = ["login", "Pixel", "PASS"]
# Unpack it into:
# test_name
# device
# result
test_name, device, result = test
print(f"Test: {test_name}")
print(f"Device: {device}")
print(f"Result: {result}")
# Print:
# Test: login
# Device: Pixel
# Result: PASS



# Extended unpacking
# Given:
numbers = [10, 20, 30, 40, 50]
# Use * to create:
# first → 10
# middle → [20, 30, 40]
# last → 50
first, *middle, last = numbers

# First two + remaining
# Given:
numbers = [10, 20, 30, 40, 50]
# Create:
# first → 10
# second → 20
# remaining → [30, 40, 50]
first, second, *remaining = numbers

# First + remaining + last
# Given:
numbers = [1, 2, 3, 4, 5, 6]
# Create:
# first → 1
# middle → [2, 3, 4, 5]
# last → 6
first, *middle, last = numbers

# Automation-style challenge
# Given:
test = [    "test_login",    "Pixel",    "Android 16",    "PASS",    "2.5s"]
# Use unpacking to get:
# test_name
# device
# version
# result
# execution_time
test_name, device, version, result, execution_time = test
# Then print:
# Test: test_login
# Device: Pixel
# Version: Android 16
# Result: PASS
# Execution time: 2.5s
print(f"Test: {test_name}")
print(f"Device: {device}")
print(f"Version: {version}")
print(f"Result: {result}")
print(f"Execution time: {execution_time}")
