# Day 2 - Operators and Conditions

a = 10
b = 3
print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)

x = 5
print(x)
x += 5
print(x)
x -= 3
print(x)

a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print(a > 5 and b > 5)
print(a > 5 and b > 50)
print(a > 5 or b > 50)
print(not a > b)

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the largest number")
elif b >= a and b >= c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")

largest = max(a, b, c)
print("Largest number is:", largest)

year = int(input("Enter a year"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
