# Zip() Excercise
# Given:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
# Use zip() to produce:
# Alice 25
# Bob 30
# Charlie 28
for name, age in zip(names, ages):
    print(name, age)


# Two lists
# Given:
devices = ["Pixel", "Samsung", "OnePlus"]
results = ["PASS", "FAIL", "PASS"]
# Use zip() to produce:
# Pixel PASS
# Samsung FAIL
# OnePlus PASS
for device, result in zip(devices, results):
    print(device, result)

# Create a new list
# Given:
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]
# Create:
# [("Alice", 90),    ("Bob", 85),    ("Charlie", 95)]
# using zip().
# Hint: You can use:
# list(zip(...))
print(list(zip(names, scores)))

# Automation example
# Given:
test_names = ["login", "logout", "payment", "search"]
test_results = ["PASS", "PASS", "FAIL", "PASS"]
# Print only the failed test:
# payment FAIL
# Use zip().
for name, result in zip(test_names, test_results):
    if result == "FAIL":
        print(name, result)


# Challenge
# Given:
devices = ["Pixel", "Samsung", "OnePlus"]
versions = ["Android 16", "Android 15", "Android 14"]
results = ["PASS", "FAIL", "PASS"]
# Use zip() to produce:
# Pixel Android 16 PASS
# Samsung Android 15 FAIL
# OnePlus Android 14 PASS
# You need to combine three lists.
for device, version, result in zip(devices, versions, results):
    print(device, version, result)
