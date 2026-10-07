# Lambda Functions in Python
#
# A lambda function is a small anonymous function.
# It is useful when we need a simple function for a short operation.
#
# Syntax:
# lambda parameters: expression


# --------------------------------------------------
# 1. Normal Function vs Lambda
# --------------------------------------------------

def square(x):
    return x * x


print(square(5))


square_lambda = lambda x: x * x

print(square_lambda(5))


# --------------------------------------------------
# 2. Lambda with One Parameter
# --------------------------------------------------

double = lambda x: x * 2

print(double(10))


# --------------------------------------------------
# 3. Lambda with Multiple Parameters
# --------------------------------------------------

add = lambda a, b: a + b

print(add(10, 5))


multiply = lambda a, b: a * b

print(multiply(6, 4))


# --------------------------------------------------
# 4. Lambda Automatically Returns the Expression
# --------------------------------------------------

# Normal function:

def cube(x):
    return x * x * x


# Lambda:

cube_lambda = lambda x: x * x * x

print(cube_lambda(3))


# A lambda does not normally use a separate return statement.
#
# Correct:
# lambda x: x * 2
#
# Not:
# lambda x:
#     return x * 2


# --------------------------------------------------
# 5. Lambda with map()
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)


# map() transforms each item.


# --------------------------------------------------
# 6. Lambda with filter()
# --------------------------------------------------

numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 20, numbers))

print(result)


# filter() selects items that satisfy a condition.


# --------------------------------------------------
# 7. Lambda with Strings
# --------------------------------------------------

names = ["alice", "bob", "andrew", "charlie"]

result = list(
    filter(lambda name: name.startswith("a"), names)
)

print(result)


# --------------------------------------------------
# 8. Combining filter() and map()
# --------------------------------------------------

names = ["alice", "bob", "andrew", "charlie", "amanda"]

result = list(
    map(
        lambda name: name.upper(),
        filter(lambda name: name.startswith("a"), names)
    )
)

print(result)


# First filter() selects the required items.
# Then map() transforms the selected items.


# --------------------------------------------------
# 9. Lambda with Conditional Expression
# --------------------------------------------------

get_status = lambda score: "PASS" if score >= 50 else "FAIL"

print(get_status(75))
print(get_status(30))


# --------------------------------------------------
# 10. Lambda in Automation Testing
# --------------------------------------------------

test_results = [
    ["login", "PASS"],
    ["payment", "FAIL"],
    ["search", "PASS"],
    ["checkout", "FAIL"]
]

failed_tests = list(
    filter(lambda test: test[1] == "FAIL", test_results)
)

print(failed_tests)


# --------------------------------------------------
# 11. Lambda with sorted()
# --------------------------------------------------

# Lambda is commonly used with sorted(key=...)
# to tell sorted() which value should be used for sorting.

tests = [
    ["login", 120],
    ["payment", 450],
    ["search", 80],
    ["checkout", 300]
]

result = sorted(tests, key=lambda test: test[1])

print(result)


# --------------------------------------------------
# KEY TAKEAWAYS
# --------------------------------------------------

# lambda creates a small anonymous function.
#
# Syntax:
# lambda parameters: expression
#
# Lambda automatically returns the expression.
#
# map() + lambda:
# transforms data.
#
# filter() + lambda:
# selects data.
#
# sorted() + lambda:
# tells sorted() which value to use for sorting.
#
# Lambda is best for small, simple operations.
# For complex logic, use a normal def function.

