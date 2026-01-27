"""
Day 5 – Python Collections
Topics: List, Tuple, Set
"""

# --------------------------------------------------
# THEORY (for quick revision)
# --------------------------------------------------

# List:
# - Ordered
# - Mutable
# - Allows duplicates
# Example: [1, 2, 3]

# Tuple:
# - Ordered
# - Immutable
# Example: (1, 2, 3)

# Set:
# - Unordered
# - Mutable
# - No duplicates
# Example: {1, 2, 3}

# 1. LIST BASICS

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 2. LIST METHODS

values = [10, 30, 5, 60]
print("\nInitial list:", values)

values.append(8)          # add at end
print("After append:", values)

values.insert(2, 9)       # insert at index 2
print("After insert:", values)

values.remove(5)          # remove value 5
print("After remove:", values)

values.pop()              # remove last element
print("After pop:", values)

values.sort()             # sort list
print("After sort:", values)

values.reverse()          # reverse list
print("After reverse:", values)

# 3. FIND SUM OF LIST

nums = [100, 30, 5, 60]
total = sum(nums)
print("\nSum of list:", total)

# 4. FIND LARGEST NUMBER (WITHOUT max())

numbers = [100, 30, 5, 60]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)

# 5. REMOVE DUPLICATES USING SET

numbers = [100, 30, 5, 60, 30]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)
