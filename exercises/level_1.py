# Level 1 — Fundamentals
print("Level 1 — Fundamentals")

print("Create a list containing:")
print("10, 20, 30, 40, 50")

numbers = [10, 20, 30, 40, 50]
print(numbers)

print("Print the first and last elements.")
# Given:
# numbers = [10, 20, 30, 40, 50]
print(numbers[0], numbers[-1])

print("Change 30 to 100.")
# Expected:
# [10, 20, 100, 40, 50]

numbers[2] = 100
print(numbers)


# Given:
languages = ["Python", "Java", "C++"]
# Add 'JavaScript' to the end.
print("Add 'JavaScript' to the end.")
languages.append("JavaScript")
print(languages)


# Given:
numbers = [1, 2, 3]
# Add:
# 4, 5, 6 at the end of the list.
numbers.extend([4,5,6])
print(numbers)


# Given:
numbers = [10, 20, 30, 40]
# Remove 30.
numbers.remove(30)
print(numbers)
