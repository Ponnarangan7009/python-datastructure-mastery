# Don't use enumerate(), zip(), sum(), flatten() libraries, or list comprehension yet.
# Create this nested list:
# [    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]]
nested_list = [[10, 20, 30],    [40, 50, 60],    [70, 80, 90]]
# Print the entire list.
print(nested_list)


# Using the same list, print:
print(nested_list[1][1])


# Print:
# 70
print(nested_list[2][0])


# Print the first inner list:
# [10, 20, 30]
print(nested_list[0])

# Change 50 to 500.
# Expected:
# [[10, 20, 30],    [40, 500, 60],    [70, 80, 90]]
nested_list[1][1] = 500
print(nested_list)


# Given:
numbers = [    [1, 2, 3],    [4, 5, 6],    [7, 8, 9]]
# Calculate the sum of the second inner list.
# Expected:
# 15
sum = 0
for number in numbers[1]:
    sum += number
print(sum)


# Given:
numbers = [[1, 2],    [3, 4],    [5, 6]]
# Create a new list containing all the numbers:
# [1, 2, 3, 4, 5, 6]
new_list = []
for num in numbers:
    for number in num:
        new_list.append(number)
print(new_list)

