# Dictionary Exercises

# 1. Basic Access

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

print(test_results["checkout"])
# Answer: FAIL


# 2. get()

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

print(test_results.get("search"))
# Answer: None


# 3. get() with Default

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

print(test_results.get("search", "NOT EXECUTED"))
# Answer: NOT EXECUTED


# 4. Check Key Membership

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

print("payment" in test_results)
# Answer: False


# 5. Check Value Membership

print("PASS" in test_results.values())
# Answer: True


# 6. Direct Dictionary Loop

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

for test in test_results:
    print(test)

# Answer:
# login
# checkout
# search


# 7. items()

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

for test, status in test_results.items():
    print(test, status)

# Answer:
# login PASS
# checkout FAIL


# 8. Update / Create Using []

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

test_results["login"] = "FAIL"
test_results["search"] = "PASS"

print(test_results)

# Answer:
# {'login': 'FAIL', 'checkout': 'FAIL', 'search': 'PASS'}


# 9. update()

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

test_results.update({
    "login": "FAIL",
    "search": "PASS",
    "payment": "NOT EXECUTED"
})

print(test_results)

# Answer:
# {
#     'login': 'FAIL',
#     'checkout': 'FAIL',
#     'search': 'PASS',
#     'payment': 'NOT EXECUTED'
# }


# 10. pop()

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

removed = test_results.pop("checkout")

print(removed)
print(test_results)

# Answer:
# FAIL
# {'login': 'PASS', 'search': 'PASS'}


# 11. popitem()

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS"
}

removed = test_results.popitem()

print(removed)
print(test_results)

# Answer:
# ('search', 'PASS')
# {'login': 'PASS', 'checkout': 'FAIL'}


# 12. clear()

test_results = {
    "login": "PASS",
    "checkout": "FAIL"
}

test_results.clear()

print(test_results)

# Answer:
# {}


# 13. clear() and References

test_results = {
    "login": "PASS"
}

backup = test_results

test_results.clear()

print(test_results)
print(backup)

# Answer:
# {}
# {}


# 14. Reassignment

test_results = {
    "login": "PASS"
}

backup = test_results

test_results = {}

print(test_results)
print(backup)

# Answer:
# {}
# {'login': 'PASS'}


# 15. update()

test = {
    "status": "PASS",
    "browser": "Chrome"
}

test.update({
    "status": "FAIL",
    "duration": 2.5
})

print(test)

# Answer:
# {'status': 'FAIL', 'browser': 'Chrome', 'duration': 2.5}


# 16. Dictionary Comprehension

tests = ["login", "checkout", "search"]

result = {
    test: len(test)
    for test in tests
}

print(result)

# Answer:
# {'login': 5, 'checkout': 8, 'search': 6}


# 17. Conditional Dictionary Comprehension

test_results = {
    "login": "PASS",
    "checkout": "FAIL",
    "search": "PASS",
    "payment": "FAIL"
}

result = {
    key: value
    for key, value in test_results.items()
    if value == "FAIL"
}

print(result)

# Answer:
# {'checkout': 'FAIL', 'payment': 'FAIL'}


# 18. Nested Dictionary

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

print(test_results["checkout"]["status"])

# Answer:
# FAIL


# 19. Nested Dictionary Loop

for test, details in test_results.items():
    if details["status"] == "FAIL":
        print(test, details["status"], details["browser"])

# Answer:
# checkout FAIL Chrome


# 20. Nested Dictionary Comprehension

result = {
    key: value["browser"]
    for key, value in test_results.items()
    if value["status"] == "FAIL"
}

print(result)

# Answer:
# {'checkout': 'Chrome'}
