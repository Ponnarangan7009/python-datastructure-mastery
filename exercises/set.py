# ============================================================
# SET — EXERCISES
# ============================================================


# ============================================================
# Q1. Create a Set
# ============================================================
numbers = {10, 20, 30, 40}

print(numbers)


# ============================================================
# Q2. Remove Duplicates
# ============================================================
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# ============================================================
# Q3. Create an Empty Set
# ============================================================
empty_set = set()

print(empty_set)


# ============================================================
# Q4. Add an Element
# ============================================================
tests = {"login", "checkout", "search"}

tests.add("payment")

print(tests)


# ============================================================
# Q5. Remove an Element
# ============================================================
tests = {"login", "checkout", "search"}

tests.remove("checkout")

print(tests)


# ============================================================
# Q6. discard()
# ============================================================
tests = {"login", "checkout", "search"}

tests.discard("payment")

print(tests)


# ============================================================
# Q7. Membership
# ============================================================
tests = {"login", "checkout", "search"}

result = "login" in tests

print(result)


# ============================================================
# Q8. Length
# ============================================================
tests = {"login", "checkout", "search", "login"}

count = len(tests)

print(count)


# ============================================================
# Q9. Union
# ============================================================
android_tests = {"login", "checkout", "search"}
google_tv_tests = {"login", "checkout", "settings"}

all_tests = android_tests | google_tv_tests

print(all_tests)


# ============================================================
# Q10. Intersection
# ============================================================
android_tests = {"login", "checkout", "search"}
google_tv_tests = {"login", "checkout", "settings"}

common_tests = android_tests & google_tv_tests

print(common_tests)


# ============================================================
# Q11. Android-Only Tests
# ============================================================
android_tests = {"login", "checkout", "search"}
google_tv_tests = {"login", "checkout", "settings"}

android_only = android_tests - google_tv_tests

print(android_only)


# ============================================================
# Q12. Google TV-Only Tests
# ============================================================
android_tests = {"login", "checkout", "search"}
google_tv_tests = {"login", "checkout", "settings"}

google_tv_only = google_tv_tests - android_tests

print(google_tv_only)


# ============================================================
# Q13. Symmetric Difference
# ============================================================
android_tests = {"login", "checkout", "search"}
google_tv_tests = {"login", "checkout", "settings"}

different_tests = android_tests ^ google_tv_tests

print(different_tests)


# ============================================================
# Q14. Subset
# ============================================================
smoke_tests = {"login", "checkout"}
all_tests = {"login", "checkout", "search", "payment"}

result = smoke_tests.issubset(all_tests)

print(result)


# ============================================================
# Q15. Superset
# ============================================================
smoke_tests = {"login", "checkout"}
all_tests = {"login", "checkout", "search", "payment"}

result = all_tests.issuperset(smoke_tests)

print(result)


# ============================================================
# Q16. Disjoint
# ============================================================
set1 = {"login", "checkout"}
set2 = {"payment", "search"}

result = set1.isdisjoint(set2)

print(result)


# ============================================================
# Q17. Missing Tests
# ============================================================
expected_tests = {
    "login",
    "checkout",
    "search",
    "payment"
}

executed_tests = {
    "login",
    "search"
}

missing_tests = expected_tests - executed_tests

print("Missing tests:", missing_tests)


# ============================================================
# Q18. Common Platform Tests
# ============================================================
android_tests = {
    "login",
    "checkout",
    "search"
}

google_tv_tests = {
    "login",
    "checkout",
    "settings"
}

common_tests = android_tests & google_tv_tests

print("Common tests:", common_tests)


# ============================================================
# Q19. Remove Duplicate Test Names
# ============================================================
test_names = [
    "test_login",
    "test_checkout",
    "test_login",
    "test_search",
    "test_checkout"
]

unique_tests = set(test_names)

print("Unique tests:", unique_tests)


# ============================================================
# Q20. Platform-Specific Tests
# ============================================================
android_tests = {
    "login",
    "checkout",
    "search"
}

google_tv_tests = {
    "login",
    "checkout",
    "settings"
}

android_only = android_tests - google_tv_tests
google_tv_only = google_tv_tests - android_tests

print("Android only:", android_only)
print("Google TV only:", google_tv_only)


# ============================================================
# Q21. pop()
# ============================================================
tests = {"login", "checkout", "search"}

removed_test = tests.pop()

print("Removed:", removed_test)
print("Remaining:", tests)


# ============================================================
# Q22. clear()
# ============================================================
tests = {"login", "checkout", "search"}

tests.clear()

print(tests)


# ============================================================
# Q23. List -> Set
# ============================================================
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# ============================================================
# Q24. Set -> List
# ============================================================
numbers = {10, 20, 30, 40}

numbers_list = list(numbers)

print(numbers_list)


# ============================================================
# Q25. Automation Scenario
# ============================================================
expected_tests = {
    "login",
    "checkout",
    "search",
    "payment",
    "profile"
}

executed_tests = {
    "login",
    "checkout",
    "search",
    "profile"
}

passed_tests = {
    "login",
    "search",
    "profile"
}

missing_tests = expected_tests - executed_tests
failed_tests = executed_tests - passed_tests

print("Missing tests:", missing_tests)
print("Failed tests:", failed_tests)


# ============================================================
# SET OPERATIONS — QUICK REFERENCE
# ============================================================

# Union
# A | B

# Intersection
# A & B

# Difference
# A - B

# Symmetric Difference
# A ^ B

# Subset
# A <= B
# A.issubset(B)

# Superset
# A >= B
# A.issuperset(B)

# Disjoint
# A.isdisjoint(B)

# Membership
# value in set

# Add
# set.add(value)

# Remove
# set.remove(value)

# Safe Remove
# set.discard(value)

# Remove Arbitrary Element
# set.pop()

# Remove Everything
# set.clear()
