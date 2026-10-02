# enumerate() exercises
# Given:
languages = ["Python", "Java", "C++", "Go"]
# Use enumerate() to produce:
# 0 Python
# 1 Java
# 2 C++
# 3 Go
for index, language in enumerate(languages):
    print(f"{index} {language}")

# Start from 1
# Using the same list, produce:
# 1 Python
# 2 Java
# 3 C++
# 4 Go
for index, language in enumerate(languages, start=1):
    print(f"{index} {language}")


# Find an index
# Given:
languages = ["Python", "Java", "C++", "Go"]
# Use enumerate() to print:
# Python is at index 0
# Java is at index 1
# Don't use .index().
for index, language in enumerate(languages):
    print(f"{language} is at index {index}")

# Automation example
# Given:
test_results = ["PASS", "FAIL", "PASS", "FAIL"]
# Test 1: PASS
# Test 2: FAIL
# Test 3: PASS
# Test 4: FAIL
# Use enumerate() with start=1.
for index, results in enumerate(test_results, start=1):
    print(f"Test {index}: {results}")


# Given:
# test_results = ["PASS", "FAIL", "PASS", "FAIL"]
# Print only the failed tests, including their test number:
# Test 2: FAIL
# Test 4: FAIL
for index, results in enumerate(test_results, start=1):
    if results == "FAIL": 
        print(f"Test {index}: {results}")

