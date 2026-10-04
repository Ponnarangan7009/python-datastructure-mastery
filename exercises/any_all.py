# ==========================================
# any() and all() - Exercises
# ==========================================


# ------------------------------------------
# Q1
# ------------------------------------------

numbers = [0, 0, 5, 0]

print(any(numbers))
print(all(numbers))

# Expected:
# True
# False


# ------------------------------------------
# Q2
# ------------------------------------------

numbers = [1, 2, 3, 4]

print(any(numbers))
print(all(numbers))

# Expected:
# True
# True


# ------------------------------------------
# Q3
# ------------------------------------------

results = [True, True, False, True]

print(any(results))
print(all(results))

# Expected:
# True
# False


# ------------------------------------------
# Q4
# ------------------------------------------

results = ["PASS", "PASS", "PASS"]

print(any(result == "FAIL" for result in results))
print(all(result == "PASS" for result in results))

# Expected:
# False
# True


# ------------------------------------------
# Q5
# ------------------------------------------

results = ["PASS", "FAIL", "PASS"]

print(any(result == "FAIL" for result in results))
print(all(result == "PASS" for result in results))

# Expected:
# True
# False


# ------------------------------------------
# Q6 - Automation Testing
# ------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "PASS"],
    ["search", "PASS"],
    ["logout", "PASS"]
]

print(all(test[1] == "PASS" for test in test_results))

# Expected:
# True


# ------------------------------------------
# Q7 - Automation Testing
# ------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["logout", "PASS"]
]

print(any(test[1] == "FAIL" for test in test_results))

# Expected:
# True


# ------------------------------------------
# Q8 - Challenge
# ------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["logout", "FAIL"]
]

print(any(test[1] == "FAIL" for test in test_results))
print(all(test[1] == "PASS" for test in test_results))

# Expected:
# True
# False
