# Day 4 - Strings in Python
# Topics: indexing, slicing, methods, reverse, palindrome, vowel count

# 1. String indexing and slicing

text = "python"

print("Indexing examples:")
print(text[0])      # first character
print(text[1])      # second character
print(text[-1])     # last character

print("\nSlicing examples:")
print(text[0:3])    # characters from index 0 to 2
print(text[1:])     # from index 1 to end
print(text[:4])     # from start to index 3
print(text[::-1])   # reverse string


# 2. String methods

text = "  Hello World  "

print("\nString methods:")
print(text.lower())                     # convert to lowercase
print(text.upper())                     # convert to uppercase
print(text.strip())                     # remove spaces from both ends
print(text.lstrip())                    # remove left spaces
print(text.rstrip())                    # remove right spaces
print(text.split())                     # split by space
print(text.find("W"))                   # find index of W
print(text.replace("Hello", "Python"))  # replace word


# 3. Split using custom separator

text = "apple,banana,orange"
fruits = text.split(",")

print("\nSplit with comma:")
print(fruits)


# 4. Extract username from email

email = "sam@gmail.com"
username = email.split("@")[0]
print("\nUsername from email:", username)


# 5. Reverse a string (user input)

text = input("\nEnter a text to reverse: ")
print("Reversed text:", text[::-1])


# 6. Palindrome check

text = input("\nEnter a word to check palindrome: ")

if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")



# 7. Count vowels in a string


text = input("\nEnter text to count vowels: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Total number of vowels:", count)
