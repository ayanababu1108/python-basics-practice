# -----FOR LOOP-----
# print 1 to 5
for i in range(1,6):
    print(i)

# print 0 to 4
for i in range(5):
  print(i)

# Print even numbers from 1 to 10

for i in range(1,11):
  if(i%2 == 0):
    print(i)
# -----WHILE LOOP-----

# Print 1 to 5

i = 1
while i < 6:
  print(i)
  i=i+1

# break and continue

for i in range(1,10):
  if i == 5:
    break
  print(i)

for i in range(1,10):
  if (i == 5):
    continue
  print(i)
# Print numbers from 1 to 10

for i in range(1,11):
  print(i)

# Print even numbers from 1 to 20

for i in range(1,21):
  if(i%2 == 0):
    print(i)

# Find sum of numbers from 1 to 10
total = 0
for i in range(1,11):
  total=total+i
print(total)

# Print multiplication table of a number
num = int(input("Enter a number"))
for i in range(1,11):
  print(i*num) 