# ============================================
# SORTED() — EXERCISES WITH SOLUTIONS
# ============================================

# Exercise 1: Sort numbers in ascending order.
numbers = [40, 10, 30, 20, 50]
result = sorted(numbers)
print("1:", result)
# [10, 20, 30, 40, 50]


# Exercise 2: sorted() returns a new list.
numbers = [40, 10, 30, 20]
result = sorted(numbers)
print("2 - original:", numbers)
print("2 - sorted:  ", result)
# original: [40, 10, 30, 20]
# sorted:   [10, 20, 30, 40]


# Exercise 3: Sort in descending order.
numbers = [40, 10, 30, 20]
result = sorted(numbers, reverse=True)
print("3:", result)
# [40, 30, 20, 10]


# Exercise 4: Sort names alphabetically.
names = ["Charlie", "Alice", "Bob", "David"]
result = sorted(names)
print("4:", result)
# ['Alice', 'Bob', 'Charlie', 'David']


# Exercise 5: Sort names by length using key=len.
names = ["Alexander", "Bob", "John", "David"]
result = sorted(names, key=len)
print("5:", result)
# ['Bob', 'John', 'David', 'Alexander']


# Exercise 6: Sort names by length using lambda.
names = ["Alexander", "Bob", "John", "David"]
result = sorted(names, key=lambda name: len(name))
print("6:", result)
# ['Bob', 'John', 'David', 'Alexander']


# Exercise 7: Sort tests by execution time (second value).
tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300],
]
result = sorted(tests, key=lambda test: test[1])
print("7:", result)
# [['search', 80], ['login', 120], ['checkout', 300], ['payment', 450]]


# Exercise 8: Sort tests from slowest to fastest.
tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300],
]
result = sorted(tests, key=lambda test: test[1], reverse=True)
print("8:", result)
# [['payment', 450], ['checkout', 300], ['login', 120], ['search', 80]]


# Exercise 9: Use a normal function as the sorting key.
def get_time(test):
    return test[1]


tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
]
result = sorted(tests, key=get_time)
print("9:", result)
# [['search', 80], ['login', 120], ['payment', 450]]


# Exercise 10: Sort names by length, longest first.
names = ["Alexander", "Bob", "John", "David"]
result = sorted(names, key=len, reverse=True)
print("10:", result)
# ['Alexander', 'Charlie' ...] — see actual names above:
# ['Alexander', 'Bob', 'John', 'David'] sorted by length:
# ['Alexander', 'David', 'John', 'Bob']


# Exercise 11: Sort tests by time, largest first.
tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300],
]
result = sorted(tests, key=lambda test: test[1], reverse=True)
print("11:", result)
# [['payment', 450], ['checkout', 300], ['login', 120], ['search', 80]]


# Exercise 12: Use a normal function and reverse=True.
def get_time(test):
    return test[1]


tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
]
result = sorted(tests, key=get_time, reverse=True)
print("12:", result)
# [['payment', 450], ['login', 120], ['search', 80]]


# Exercise 13: Sort tests by execution time.
tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300],
]
result = sorted(tests, key=lambda test: test[2])
print("13:", result)
# [['search', 'PASS', 80], ['login', 'PASS', 120],
#  ['checkout', 'FAIL', 300], ['payment', 'FAIL', 450]]


# Exercise 14: Sort by status alphabetically, then by time.
tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300],
]
result = sorted(tests, key=lambda test: (test[1], test[2]))
print("14:", result)
# FAIL sorts before PASS alphabetically:
# [['checkout', 'FAIL', 300], ['payment', 'FAIL', 450],
#  ['search', 'PASS', 80], ['login', 'PASS', 120]]


# Exercise 15: Put PASS before FAIL, then sort each group by time.
tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "FAIL", 300],
]
status_order = {"PASS": 0, "FAIL": 1}
result = sorted(
    tests,
    key=lambda test: (status_order[test[1]], test[2]),
)
print("15:", result)
# [['search', 'PASS', 80], ['login', 'PASS', 120],
#  ['checkout', 'FAIL', 300], ['payment', 'FAIL', 450]]


# Final challenge: Keep PASS tests, sort by time, then uppercase names.
tests = [
    ["login", "PASS", 120],
    ["payment", "FAIL", 450],
    ["search", "PASS", 80],
    ["checkout", "PASS", 300],
    ["profile", "FAIL", 200],
]

passed_tests = filter(lambda test: test[1] == "PASS", tests)
sorted_tests = sorted(passed_tests, key=lambda test: test[2])
result = list(map(lambda test: test[0].upper(), sorted_tests))

print("Final challenge:", result)
# ['SEARCH', 'LOGIN', 'CHECKOUT']
