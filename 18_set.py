9# ============================================================
# SET — CONCEPTS & LEARNING
# ============================================================

# A set is:
# - Unordered
# - Mutable
# - Does NOT allow duplicate values
# - Supports fast membership testing
#
# Common automation/testing uses:
# - Removing duplicate test names
# - Comparing test collections
# - Finding missing tests
# - Finding common tests
# - Checking whether one group of tests is contained in another


# ============================================================
# 1. CREATING A SET
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)

# Duplicate values are automatically removed

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)
# {10, 20, 30}


# ============================================================
# 2. EMPTY SET
# ============================================================

empty_set = set()

print(empty_set)

# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.

empty_dict = {}

print(type(empty_dict))
print(type(empty_set))


# ============================================================
# 3. SET IS UNORDERED
# ============================================================

numbers = {10, 20, 30}

# A set does not provide positional indexing.

# numbers[0]       # TypeError

# Do NOT depend on the printed order of a set.
# Sets are designed for membership and set operations,
# not positional access.


# ============================================================
# 4. SET IS MUTABLE
# ============================================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# The set itself can be changed after creation.


# ============================================================
# 5. add()
# ============================================================

tests = {"login", "checkout"}

tests.add("search")

print(tests)

# If the value already exists, nothing happens.

tests.add("login")

print(tests)


# ============================================================
# 6. remove()
# ============================================================

tests = {"login", "checkout", "search"}

tests.remove("checkout")

print(tests)

# remove() raises KeyError if the value does not exist.

# tests.remove("payment")   # KeyError


# ============================================================
# 7. discard()
# ============================================================

tests = {"login", "checkout", "search"}

tests.discard("checkout")

print(tests)

# discard() does NOT raise an error if the value is missing.

tests.discard("payment")

print(tests)


# remove() vs discard()
#
# remove(value)
# -> Removes value
# -> Raises KeyError if value does not exist
#
# discard(value)
# -> Removes value
# -> Does nothing if value does not exist


# ============================================================
# 8. pop()
# ============================================================

tests = {"login", "checkout", "search"}

removed_test = tests.pop()

print("Removed:", removed_test)
print("Remaining:", tests)

# pop() removes and returns an arbitrary element.
#
# Do NOT assume which element will be removed.


# ============================================================
# 9. clear()
# ============================================================

tests = {"login", "checkout", "search"}

tests.clear()

print(tests)

# Output:
# set()


# ============================================================
# 10. len()
# ============================================================

tests = {"login", "checkout", "search"}

print(len(tests))

# Output:
# 3


# ============================================================
# 11. MEMBERSHIP — in
# ============================================================

tests = {"login", "checkout", "search"}

print("login" in tests)
print("payment" in tests)

# True
# False

# This is one of the most useful operations with sets.


# ============================================================
# 12. ITERATING THROUGH A SET
# ============================================================

tests = {"login", "checkout", "search"}

for test in tests:
    print(test)

# Do not depend on the iteration order of a set.


# ============================================================
# 13. LIST TO SET
# ============================================================

tests = ["login", "checkout", "login", "search", "checkout"]

unique_tests = set(tests)

print(unique_tests)

# Useful for removing duplicates.


# ============================================================
# 14. STRING TO SET
# ============================================================

name = "hello"

characters = set(name)

print(characters)

# Duplicate characters are removed.


# ============================================================
# 15. UNION — |
# ============================================================

android_tests = {"login", "checkout", "search"}
tv_tests = {"login", "checkout", "settings"}

all_tests = android_tests | tv_tests

print(all_tests)

# Union = everything from both sets
# Duplicate values appear only once.


# ============================================================
# 16. INTERSECTION — &
# ============================================================

android_tests = {"login", "checkout", "search"}
tv_tests = {"login", "checkout", "settings"}

common_tests = android_tests & tv_tests

print(common_tests)

# Result:
# {"login", "checkout"}

# Intersection = values common to both sets.


# ============================================================
# 17. DIFFERENCE — -
# ============================================================

all_tests = {"login", "checkout", "search", "payment"}
executed_tests = {"login", "search"}

missing_tests = all_tests - executed_tests

print(missing_tests)

# Result:
# {"checkout", "payment"}

# Difference:
# Values present in the LEFT set
# but NOT present in the RIGHT set.


# ============================================================
# 18. SYMMETRIC DIFFERENCE — ^
# ============================================================

android_tests = {"login", "checkout", "search"}
tv_tests = {"login", "checkout", "settings"}

different_tests = android_tests ^ tv_tests

print(different_tests)

# Result:
# {"search", "settings"}

# Symmetric difference =
# values that exist in either set,
# but NOT in both.


# ============================================================
# 19. SUBSET — <=
# ============================================================

smoke_tests = {"login", "checkout"}

all_tests = {"login", "checkout", "search", "payment"}

print(smoke_tests <= all_tests)

# True

# Every element in smoke_tests exists in all_tests.


# ============================================================
# 20. SUPERSET — >=
# ============================================================

all_tests = {"login", "checkout", "search", "payment"}

smoke_tests = {"login", "checkout"}

print(all_tests >= smoke_tests)

# True

# all_tests contains every element from smoke_tests.


# ============================================================
# 21. DISJOINT SETS
# ============================================================

set1 = {"login", "checkout"}
set2 = {"payment", "search"}

print(set1.isdisjoint(set2))

# True

# Disjoint means:
# The two sets have NO common elements.


# ============================================================
# 22. SET HASHABILITY
# ============================================================

# Set elements must be hashable.

numbers = {10, 20, 30}          # Valid
names = {"John", "David"}       # Valid
items = {(1, 2), (3, 4)}        # Valid


# Lists cannot be set elements because lists are mutable.

# invalid = {[1, 2], [3, 4]}    # TypeError

# Dictionaries cannot be set elements.

# invalid = {{"name": "John"}}  # TypeError


# IMPORTANT:
# Set itself is mutable.
# Therefore a set cannot be used as an element of another set.


# ============================================================
# 23. FROZENSET — IMMUTABLE SET
# ============================================================

numbers = frozenset({10, 20, 30})

print(numbers)

# frozenset is immutable.
#
# It can be used where a hashable set-like object is required.


# ============================================================
# 24. COPY
# ============================================================

tests = {"login", "checkout", "search"}

copied_tests = tests.copy()

copied_tests.add("payment")

print(tests)
print(copied_tests)

# copy() creates a separate set.


# ============================================================
# 25. SET VS LIST
# ============================================================

# LIST
#
# - Ordered
# - Allows duplicates
# - Supports indexing
# - Mutable
#
# SET
#
# - Unordered
# - Does not allow duplicates
# - No indexing
# - Mutable
# - Excellent for membership testing and comparisons


# ============================================================
# 26. AUTOMATION EXAMPLE — REMOVE DUPLICATE TESTS
# ============================================================

test_names = [
    "test_login",
    "test_checkout",
    "test_login",
    "test_search",
    "test_checkout"
]

unique_tests = set(test_names)

print(unique_tests)


# ============================================================
# 27. AUTOMATION EXAMPLE — FIND MISSING TESTS
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
# 28. AUTOMATION EXAMPLE — FIND COMMON TESTS
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
# 29. AUTOMATION EXAMPLE — FIND PLATFORM-SPECIFIC TESTS
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
tv_only = google_tv_tests - android_tests

print("Android only:", android_only)
print("Google TV only:", tv_only)


# ============================================================
# QUICK INTERVIEW SUMMARY
# ============================================================

# Set:
#
# 1. Unordered
# 2. Mutable
# 3. No duplicate values
# 4. No indexing or slicing
# 5. Fast membership testing
#
# Important methods:
#
# add()
# remove()
# discard()
# pop()
# clear()
#
# Important operations:
#
# |   -> Union
# &   -> Intersection
# -   -> Difference
# ^   -> Symmetric Difference
# <=  -> Subset
# >=  -> Superset
#
# Important:
#
# {}      -> Empty dictionary
# set()   -> Empty set
#
# List -> set() is commonly used to remove duplicates.
#
# Set elements must be hashable.
