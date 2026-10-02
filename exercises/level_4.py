# Level 4 — Automation-flavored problems
# You receive test results:
results = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "PASS"]
# Create a list containing only failed results.
failed_results = [result for result in results if result == "FAIL"]
print(failed_results)


# You receive:
test_names = [    "test_login",    "test_logout",    "test_payment",    "test_search"]
# Create a list containing only tests whose names contain "login" or "payment".
custom_test = [test for test in test_names if "login" in test or "payment" in test]
print(custom_test)

custom_test = [test for test in test_names if test.endswith(("login", "payment"))]
print(custom_test)


# Given:
devices = ["Pixel", "Samsung", "Pixel", "OnePlus", "Samsung", "Pixel"]
# Create a list containing only unique device names.
# Do not use set() yet.
# This one forces you to think about list operations.
unique_devices = []

for device in devices:
    if device not in unique_devices:
        unique_devices.append(device)

print(unique_devices)


# Given:
numbers = [10, 20, 30, 40, 50]
# Write code that creates:
# [50, 40, 30, 20, 10]
# without using .reverse().
print(numbers[::-1])


# Given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a list containing the squares of only the even numbers.
# Expected:
# [4, 16, 36, 64, 100]
# This combines:
# expression + loop + condition
# [expression for item in iterable if condition]
even_square_numbers = [number**2 for number in numbers if number %2==0]
print(even_square_numbers)
