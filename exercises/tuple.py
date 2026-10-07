"""
TUPLE - EXERCISES WITH ANSWERS
==============================
"""


# ============================================================
# Q1. INDEXING
# ============================================================

data = ("login", "PASS", 120, "Chrome")

print(data[0])    # login
print(data[1])    # PASS
print(data[-1])   # Chrome


# ============================================================
# Q2. SLICING
# ============================================================

data = ("login", "PASS", 120, "Chrome", "Android")

print(data[1:4])  # ("PASS", 120, "Chrome")
print(data[-2:])  # ("Chrome", "Android")


# ============================================================
# Q3. IMMUTABILITY
# ============================================================

data = ("login", "PASS", 120)

# data[1] = "FAIL"

# Answer:
# TypeError
#
# Tuples are immutable, so existing elements
# cannot be changed.


# ============================================================
# Q4. SINGLE-ELEMENT TUPLE
# ============================================================

x = (10,)

print(type(x))

# Answer:
# tuple
#
# The comma is required to create a single-element tuple.


# ============================================================
# Q5. count() AND index()
# ============================================================

results = ("PASS", "FAIL", "PASS", "PASS", "FAIL")

print(results.count("PASS"))   # 3
print(results.index("FAIL"))   # 1


# ============================================================
# Q6. NORMAL UNPACKING
# ============================================================

test = ("login", "PASS", 120)

name, status, time = test

print(name)     # login
print(status)   # PASS
print(time)     # 120


# ============================================================
# Q7. += WITH A TUPLE
# ============================================================

test = ("login", "PASS", 120)

test += ("Chrome",)

print(test)

# Answer:
# ("login", "PASS", 120, "Chrome")
#
# += creates a NEW tuple and reassigns it to test.
# It does not modify the original tuple.


# ============================================================
# Q8. TUPLE REPETITION
# ============================================================

test = ("login", "PASS", 120)

result = test * 2

print(result)

# Answer:
# ("login", "PASS", 120, "login", "PASS", 120)


# ============================================================
# Q9. MEMBERSHIP
# ============================================================

test = ("login", "PASS", 120, "Chrome")

print("PASS" in test)   # True
print("FAIL" in test)   # False


# ============================================================
# Q10. NESTED TUPLE
# ============================================================

test = (
    ("login", "PASS"),
    ("search", "FAIL"),
    ("checkout", "PASS")
)

print(test[1][0])   # search
print(test[1][1])   # FAIL


# ============================================================
# Q11. STARRED UNPACKING
# ============================================================

test = ("login", "PASS", 120, "Chrome")

name, status, *details = test

print(name)      # login
print(status)    # PASS
print(details)   # [120, "Chrome"]

# Answer:
# The starred variable receives the remaining
# values as a LIST.


# ============================================================
# Q12. STARRED UNPACKING
# ============================================================

data = ("login", "PASS", 120)

name, *details = data

print(name)      # login
print(details)   # ["PASS", 120]


# ============================================================
# Q13. LIST → TUPLE
# ============================================================

data = ["login", "PASS", 120]

result = tuple(data)

print(result)

# Answer:
# ("login", "PASS", 120)


# ============================================================
# Q14. TUPLE WITH MUTABLE OBJECT
# ============================================================

data = ("login", ["PASS", "FAIL"])

data[1].append("SKIPPED")

print(data)

# Answer:
# ("login", ["PASS", "FAIL", "SKIPPED"])
#
# The tuple is immutable, but the list inside
# the tuple is mutable.


# ============================================================
# Q15. TUPLE AS DICTIONARY KEY
# ============================================================

data = {
    ("login", "PASS"): 120,
    ("search", "PASS"): 150
}

print(data[("login", "PASS")])

# Answer:
# 120
#
# A tuple can be a dictionary key when all
# of its elements are hashable.


# ============================================================
# FINAL INTERVIEW CHECK
# ============================================================

"""
Q1. Is a tuple mutable?
Answer: No.

Q2. Does a tuple allow duplicates?
Answer: Yes.

Q3. Does a tuple support indexing?
Answer: Yes.

Q4. Does a tuple support slicing?
Answer: Yes.

Q5. How do you create a single-element tuple?
Answer: (10,)

Q6. Can a tuple contain a list?
Answer: Yes.

Q7. Can the list inside a tuple be modified?
Answer: Yes.

Q8. Can every tuple be used as a dictionary key?
Answer: No.
A tuple can be a dictionary key only when all
its elements are hashable.

Q9. What does *details do during unpacking?
Answer: It collects the remaining values into a list.

Q10. What does tuple(list) do?
Answer: Converts a list into a tuple.

Q11. What does list(tuple) do?
Answer: Converts a tuple into a list.
"""
