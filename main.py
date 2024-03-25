#introduction
print("Hello world")
print("         /|")
print("        / |")
print("       /  |  ")
print("      /   |")
print("     /    |")
print("    /     |")
print("   /      |")
print("  /       |")
print(" /        |")
print("/_________|")

#working with variables
character_name = "Charles"
character_age = "21"
is_Male = True
print("There was once a man named " + character_name + " , ")
print("He was " + character_age + " years old")
print("He really liked the name " + character_name + " ")
print("but didnt like being"  + character_age + " years old")

#working with strings
phrase = "Cow Academy"
print (phrase.upper() + "is cool")
print("Giraffe\nAcademy")
print(len(phrase))
print(phrase[0])
print(phrase.index("A"))
print(phrase.replace("Cow", "Elephant"))

#working with numbers
from math import *
print(2)
print(2.5435)
print(-3.6546)
print(2 +9.8433)
print(10%3) #modulus operator
my_num = 5
print(my_num)
print(str(my_num) + "my favorite number")
print(abs(my_num))
print(min(3,2))
print(round(3.7))
print(sqrt(36))

#introduction practise
print("hello charlie")

#working with variables practise
character_name = "Hillary"
character_age = "36"
print("There was once a man named" + character_name)
print("He was uneducated but hardworking")
print("He was 36 years old")
print("He wished he was not" + character_age +"years old")

#variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "python programming"
print(students_count)

#how to use strings in python
course = "python programming"
print(len(course))
print(course[0])
print(course[0:3])

#escape sequences
course = "Python \"programming "
print(course)
#Formatted strings
first = "Mosh"
last = "Hamedani"
full = f"{first} {last}"
print(full)

#string methods
course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.strip())
print(course.find("pro"))
print("Pro" in course)
print("swift" not in course)

#Getting input from users
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello\n"  + name + "\n!you are\n" +  age)
