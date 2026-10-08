# ============================================
# Python Dictionary Mastery
# File: 19_dictionary.py
# ============================================


# ============================================
# 1. CREATING A DICTIONARY
# ============================================

user = {
    "name": "John",
    "age": 30
}

print(user)

# Empty dictionary
empty_dict = {}

# Another way to create an empty dictionary
another_empty_dict = dict()


# ============================================
# 2. KEYS AND VALUES
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

# Keys must be unique.
# Values can be duplicated.

# If the same key is repeated, the latest value replaces
# the previous value.

example = {
    "login": "PASS",
    "login": "FAIL"
}

print(example)
# {'login': 'FAIL'}


# ============================================
# 3. ACCESSING VALUES
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

print(test_results["login"])
# PASS

print(test_results["checkout"])
# FAIL

# If the key does not exist, [] raises KeyError.

# test_results["payment"]
# KeyError: 'payment'


# ============================================
# 4. ADDING / UPDATING VALUES USING []
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

# Existing key -> update value
test_results["login"] = "FAIL"

# Missing key -> create new key
test_results["payment"] = "NOT EXECUTED"

print(test_results)


# ============================================
# 5. get()
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

# Existing key
print(test_results.get("login"))
# PASS

# Missing key -> None
print(test_results.get("search"))
# None

# Missing key -> custom default
print(test_results.get("search", "NOT EXECUTED"))
# NOT EXECUTED


# [] vs get()
#
# test_results["search"]
# -> KeyError if missing
#
# test_results.get("search")
# -> None if missing
#
# test_results.get("search", "NOT EXECUTED")
# -> "NOT EXECUTED" if missing


# ============================================
# 6. MEMBERSHIP - CHECKING KEYS
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

print("login" in test_results)
# True

print("payment" in test_results)
# False

# 'in' checks dictionary KEYS by default.


# ============================================
# 7. MEMBERSHIP - CHECKING VALUES
# ============================================

print("PASS" in test_results.values())
# True

print("NOT EXECUTED" in test_results.values())
# False


# ============================================
# 8. DICTIONARY LOOP - KEYS
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

for test in test_results:
    print(test)

# Output:
# login
# checkout
# search

# Direct iteration over a dictionary gives KEYS.


# ============================================
# 9. .keys()
# ============================================

for test in test_results.keys():
    print(test)

# Explicitly accesses the dictionary keys.


# ============================================
# 10. .values()
# ============================================

for status in test_results.values():
    print(status)

# Output:
# PASS
# FAIL
# PASS


# ============================================
# 11. .items()
# ============================================

for test, status in test_results.items():
    print(test, status)

# Output:
# login PASS
# checkout FAIL
# search PASS

# .items() gives key-value pairs.


# ============================================
# 12. UPDATE MULTIPLE VALUES - update()
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

test_results.update({
    "login": "FAIL",
    "checkout": "PASS",
    "payment": "NOT EXECUTED"
})

print(test_results)

# Existing keys -> updated
# Missing keys -> created


# [] vs update()
#
# One key:
#
# test_results["login"] = "FAIL"
#
# Multiple keys:
#
# test_results.update({
#     "login": "FAIL",
#     "checkout": "PASS"
# })


# ============================================
# 13. REMOVING A KEY - del
# ============================================

test_result = {
    "status": "PASS",
    "browser": "Chrome"
}

del test_result["browser"]

print(test_result)

# del removes the specified key.
# It does not return the removed value.


# ============================================
# 14. pop()
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

removed = test_results.pop("checkout")

print(removed)
# FAIL

print(test_results)
# {'login': 'PASS', 'search': 'PASS'}

# pop() removes a specific key
# and returns its VALUE.


# pop() with a default value

removed = test_results.pop("payment", "NOT EXECUTED")

print(removed)
# NOT EXECUTED

# Prevents KeyError when the key is missing.


# ============================================
# 15. popitem()
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

removed = test_results.popitem()

print(removed)
# ('search', 'PASS')

print(test_results)
# {'login': 'PASS', 'checkout': 'FAIL'}

# popitem() removes the LAST INSERTED
# key-value pair.
#
# It returns:
# (key, value)
#
# which is a tuple.


# ============================================
# 16. clear()
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

test_results.clear()

print(test_results)
# {}


# ============================================
# 17. clear() vs REASSIGNMENT
# ============================================

test_results = {
    "login": "PASS"
}

backup = test_results

# clear() mutates the SAME dictionary
test_results.clear()

print(test_results)
# {}

print(backup)
# {}

# Both variables refer to the same dictionary.


# Reassignment

test_results = {
    "login": "PASS"
}

backup = test_results

test_results = {}

print(test_results)
# {}

print(backup)
# {'login': 'PASS'}

# test_results now refers to a NEW dictionary.
# backup still refers to the ORIGINAL dictionary.


# ============================================
# 18. NESTED DICTIONARIES
# ============================================

test_results = {
    "login": {
        "status": "PASS",
        "browser": "Chrome"
    },
    "checkout": {
        "status": "FAIL",
        "browser": "Chrome"
    },
    "search": {
        "status": "PASS",
        "browser": "Firefox"
    }
}


# ============================================
# 19. ACCESSING NESTED DICTIONARY VALUES
# ============================================

print(test_results["checkout"]["status"])
# FAIL

print(test_results["checkout"]["browser"])
# Chrome


# Mental model:
#
# test_results
#     ↓
# "checkout"
#     ↓
# inner dictionary
#     ↓
# "status"
#     ↓
# "FAIL"


# ============================================
# 20. LOOPING THROUGH NESTED DICTIONARY
# ============================================

for test, details in test_results.items():
    print(test, details["status"], details["browser"])

# Output:
# login PASS Chrome
# checkout FAIL Chrome
# search PASS Firefox


# ============================================
# 21. NESTED DICTIONARY + CONDITION
# ============================================

for test, details in test_results.items():
    if details["status"] == "FAIL":
        print(test, details["status"], details["browser"])

# Output:
# checkout FAIL Chrome


# ============================================
# 22. LOOP THROUGH INNER DICTIONARY
# ============================================

for test, details in test_results.items():

    for key, value in details.items():
        print(key, value)

# This loops through each inner dictionary.


# ============================================
# 23. DICTIONARY COMPREHENSION
# ============================================

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number * number
    for number in numbers
}

print(squares)

# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


# General structure:
#
# {key: value for item in iterable}


# ============================================
# 24. DICTIONARY COMPREHENSION - AUTOMATION
# ============================================

tests = ["login", "checkout", "search"]

test_status = {
    test: "NOT RUN"
    for test in tests
}

print(test_status)

# {
#     "login": "NOT RUN",
#     "checkout": "NOT RUN",
#     "search": "NOT RUN"
# }


# ============================================
# 25. DICTIONARY COMPREHENSION WITH len()
# ============================================

test_lengths = {
    test: len(test)
    for test in tests
}

print(test_lengths)

# {
#     "login": 5,
#     "checkout": 8,
#     "search": 6
# }


# ============================================
# 26. CONDITIONAL DICTIONARY COMPREHENSION
# ============================================

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS",
    "payment": "FAIL"
}

failed_tests = {
    test: status
    for test, status in test_results.items()
    if status == "FAIL"
}

print(failed_tests)

# {
#     "checkout": "FAIL",
#     "payment": "FAIL"
# }


# ============================================
# 27. NESTED DICTIONARY COMPREHENSION
# ============================================

test_results = {
    "login": {
        "status": "PASS",
        "browser": "Chrome"
    },
    "checkout": {
        "status": "FAIL",
        "browser": "Chrome"
    },
    "search": {
        "status": "PASS",
        "browser": "Firefox"
    }
}

failed_browsers = {
    test: details["browser"]
    for test, details in test_results.items()
    if details["status"] == "FAIL"
}

print(failed_browsers)

# {
#     "checkout": "Chrome"
# }


# ============================================
# 28. DICTIONARY vs SET
# ============================================

# Set:
#
# Stores unique values.
#
# tests = {
#     "login",
#     "checkout",
#     "search"
# }


# Dictionary:
#
# Stores key-value relationships.
#
# test_results = {
#     "login": "PASS",
#     "checkout": "FAIL"
# }


# ============================================
# 29. AUTOMATION USE CASES
# ============================================

# Dictionaries are commonly used for:
#
# 1. Test results
# 2. Configuration
# 3. API/JSON responses
# 4. Test metadata
# 5. Browser/device information
# 6. Environment configuration
# 7. Mapping test names to statuses
# 8. Mapping API names to response details


# Example:

test_config = {
    "browser": "Chrome",
    "environment": "QA",
    "timeout": 30
}

print(test_config["browser"])


# ============================================
# 30. QUICK REFERENCE
# ============================================

# Create:
# {}

# Access:
# dictionary["key"]

# Safe access:
# dictionary.get("key")

# Safe access with default:
# dictionary.get("key", default)

# Add/update one:
# dictionary["key"] = value

# Add/update multiple:
# dictionary.update({...})

# Check key:
# "key" in dictionary

# Check value:
# "value" in dictionary.values()

# Keys:
# dictionary.keys()

# Values:
# dictionary.values()

# Key + value:
# dictionary.items()

# Remove specific key:
# del dictionary["key"]

# Remove and return value:
# dictionary.pop("key")

# Remove last inserted pair:
# dictionary.popitem()

# Empty dictionary:
# dictionary.clear()

# Dictionary comprehension:
# {key: value for item in iterable}


# ============================================
# END
# ============================================
# Dictionary mastery complete.
# ============================================
