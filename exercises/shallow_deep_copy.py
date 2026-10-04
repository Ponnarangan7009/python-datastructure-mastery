# ==========================================
# SHALLOW COPY vs DEEP COPY - EXERCISES
# ==========================================

import copy


# ------------------------------------------
# Q1 - Assignment (=)
# ------------------------------------------

a = [10, 20, 30]
b = a

b.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30, 40]

# a and b refer to the same list object.


# ------------------------------------------
# Q2 - Shallow Copy
# ------------------------------------------

a = [10, 20, 30]
b = a.copy()

b.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30]
# [10, 20, 30, 40]

# a and b are different outer list objects.


# ------------------------------------------
# Q3 - Nested Shallow Copy
# ------------------------------------------

a = [
    [1, 2],
    [3, 4]
]

b = a.copy()

b[1][0] = 300

print(a)
print(b)

# Output:
# [[1, 2], [300, 4]]
# [[1, 2], [300, 4]]

# The outer lists are different,
# but the inner lists are shared.


# ------------------------------------------
# Q4 - Deep Copy
# ------------------------------------------

a = [
    [1, 2],
    [3, 4]
]

b = copy.deepcopy(a)

b[1][0] = 300

print(a)
print(b)

# Output:
# [[1, 2], [3, 4]]
# [[1, 2], [300, 4]]

# Deep copy creates independent
# outer and inner lists.


# ------------------------------------------
# Q5 - Identity Test
# ------------------------------------------

a = [[1, 2], [3, 4]]

b = a
c = a.copy()
d = copy.deepcopy(a)

print(a is b)
print(a is c)
print(a is d)

print(a[0] is b[0])
print(a[0] is c[0])
print(a[0] is d[0])

# Output:
# True
# False
# False
# True
# True
# False


# ------------------------------------------
# Q6 - Automation Testing Scenario
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

# Output:
# [['login', 'PASS'], ['payment', 'FAIL'], ['search', 'PASS']]
# [['login', 'PASS'], ['payment', 'PASS'], ['search', 'PASS']]

# The original test_results remains unchanged.


# ------------------------------------------
# Q7 - Challenge
# ------------------------------------------

a = [[1, 2], [3, 4]]

b = a.copy()
c = copy.deepcopy(a)

b[0].append(99)
c[1].append(88)

print(a)
print(b)
print(c)

# Output:
# [[1, 2, 99], [3, 4]]
# [[1, 2, 99], [3, 4]]
# [[1, 2], [3, 4, 88]]

# b shares the inner lists with a.
# c has completely independent inner lists.
