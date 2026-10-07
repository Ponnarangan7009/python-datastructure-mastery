# 13_map.py
"""
Python map() - Learning Notes

Topics:
1. What map() is
2. map(function, iterable)
3. list(map(...))
4. map() with normal functions
5. map() with lambda
6. map() with multiple iterables
7. map() with strings
8. map() with automation-style data
9. print() vs return when using map()
"""


# ============================================================
# 1. WHAT map() IS
# ============================================================

"""
map() applies a function to every item in an iterable.

General syntax:

map(function, iterable)

Example:

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

Output:
[2, 4, 6, 8]
"""


# ============================================================
# 2. map(function, iterable)
# ============================================================

"""
map() takes:

1. A function
2. An iterable

The function is applied to each item.

Example:

numbers = [1, 2, 3, 4]

def double(number):
    return number * 2

result = map(double, numbers)

print(list(result))

Output:
[2, 4, 6, 8]
"""


# ============================================================
# 3. list(map(...))
# ============================================================

"""
map() returns a map object (iterator).

To see all the results as a list, we commonly use list().

Example:

numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)

The output is a map object.

To get the actual values:

print(list(result))

Output:
[2, 4, 6]
"""


# ============================================================
# 4. map() WITH NORMAL FUNCTIONS
# ============================================================

"""
We can pass a normal user-defined function to map().

Example:

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))

Output:
[1, 4, 9, 16]

Important:

The function should RETURN the transformed value
if we want map() to collect the results.
"""


# ============================================================
# 5. map() WITH lambda
# ============================================================

"""
lambda is useful when the transformation is simple.

Example:

numbers = [10, 20, 30]

result = map(lambda x: x + 5, numbers)

print(list(result))

Output:
[15, 25, 35]

Equivalent normal function:

def add_five(x):
    return x + 5
"""


# ============================================================
# 6. map() WITH MULTIPLE ITERABLES
# ============================================================

"""
map() can accept multiple iterables.

Example:

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = map(lambda x, y: x + y, numbers1, numbers2)

print(list(result))

Output:
[11, 22, 33]

Here:

x receives an item from numbers1
y receives an item from numbers2

The function is called like:

1 + 10
2 + 20
3 + 30
"""


# IMPORTANT:
"""
When using multiple iterables, map() stops when the
SHORTEST iterable is exhausted.

Example:

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]

result = map(lambda x, y: x + y, numbers1, numbers2)

print(list(result))

Output:
[11, 22]
"""


# ============================================================
# 7. map() WITH STRINGS
# ============================================================

"""
map() can transform strings as well.

Example:

names = ["alice", "bob", "charlie"]

result = map(str.upper, names)

print(list(result))

Output:

['ALICE', 'BOB', 'CHARLIE']

Here str.upper is a function that is applied
to every string.
"""


# Another example:

"""
names = ["alice", "bob", "charlie"]

result = map(str.title, names)

print(list(result))

Output:

['Alice', 'Bob', 'Charlie']
"""


# ============================================================
# 8. map() WITH AUTOMATION-STYLE DATA
# ============================================================

"""
map() is useful when transforming test data.

Example:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

def get_test_name(data):
    return data[0]

output = list(map(get_test_name, test_results))

print(output)

Output:

['login', 'payment', 'search']
"""


# Another example:

"""
test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

def get_status(data):
    return data[1]

statuses = list(map(get_status, test_results))

print(statuses)

Output:

['PASS', 'FAIL', 'PASS']
"""


# ============================================================
# 9. print() vs return() WHEN USING map()
# ============================================================

"""
print()
-------
Displays something on the screen.

return
------
Sends a value back to the caller.

Example using print():

def get_test_name(data):
    print(data[0])

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

output = list(map(get_test_name, test_results))

The names are printed:

login
payment
search

BUT:

output will be:

[None, None, None]

Why?

Because the function printed the value but did not return it.
"""


# Using return:

"""
def get_test_name(data):
    return data[0]

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

output = list(map(get_test_name, test_results))

print(output)

Output:

['login', 'payment', 'search']
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. map() applies a function to every item.

2. Basic syntax:

   map(function, iterable)

3. map() returns a map object.

4. Use list(map(...)) when you want the results as a list.

5. map() can work with normal functions.

6. map() can work with lambda.

7. map() can work with multiple iterables.

8. With multiple iterables, map() stops at the shortest one.

9. map() can transform strings.

10. map() is useful for transforming automation test data.

11. print() displays a value.

12. return sends a value back to the caller.

13. When using map(), use return when you want map()
    to collect transformed values.
"""
