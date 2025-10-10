# Week 1: Python Basics by Mughees

print("Welcome to Week 1 of Python Learning")

# Variables and Data Types
a = 10
b = 3.5
c = "Mughees"
d = True
x, y, z = 5, 10, 15

print(a, b, c, d, x, y, z)
print(type(a), type(b), type(c), type(d))

# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")

# Arithmetic Operations
sum_result = a + b
diff_result = x - y
mul_result = x * z
div_result = z / y
mod_result = x % a
print(sum_result, diff_result, mul_result, div_result, mod_result)

# Conditional Statements
if age < 18:
    print("You are a minor")
elif age == 18:
    print("You just became an adult")
else:
    print("You are an adult")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# While Loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

# For Loop
for j in range(1, 6):
    print("Square of", j, "is", j * j)

# Lists
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

fruits.append("mango")
fruits.remove("banana")
print(fruits)
print(fruits[0], fruits[-1])

nums = [2, 4, 6, 8, 10]
total = 0
for n in nums:
    total += n
print("Sum:", total)
print("Max:", max(nums), "Min:", min(nums))

# Tuples
tuple1 = (1, 2, 3, 4)
print(tuple1[1], len(tuple1))

# Sets
set1 = {1, 2, 3, 3, 2, 1}
set2 = {3, 4, 5}
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))

# Dictionaries
person = {"name": "Mughees", "age": 18, "city": "Lahore"}
print(person["name"])
person["profession"] = "Student"
print(person.keys())
print(person.values())

# Functions
def greet(n):
    return "Hello " + n

print(greet(name))

def add(a, b):
    return a + b

print(add(5, 7))

# Factorial Function
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print("Factorial of 5:", factorial(5))

# Prime Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

# String Reversal
def reverse_string(s):
    return s[::-1]

print(reverse_string("Machine Learning"))

# Vowel Counter
def count_vowels(s):
    v = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in v:
            count += 1
    return count

print("Vowels:", count_vowels("Artificial Intelligence"))

# List Comprehension
nums = [3, 6, 9, 12, 15]
sq = [n * n for n in nums]
print(sq)

# Nested Loop (Matrix Example)
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# String Iteration
s = "python"
for ch in s:
    print(ch)

# Exception Handling
try:
    num = int(input("Enter a number to divide 100: "))
    print(100 / num)
except:
    print("Invalid input or division by zero")

# File Handling
file = open("test.txt", "w")
file.write("Hello, this is Week 1 learning summary.")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

