# 14_filter.py
"""
Python filter() - Learning Notes

Topics:
1. What filter() is
2. filter(function, iterable)
3. list(filter(...))
4. filter() with normal functions
5. filter() with lambda
6. Filtering numbers
7. Filtering strings
8. Filtering automation-style data
9. Boolean conditions with filter()
10. Truthiness with filter()
11. filter() vs map()
12. Combining filter() and map()
"""


# ============================================================
# 1. WHAT filter() IS
# ============================================================

"""
filter() selects items from an iterable based on a condition.

It does NOT transform the items.

General syntax:

filter(function, iterable)

Example:

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

Output:

[2, 4, 6]
"""


# ============================================================
# 2. filter(function, iterable)
# ============================================================

"""
filter() takes:

1. A function
2. An iterable

The function should determine whether each item should
be kept.

Example:

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4]

result = filter(is_even, numbers)

print(list(result))

Output:

[2, 4]
"""


# ============================================================
# 3. list(filter(...))
# ============================================================

"""
filter() returns a filter object (iterator).

To get the actual values as a list:

numbers = [1, 2, 3, 4]

result = filter(lambda x: x > 2, numbers)

print(list(result))

Output:

[3, 4]
"""


# ============================================================
# 4. filter() WITH NORMAL FUNCTIONS
# ============================================================

"""
Example:

def is_positive(number):
    return number > 0

numbers = [-5, 10, -2, 0, 8]

result = filter(is_positive, numbers)

print(list(result))

Output:

[10, 8]
"""


# ============================================================
# 5. filter() WITH lambda
# ============================================================

"""
lambda is useful for simple filtering conditions.

Example:

numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x >= 25, numbers)

print(list(result))

Output:

[25, 30]
"""


# ============================================================
# 6. FILTERING NUMBERS
# ============================================================

"""
Keep only even numbers:

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

Output:

[2, 4, 6]
"""


# Multiple conditions:

"""
numbers = [5, 12, 18, 21, 30, 35, 40]

result = filter(
    lambda x: x % 2 == 0 and x > 20,
    numbers
)

print(list(result))

Output:

[30, 40]
"""


# ============================================================
# 7. FILTERING STRINGS
# ============================================================

"""
Example:

names = ["Alice", "Bob", "Amanda", "John", "Andrew"]

result = filter(
    lambda name: name.startswith("A"),
    names
)

print(list(result))

Output:

['Alice', 'Amanda', 'Andrew']
"""


# Another example:

"""
test_names = [
    "login_test",
    "payment_test",
    "login_api",
    "search_test",
    "checkout_api"
]

result = filter(
    lambda name: name.endswith("_test"),
    test_names
)

print(list(result))

Output:

[
    'login_test',
    'payment_test',
    'search_test'
]
"""


# ============================================================
# 8. FILTERING AUTOMATION-STYLE DATA
# ============================================================

"""
Example test data:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

Keep only failed tests:

def is_failed(test):
    return test[1] == "FAIL"

failed_tests = list(filter(is_failed, test_results))

print(failed_tests)

Output:

[
    ['payment', 'FAIL'],
    ['checkout', 'FAIL']
]
"""


# ============================================================
# 9. BOOLEAN CONDITIONS WITH filter()
# ============================================================

"""
The filtering function normally returns True or False.

Example:

def is_passed(test):
    return test[1] == "PASS"

filter(is_passed, test_results)

True  -> keep the item
False -> remove the item
"""


# AND:

"""
Both conditions must be True.

lambda x: condition1 and condition2
"""


# OR:

"""
At least one condition must be True.

lambda x: condition1 or condition2
"""


# ============================================================
# 10. TRUTHINESS WITH filter()
# ============================================================

"""
filter() can also work with truthy/falsy values.

Example:

numbers = [0, 1, 2, 3, 4]

result = filter(lambda x: x, numbers)

print(list(result))

Output:

[1, 2, 3, 4]

Why?

0 is falsy.

1, 2, 3 and 4 are truthy.
"""


# filter(None, iterable) is another useful pattern:

"""
values = [0, 1, "", "hello", None, 5, False]

result = filter(None, values)

print(list(result))

Output:

[1, 'hello', 5]
"""


# ============================================================
# 11. filter() VS map()
# ============================================================

"""
map() -> TRANSFORMS items

filter() -> SELECTS items

Example:

numbers = [1, 2, 3, 4, 5]

map():

list(map(lambda x: x * 2, numbers))

Output:

[2, 4, 6, 8, 10]


filter():

list(filter(lambda x: x > 3, numbers))

Output:

[4, 5]
"""


# IMPORTANT:
"""
filter() keeps the ORIGINAL items.

It does not replace them with the value returned
by the condition.
"""


# ============================================================
# 12. COMBINING filter() AND map()
# ============================================================

"""
A common pattern is:

filter() -> select
map()    -> transform

Example:

test_names = [
    "login_test",
    "payment_test",
    "login_api",
    "search_test",
    "checkout_api"
]

result = list(
    map(
        lambda x: x.upper(),
        filter(
            lambda x: x.endswith("_test"),
            test_names
        )
    )
)

Output:

[
    'LOGIN_TEST',
    'PAYMENT_TEST',
    'SEARCH_TEST'
]
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. filter() selects items.

2. Basic syntax:

   filter(function, iterable)

3. filter() returns a filter object.

4. Use list(filter(...)) to create a list.

5. The function normally returns True or False.

6. True  -> keep the item.
7. False -> remove the item.

8. filter() does NOT transform the original values.

9. map() -> TRANSFORM
10. filter() -> SELECT

11. filter() is useful for automation test results.

12. filter() and map() can be combined:

    filter() -> select
    map()    -> transform
"""
