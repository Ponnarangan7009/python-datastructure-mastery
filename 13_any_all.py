# ==========================================
# any() and all()
# ==========================================


# ------------------------------------------
# 1. any()
# ------------------------------------------

numbers = [0, 0, 5, 0]

print(any(numbers))

# Output:
# True

# any() returns True when at least ONE
# item is truthy.


# ------------------------------------------
# 2. all()
# ------------------------------------------

numbers = [1, 2, 3, 4]

print(all(numbers))

# Output:
# True

# all() returns True when EVERY item
# is truthy.


# ------------------------------------------
# 3. any() vs all()
# ------------------------------------------

results = [True, True, False, True]

print(any(results))
print(all(results))

# Output:
# True
# False

# any() → at least one True
# all() → every value must be True


# ------------------------------------------
# 4. Truthy and Falsy Values
# ------------------------------------------

numbers = [0, 0, 10, 0]

print(any(numbers))
print(all(numbers))

# Output:
# True
# False

# 0 is falsy.
# Non-zero numbers are truthy.


# ------------------------------------------
# 5. any() with a Condition
# ------------------------------------------

numbers = [1, 3, 5, 8]

print(any(number % 2 == 0 for number in numbers))

# Output:
# True

# There is at least one even number.


# ------------------------------------------
# 6. all() with a Condition
# ------------------------------------------

numbers = [2, 4, 6, 8]

print(all(number % 2 == 0 for number in numbers))

# Output:
# True

# Every number is even.


# ------------------------------------------
# 7. any() with Strings
# ------------------------------------------

results = ["PASS", "FAIL", "PASS"]

print(any(result == "FAIL" for result in results))

# Output:
# True

# At least one result is FAIL.


# ------------------------------------------
# 8. all() with Strings
# ------------------------------------------

results = ["PASS", "PASS", "PASS"]

print(all(result == "PASS" for result in results))

# Output:
# True

# Every result is PASS.


# ------------------------------------------
# 9. Automation Testing Example
# ------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"]
]

print(any(test[1] == "FAIL" for test in test_results))

# Output:
# True

# At least one test failed.


print(all(test[1] == "PASS" for test in test_results))

# Output:
# False

# Not every test passed.


# ------------------------------------------
# 10. Common Automation Patterns
# ------------------------------------------

# Did any test fail?

any(test[1] == "FAIL" for test in test_results)


# Did all tests pass?

all(test[1] == "PASS" for test in test_results)


# ------------------------------------------
# 11. Mental Model
# ------------------------------------------

# any()
#
# "Is there AT LEAST ONE?"
#
# any([False, False, True])
# → True


# all()
#
# "Is EVERY ONE true?"
#
# all([True, True, True])
# → True
#
# all([True, False, True])
# → False


# ------------------------------------------
# 12. Important Difference
# ------------------------------------------

results = ["FAIL", "FAIL", "FAIL"]

print(any(results))

# Output:
# True

# Why?
# Non-empty strings are truthy.


print(any(result == "PASS" for result in results))

# Output:
# False

# This specifically checks whether
# any result is PASS.
