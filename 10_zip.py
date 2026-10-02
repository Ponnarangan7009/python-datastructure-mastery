# Python List Mastery
# Topic: zip()

# zip() combines corresponding elements
# from two or more lists.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]


# Combining two lists

for name, age in zip(names, ages):
    print(name, age)

# Output:
# Alice 25
# Bob 30
# Charlie 28


# Another example

devices = ["Pixel", "Samsung", "OnePlus"]
results = ["PASS", "FAIL", "PASS"]

for device, result in zip(devices, results):
    print(device, result)


# Creating a list from zip()

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

student_scores = list(zip(names, scores))

print(student_scores)

# Output:
# [('Alice', 90), ('Bob', 85), ('Charlie', 95)]


# zip() with three lists

devices = ["Pixel", "Samsung", "OnePlus"]
versions = ["Android 16", "Android 15", "Android 14"]
results = ["PASS", "FAIL", "PASS"]

for device, version, result in zip(devices, versions, results):
    print(device, version, result)


# zip() with a condition

test_names = ["login", "logout", "payment", "search"]
test_results = ["PASS", "PASS", "FAIL", "PASS"]

for test_name, result in zip(test_names, test_results):
    if result == "FAIL":
        print(test_name, result)


# Important:
# Normal zip() stops when the shortest list runs out.

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)

# Charlie is not included because scores
# does not have a corresponding value.
