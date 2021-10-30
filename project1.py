"""
print("Hello World")
print("      /|")
print("     / |")
print("    /  |")
print("   /___|")
character_name = "George"
character_age = "70"
is_Male = True
# False
print("There was a man named , " + character_name)
print("he was " + character_name + " years old. ")
print("He really liked the name " + character_name)
print("but didn't like being " + character_age)
my_num = 5
print(str(my_num) + " What the hell?")

# add new line \n, quotation mark \" , backslash \
phrase = "Giraffe Academy"

# convert to upper or lower
print(phrase.upper())

# number of characters
print(len(phrase))

# grab index 3
print(phrase[3])

# return the index of G
print(phrase.index("G"))

# replace
print(phrase.replace("d", "fuck"))

# 25 raised to 4
print(pow(25, 4))

#imports
from math import *

my_num = -5
print(sqrt(25.56))

# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + " You are " + age)

# number
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = int(num1) + int(num2)
print(result)

# double
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)

# madlib

color = input("Enter a color ")
plural_noun = input("Enter a Plural Noun ")
celebrity = input("Enter a celebrity ")


print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Lists
friends = ["John", "Sharon", "Jane", "Jim"]
print(friends)
print(friends[3])

# items from the back of the list from the back first is -1
print(friends[-1])

# items after index 1 to 3
print(friends[1:3])

# items after index 1
print(friends[1:])

# modify
friends[1] = "Joshua"
print(friends[1])

# Lists
lucky_numbers = [4, 5, 6, 34, 86, 9, 12]
friends = ["John", "Sharon", "Jane", "Jim"]
# add friends to lucky numbers
friends.extend(lucky_numbers)
print(friends)

# add item to the end of the list
friends.append("Creek")

# add item at a point of the list
friends.insert(2, "kelly")

# remove item at a point of the list
friends.remove("Jim")

# remove all item at a point of the list
friends.clear()

# pop last item at a point of the list
friends.pop()

# find index of item in the list

print(friends.index("Jim"))

# count index of item in the list
print(friends.count("Jim"))

# sort index of item in the list
friends.sort()
print(friends)

# reverse index of item in the list
lucky_numbers.reverse()
print(lucky_numbers)

# copy the list
friends2 = friends.copy()
print(friends2)

# Tuple(Type of data structure its a container) similar to list
# tuples are immutable(Can't change,add, edit,delete)

coordinates = [(4, 5), (6, 7), (80, 34)]
coordinates = (4, 5)

print(coordinates[0])
coordinates[0] = 10 # not allowed

# Functions
def say_hi():
    print("Hello User")


print("Top")
say_hi()
print("Bottom")

# Functions
# parameters
def say_hi(name, age):
    print("Hello " + name + " You are " + age)


say_hi("Jane", "45")
say_hi("Christ", "9")

def say_hi(name, age):
    print("Hello " + name + " You are " + str(age))


say_hi("Jane", 45)
say_hi("Christ", 9)


# Return statements in python functions
def cube(num):
    return num * num * num


# nothing should be printed after return

result = cube(4)
print(result)

# if statement
is_male = True

if is_male:
    print("You are a male")
else:
    print("You are a female")
if is_male or is_tall:
    print("You are a male or tall or both")
    # else if
elif is_male and not (is_tall):
    print("You are a male and not tall ")
elif not (is_male) and is_tall:
    print("You are not a male and tall ")
else:
    print("You are a neither male nor tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("num1 is the maximum")
    elif num2 >= num1 and num2 >= num3:
        print("num2 is the maximum")
    else:
        return num3


print(max_num(3, 5, 6))

num1 = float(input("Enter a number: "))

operator = input("Enter operator: ")

num2 = float(input("Enter a second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator ")

# Dictionaries key must be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Ap": "April"
}
print(monthConversions.get("Bro", "Not a valid key"))

print(monthConversions.get("Jan"))
print(monthConversions["Ap"])

# While loop
i = 1
while i <= 2:
    print(i)
    #  i = i + 1
    i += 1
print("Done the loop")

# Basic guessing game
secret_word = "giraffe"

guesses = ""

while guesses != secret_word:
    guesses = input("Enter guess: ")

print("You win!")

# Basic guessing game
secret_word = "giraffe"

guesses = ""

guess_count = 0

guess_limit = 3

out_of_guesses = False

while guesses != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guesses = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose")
else:
    print("You win!")

# For loop
friends = ["Jim", "Karen"]
for name in friends:
    print(name)
for letter in "Giraffe Academy":
    print(letter)
for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)
    for index in range(len(friends)):
    print(friends[index])

# For loop
friends = ["Jim", "Karen"]

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")

        # Exponents


def raised_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raised_to_power(2, 5))
print(2**3)

# 2D lists and nested loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# row is o and column 1 is 2
print(number_grid[0][1])

# 2D lists and nested loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# row is o and column 1 is 2
print(number_grid[0][1])

for row in number_grid:
    for column in row:
        print(column)

# Basic translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase ")))


try:
    ans = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)

"""
# Reading from external files

# r read only
# w write only
# a append only
# r+ read and write

seasons_file = open("Seasons.csv", "r")
# make sure the file is readable
# print(seasons_file.readable())
# read
# print(seasons_file.read())
# read the first line
print(seasons_file.readline())
seasons_file.close()

