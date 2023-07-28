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




