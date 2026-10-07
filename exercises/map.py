# exercises/map.py
"""
map() - Practice Exercises

Try to solve each question before looking at the answers.
"""


# ============================================================
# QUESTION 1 - Basic map()
# ============================================================

"""
Given:

numbers = [1, 2, 3, 4]

Use map() to multiply every number by 2.

Expected output:

[2, 4, 6, 8]
"""


# ============================================================
# QUESTION 2 - map() with a normal function
# ============================================================

"""
Create a function called square() that returns the square
of a number.

Use map() with:

numbers = [2, 3, 4, 5]

Expected output:

[4, 9, 16, 25]
"""


# ============================================================
# QUESTION 3 - map() with lambda
# ============================================================

"""
Given:

numbers = [10, 20, 30, 40]

Use map() and lambda to add 5 to every number.

Expected output:

[15, 25, 35, 45]
"""


# ============================================================
# QUESTION 4 - Strings
# ============================================================

"""
Given:

names = ["alice", "bob", "charlie"]

Use map() to convert every name to uppercase.

Expected output:

['ALICE', 'BOB', 'CHARLIE']
"""


# ============================================================
# QUESTION 5 - String transformation
# ============================================================

"""
Given:

names = ["john doe", "alice smith", "bob brown"]

Use map() to convert every name into title case.

Expected output:

['John Doe', 'Alice Smith', 'Bob Brown']
"""


# ============================================================
# QUESTION 6 - Multiple iterables
# ============================================================

"""
Given:

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

Use map() to add corresponding values.

Expected output:

[11, 22, 33]
"""


# ============================================================
# QUESTION 7 - Different length iterables
# ============================================================

"""
Given:

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]

Use map() to add corresponding values.

Before running the code, predict the output.

Expected concept:

map() stops when the shortest iterable is exhausted.
"""


# ============================================================
# QUESTION 8 - Automation data
# ============================================================

"""
Given:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

Create a function that returns only the test name.

Use map() to produce:

['login', 'payment', 'search']
"""


# ============================================================
# QUESTION 9 - Automation data
# ============================================================

"""
Using the same test_results:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

Use map() to extract only the test statuses.

Expected output:

['PASS', 'FAIL', 'PASS']
"""


# ============================================================
# QUESTION 10 - Automation data + lambda
# ============================================================

"""
Given:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

Use map() and lambda to extract the test names.

Expected output:

['login', 'payment', 'search']
"""


# ============================================================
# QUESTION 11 - print() vs return
# ============================================================

"""
What will this code produce?

def get_name(data):
    print(data[0])

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"]
]

output = list(map(get_name, test_results))

print(output)

Predict:

1. What will be printed by get_name()?
2. What will the value of output be?
"""


# ============================================================
# QUESTION 12 - map() with int
# ============================================================

"""
Given:

numbers = ["10", "20", "30", "40"]

Use map() to convert every string into an integer.

Expected output:

[10, 20, 30, 40]
"""


# ============================================================
# QUESTION 13 - map() with multiple iterables
# ============================================================

"""
Given:

first_names = ["John", "Alice", "Bob"]
last_names = ["Smith", "Brown", "Wilson"]

Use map() to create full names.

Expected output:

['John Smith', 'Alice Brown', 'Bob Wilson']
"""


# ============================================================
# QUESTION 14 - Automation example
# ============================================================

"""
Given:

test_names = ["login", "payment", "search"]

Use map() to add the word "Test" after every name.

Expected output:

['login Test', 'payment Test', 'search Test']

Hint:

Use lambda.
"""


# ============================================================
# QUESTION 15 - Challenge
# ============================================================

"""
Given:

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

Use map() to create a list containing:

['login: PASS',
 'payment: FAIL',
 'search: PASS',
 'checkout: FAIL']

Hint:

Use a normal function OR lambda.
"""


# ============================================================
# ANSWERS
# ============================================================

# Q1
numbers = [1, 2, 3, 4]

answer_1 = list(map(lambda x: x * 2, numbers))

print(answer_1)
# [2, 4, 6, 8]


# Q2
def square(number):
    return number ** 2


numbers = [2, 3, 4, 5]

answer_2 = list(map(square, numbers))

print(answer_2)
# [4, 9, 16, 25]


# Q3
numbers = [10, 20, 30, 40]

answer_3 = list(map(lambda x: x + 5, numbers))

print(answer_3)
# [15, 25, 35, 45]


# Q4
names = ["alice", "bob", "charlie"]

answer_4 = list(map(str.upper, names))

print(answer_4)
# ['ALICE', 'BOB', 'CHARLIE']


# Q5
names = ["john doe", "alice smith", "bob brown"]

answer_5 = list(map(str.title, names))

print(answer_5)
# ['John Doe', 'Alice Smith', 'Bob Brown']


# Q6
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

answer_6 = list(map(lambda x, y: x + y, numbers1, numbers2))

print(answer_6)
# [11, 22, 33]


# Q7
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]

answer_7 = list(map(lambda x, y: x + y, numbers1, numbers2))

print(answer_7)
# [11, 22]


# Q8
test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]


def get_test_name(data):
    return data[0]


answer_8 = list(map(get_test_name, test_results))

print(answer_8)
# ['login', 'payment', 'search']


# Q9
def get_status(data):
    return data[1]


answer_9 = list(map(get_status, test_results))

print(answer_9)
# ['PASS', 'FAIL', 'PASS']


# Q10
answer_10 = list(map(lambda data: data[0], test_results))

print(answer_10)
# ['login', 'payment', 'search']


# Q11
def get_name(data):
    print(data[0])


test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"]
]

output = list(map(get_name, test_results))

print(output)

# Output:
#
# login
# payment
# [None, None]
#
# Because get_name() uses print()
# instead of return.


# Q12
numbers = ["10", "20", "30", "40"]

answer_12 = list(map(int, numbers))

print(answer_12)
# [10, 20, 30, 40]


# Q13
first_names = ["John", "Alice", "Bob"]
last_names = ["Smith", "Brown", "Wilson"]

answer_13 = list(
    map(lambda first, last: f"{first} {last}", first_names, last_names)
)

print(answer_13)
# ['John Smith', 'Alice Brown', 'Bob Wilson']


# Q14
test_names = ["login", "payment", "search"]

answer_14 = list(map(lambda name: f"{name} Test", test_names))

print(answer_14)
# ['login Test', 'payment Test', 'search Test']


# Q15
test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]


def format_result(data):
    return f"{data[0]}: {data[1]}"


answer_15 = list(map(format_result, test_results))

print(answer_15)

# [
#     'login: PASS',
#     'payment: FAIL',
#     'search: PASS',
#     'checkout: FAIL'
# ]
