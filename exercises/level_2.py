# Level 2 — Thinking
print("Level 2 — Thinking")

# Given:
numbers = [10, 20, 30, 40, 50]
# Create a new list containing only:
# 20, 30, 40
# Use slicing.
sliced_numbers = numbers[1:4]
print(sliced_numbers)


# Reverse this list using slicing:
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])


# Find how many times 2 occurs:
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
count = 0
for number in numbers:
    if number == 2:
        count +=1 
print(count)


# Find the position of "Python":
languages = ["Java", "C++", "Python", "Go"]
print(languages.index("Python"))


# Sort this list in ascending order:
numbers = [45, 12, 78, 3, 56, 9]
numbers.sort()
print(numbers)

# Then sort it in descending order.
numbers.sort(reverse = True)
print(numbers)
