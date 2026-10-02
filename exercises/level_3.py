# Level 3 — List Comprehension
# Given:
numbers = [1, 2, 3, 4, 5]
# Create:
# [1, 4, 9, 16, 25]
# using list comprehension.

squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a list containing only even numbers.
even_numbers = [number for number in numbers if number %2==0]
print(even_numbers)

# Given:
names = ["alice", "bob", "charlie", "david"]
# Create:
# ["ALICE", "BOB", "CHARLIE", "DAVID"]
# using list comprehension.
upper_names = [name.upper() for name in names ]
print(upper_names)



# Given:
numbers = [1, 2, 3, 4, 5]
# Create:
# [10, 20, 30, 40, 50]
# using list comprehension.
times_ten_numbers = [number * 10 for number in numbers]
print(times_ten_numbers)


# Given:
numbers = [10, 15, 20, 25, 30, 35, 40]
# Create a list containing numbers that are:
# - greater than 20
# - divisible by 5
# Expected:
# [25, 30, 35, 40]
custom_numbers = [number for number in numbers if number > 20 and number %5==0]
print(custom_numbers)
