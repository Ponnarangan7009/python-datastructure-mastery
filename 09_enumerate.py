# Python List Mastery
# Topic: enumerate()

# enumerate() allows us to get both:
# 1. The index
# 2. The value
# while looping through a list.

languages = ["Python", "Java", "C++"]


# Normal loop

for language in languages:
    print(language)


# Using enumerate()

for index, language in enumerate(languages):
    print(index, language)

# Output:
# 0 Python
# 1 Java
# 2 C++


# enumerate() gives us index + value.

for index, language in enumerate(languages):
    print(f"{language} is at index {index}")


# Starting the index from 1

for index, language in enumerate(languages, start=1):
    print(index, language)

# Output:
# 1 Python
# 2 Java
# 3 C++


# Useful for displaying numbered items

test_results = ["PASS", "FAIL", "PASS", "FAIL"]

for test_number, result in enumerate(test_results, start=1):
    print(f"Test {test_number}: {result}")


# Using enumerate() with a condition

for test_number, result in enumerate(test_results, start=1):
    if result == "FAIL":
        print(f"Test {test_number}: {result}")
