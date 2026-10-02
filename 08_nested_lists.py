# Python List Mastery
# Topic: Nested Lists

# A nested list is a list that contains other lists.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers)


# Accessing an inner list

print(numbers[0])
# [1, 2, 3]

print(numbers[1])
# [4, 5, 6]


# Accessing individual elements

print(numbers[0][0])
# 1

print(numbers[1][2])
# 6

print(numbers[2][1])
# 8


# Nested list indexing
#
# numbers[outer_index][inner_index]
#
# Example:
# numbers[1][1]
#
# First [1] -> selects [4, 5, 6]
# Second [1] -> selects 5

print(numbers[1][1])
# 5


# Modifying an element inside a nested list

numbers[1][1] = 500

print(numbers)
# [[1, 2, 3], [4, 500, 6], [7, 8, 9]]


# Looping through a nested list

numbers = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in numbers:
    print(row)


# Nested loops
#
# The outer loop gets each inner list.
# The inner loop gets each element.

for row in numbers:
    for number in row:
        print(number)


# Calculating the total of one inner list

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for number in numbers[1]:
    total += number

print(total)
# 15
