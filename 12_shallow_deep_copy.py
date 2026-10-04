# ==========================================
# SHALLOW COPY vs DEEP COPY
# ==========================================

import copy


# ------------------------------------------
# 1. Assignment (=)
# ------------------------------------------

numbers = [10, 20, 30]

other = numbers

other[0] = 100

print(numbers)
print(other)

# Both change because both variables refer
# to the SAME list object.


# ------------------------------------------
# 2. Shallow Copy - copy()
# ------------------------------------------

numbers = [10, 20, 30]

other = numbers.copy()

other[0] = 100

print(numbers)
print(other)

# The outer lists are DIFFERENT objects.


# ------------------------------------------
# 3. Shallow Copy with Nested Lists
# ------------------------------------------

numbers = [
    [1, 2],
    [3, 4]
]

other = numbers.copy()

other[0][0] = 100

print(numbers)
print(other)

# Output:
# [[100, 2], [3, 4]]
# [[100, 2], [3, 4]]

# Why?
# copy() creates a new OUTER list,
# but the INNER lists are still shared.


# ------------------------------------------
# 4. Deep Copy
# ------------------------------------------

numbers = [
    [1, 2],
    [3, 4]
]

other = copy.deepcopy(numbers)

other[0][0] = 100

print(numbers)
print(other)

# Output:
# [[1, 2], [3, 4]]
# [[100, 2], [3, 4]]

# Deep copy creates independent
# outer AND nested objects.


# ------------------------------------------
# 5. Three Copying Methods
# ------------------------------------------

numbers = [
    [1, 2],
    [3, 4]
]

# Assignment
a = numbers

# Shallow copy
b = numbers.copy()

# Deep copy
c = copy.deepcopy(numbers)


# Mental model:
#
# a = numbers
# SAME outer list
# SAME inner lists
#
# b = numbers.copy()
# DIFFERENT outer list
# SAME inner lists
#
# c = copy.deepcopy(numbers)
# DIFFERENT outer list
# DIFFERENT inner lists


# ------------------------------------------
# 6. Checking Object Identity
# ------------------------------------------

numbers = [
    [1, 2],
    [3, 4]
]

a = numbers
b = numbers.copy()
c = copy.deepcopy(numbers)

print(a is numbers)       # True
print(b is numbers)       # False
print(c is numbers)       # False

print(a[0] is numbers[0]) # True
print(b[0] is numbers[0]) # True
print(c[0] is numbers[0]) # False


# ------------------------------------------
# 7. Automation Testing Example
# ------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

backup_results = copy.deepcopy(test_results)

backup_results[1][1] = "PASS"

print(test_results)
print(backup_results)

# Original test_results remains unchanged.
# backup_results can be modified independently.
