# exercises/filter.py
"""
Python filter() - Exercises and Solutions

Topics practiced:
- filter() with lambda
- filter() with normal functions
- Boolean conditions
- and / or
- Truthiness
- String filtering
- Automation-style test data
- Combining filter() and map()
"""


# ============================================================
# QUESTION 1 - Basic filter()
# ============================================================

"""
Given:

numbers = [5, 10, 15, 20, 25]

Keep only numbers greater than 15.

Expected:
[20, 25]
"""

numbers = [5, 10, 15, 20, 25]

answer_1 = list(filter(lambda x: x > 15, numbers))

print(answer_1)
# [20, 25]


# ============================================================
# QUESTION 2 - Filter strings
# ============================================================

"""
Given:

names = ["Alice", "Bob", "Andrew", "Charlie"]

Keep only names that start with "A".

Expected:
["Alice", "Andrew"]
"""

names = ["Alice", "Bob", "Andrew", "Charlie"]

answer_2 = list(filter(lambda name: name.startswith("A"), names))

print(answer_2)
# ['Alice', 'Andrew']


# ============================================================
# QUESTION 3 - Normal function
# ============================================================

"""
Keep only positive numbers.

Given:

numbers = [-5, 10, -2, 0, 8, -1]

Expected:
[10, 8]
"""


def is_positive(data):
    return data > 0


numbers = [-5, 10, -2, 0, 8, -1]

answer_3 = list(filter(is_positive, numbers))

print(answer_3)
# [10, 8]


# ============================================================
# QUESTION 4 - String filtering with a normal function
# ============================================================

"""
Keep only names that start with "A".

Given:

names = ["Alex", "Bob", "Amanda", "John", "Andrew"]

Expected:
['Alex', 'Amanda', 'Andrew']
"""


def starts_with(data):
    return data.startswith("A")


names = ["Alex", "Bob", "Amanda", "John", "Andrew"]

answer_4 = list(filter(starts_with, names))

print(answer_4)
# ['Alex', 'Amanda', 'Andrew']


# ============================================================
# QUESTION 5 - Lambda condition
# ============================================================

"""
Keep only numbers greater than or equal to 25.

Given:

numbers = [10, 15, 20, 25, 30, 35]

Expected:
[25, 30, 35]
"""

numbers = [10, 15, 20, 25, 30, 35]

answer_5 = list(filter(lambda data: data >= 25, numbers))

print(answer_5)
# [25, 30, 35]


# ============================================================
# QUESTION 6 - Multiple conditions with AND
# ============================================================

"""
Keep numbers that are:

1. Greater than 20
2. Even

Given:

numbers = [5, 12, 18, 21, 30, 35, 40]

Expected:
[30, 40]
"""

numbers = [5, 12, 18, 21, 30, 35, 40]

answer_6 = list(
    filter(lambda x: x % 2 == 0 and x > 20, numbers)
)

print(answer_6)
# [30, 40]


# ============================================================
# QUESTION 7 - Automation: failed tests
# ============================================================

"""
Keep only failed tests.

Given:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

Expected:

[
    ["payment", "FAIL"],
    ["checkout", "FAIL"]
]
"""


def is_failed(tests):
    return tests[1] == "FAIL"


test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

answer_7 = list(filter(is_failed, test_results))

print(answer_7)
# [['payment', 'FAIL'], ['checkout', 'FAIL']]


# ============================================================
# QUESTION 8 - Automation: passed tests
# ============================================================

"""
Keep only tests whose status is PASS.

Expected:

[
    ["login", "PASS"],
    ["search", "PASS"]
]
"""

answer_8 = list(
    filter(lambda tests: tests[1] == "PASS", test_results)
)

print(answer_8)
# [['login', 'PASS'], ['search', 'PASS']]


# ============================================================
# QUESTION 9 - filter() and truthiness
# ============================================================

"""
Given:

numbers = [1, 2, 3, 4, 5]

What happens when we use:

filter(lambda x: x * 2, numbers)

Important:
filter() checks whether the returned value is truthy.
It does NOT replace the original item.
"""

numbers = [1, 2, 3, 4, 5]

answer_9 = list(filter(lambda x: x * 2, numbers))

print(answer_9)
# [1, 2, 3, 4, 5]


# ============================================================
# QUESTION 10 - Truthy and falsy values
# ============================================================

"""
Given:

numbers = [0, 1, 2, 3, 4]

Keep only truthy values.

Expected:
[1, 2, 3, 4]
"""

numbers = [0, 1, 2, 3, 4]

answer_10 = list(filter(lambda x: x, numbers))

print(answer_10)
# [1, 2, 3, 4]


# ============================================================
# QUESTION 11 - Automation: PASS + duration
# ============================================================

"""
Each test contains:

[test_name, status, duration_ms]

Keep only tests that:

1. Passed
2. Took 200 ms or less

Expected:

[
    ["login", "PASS", 120],
    ["search", "PASS", 80]
]
"""

test_results = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 350],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 500],
    ["profile", "PASS", 200]
]


def is_passed_and_fast(data):
    return data[1] == "PASS" and data[2] <= 200


answer_11 = list(filter(is_passed_and_fast, test_results))

print(answer_11)
# [['login', 'PASS', 120], ['search', 'PASS', 80]]


# ============================================================
# QUESTION 12 - OR condition
# ============================================================

"""
Keep tests that satisfy either condition:

1. Status is FAIL
OR
2. Duration is greater than 300 ms

Given:

test_results = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 350],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 500],
    ["profile", "PASS", 200],
    ["settings", "PASS", 450]
]

Expected:

[
    ["payment", "FAIL", 350],
    ["checkout", "FAIL", 500],
    ["settings", "PASS", 450]
]
"""

test_results = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 350],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 500],
    ["profile", "PASS", 200],
    ["settings", "PASS", 450]
]

answer_12 = list(
    filter(
        lambda x: x[1] == "FAIL" or x[2] > 300,
        test_results
    )
)

print(answer_12)
# [
#     ['payment', 'FAIL', 350],
#     ['checkout', 'FAIL', 500],
#     ['settings', 'PASS', 450]
# ]


# ============================================================
# QUESTION 13 - Filter strings
# ============================================================

"""
Keep only test names that end with "_test".

Given:

test_names = [
    "login_test",
    "payment_test",
    "login_api",
    "search_test",
    "checkout_api"
]

Expected:

[
    "login_test",
    "payment_test",
    "search_test"
]
"""

test_names = [
    "login_test",
    "payment_test",
    "login_api",
    "search_test",
    "checkout_api"
]

answer_13 = list(
    filter(lambda x: x.endswith("_test"), test_names)
)

print(answer_13)
# ['login_test', 'payment_test', 'search_test']


# ============================================================
# QUESTION 14 - filter() + map()
# ============================================================

"""
Step 1:
Keep only names ending with "_test".

Step 2:
Convert those names to uppercase.

Expected:

[
    "LOGIN_TEST",
    "PAYMENT_TEST",
    "SEARCH_TEST"
]
"""

test_names = [
    "login_test",
    "payment_test",
    "login_api",
    "search_test",
    "checkout_api"
]

answer_14 = list(
    map(
        lambda x: x.upper(),
        filter(lambda x: x.endswith("_test"), test_names)
    )
)

print(answer_14)
# ['LOGIN_TEST', 'PAYMENT_TEST', 'SEARCH_TEST']


# ============================================================
# KEY LEARNINGS
# ============================================================

"""
filter()
--------

filter(function, iterable)

filter() SELECTS items.

True  -> keep
False -> remove


map()
-----

map(function, iterable)

map() TRANSFORMS items.


Important distinction:

filter() -> SELECT
map()    -> TRANSFORM


Multiple conditions:

and -> all conditions must be True
or  -> at least one condition must be True


Truthiness:

0       -> False
""      -> False
None    -> False
False   -> False

Most non-zero numbers and non-empty strings are True.


Combining filter() and map():

filter() -> select the data
map()    -> transform the selected data
"""
