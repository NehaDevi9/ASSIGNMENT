#!/usr/bin/env python
# coding: utf-8
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70

# In[2]:


def divisible_by_5_and_7_ganerator(n):
    for num in range (n+1):
        if num % 5== 0 and num % 7 == 0:
            yield num
            
def main():
    try:
        n = int(input("Enter a value for n:"))
        result = divisible_by_5_and_7_ganerator(n)
        output = ",".join(str(num) for num in result)
        print(output)
        
    except valueError:
        print("Invalid input.please enter a valid integer for n.")
        
if __name__ =="__main__":
    main()

Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
# In[4]:


def even_numbers_generator(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num
            
            
def main():
    try:
        
        n = int(input("Enter the num for n:"))
        result = even_numbers_generator (n)
        output = ",".join(str(num) for num in result)
        print(output)
        
    except ValueError:
        print("Invalid input. please enter a valid integr for n.")
        
if __name__ == "__main__":
    main()

Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13

# In[1]:


def fibbonicci_sequence(n):
    sequence = [0,1]
    for i in range(2, n+1):
        next_number = sequence[-1]+sequence[-2]
        sequence.append(next_number)
        
    return sequence[:n+1]

def main():
    try:
        n = int(input("enter n value for n:"))
        result = fibbonicci_sequence(n)
        output = ",".join(str(num)for num in result)
        print(output)
    except ValueError:
        print("Invalid input. please eneeter a valid integer for n.")
        
        
if __name__ == "__main__":
    main()

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john

# In[2]:


def extract_username(email):
    username, _ = email.split('@')
    return username

def main():
    try:
        email = input("Enter an email address: ")
        username = extract_username(email)
        print(username)
    except ValueError:
        print("Invalid email address formate ")
        
if __name__ == "__main__":
    main()

Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# In[7]:


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


def main():
    shape = Shape()
    square = Square(5)

    print("Area of the generic shape:", shape.area()) 
    print("Area of the square:", square.area())       

if __name__ == "__main__":
    main()


# In[ ]:





# # ASSINGMENt16

# Question1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
# Examples
# stutter("incredible") ➞ "in... in... incredible?"
# 
# stutter("enthusiastic") ➞ "en... en... enthusiastic?"
# 
# stutter("outstanding") ➞ "ou... ou... outstanding?"
# 
# Hint :- Assume all input is in lower case and at least two characters long.
# 

# In[17]:


def stutter(word):
    first_two_letters = word[:2]
    stuttered_word = f"{first_two_letters}...{first_two_letters}...{word}?"
    return stuttered_word

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))
    
    

Question 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8

# In[18]:


import math

def radians_to_degrees(radians):
    degrees = radians *(180/math.pi)
    return round(degrees, 1)

print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))

Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29

# In[20]:


def is_curzon(num):
    power_value = 2 ** num +1
    multiply_value = 2 * num+1
    return power_value % multiply_value == 0

print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))

Question 4.Given the side length x find the area of a hexagon.

Examples
area_of_hexagon(1) ➞ 2.6

area_of_hexagon(2) ➞ 10.4

area_of_hexagon(3) ➞ 23.4

# In[21]:


import math 

def area_of_hexagon(x):
    area = (3 * math.sqrt(3)*x**2) / 2
    return round(area, 1)
    
print(area_of_hexagon(1))
print(area_of_hexagon(2))
print(area_of_hexagon(3))

Question 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
Examples
binary(1) ➞ "1"
# 1*1 = 1

binary(5) ➞ "101"
# 1*1 + 1*4 = 5

binary(10) ➞ "1010"
# 1*2 + 1*8 = 10


# In[22]:


def binary(decimal):
    if decimal == 0:
        return "0"
    
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal //= 2

    return binary_str


print(binary(1)) 
print(binary(5))
print(binary(10))


# In[ ]:




