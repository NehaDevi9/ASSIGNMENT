#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Add the current date to the text file today.txt as a string.
2. Read the text file today.txt into the string today_string
3. Parse the date from today_string.
4. List the files in your current directory
5. Create a list of all of the files in your parent directory (minimum five files should be available).
6. Use multiprocessing to create three separate processes. Make each one wait a random number of
seconds between one and five, print the current time, and then exit.
7. Create a date object of your day of birth.
get_ipython().run_line_magic('pinfo', 'birth')
get_ipython().run_line_magic('pinfo', 'old')


# In[3]:


import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
with open("today.txt", "w") as file:
    file.write(current_date)
print(current_date)


# In[5]:


from dateutil.parser import parse

parsed_date = parse(today_string).date()
print(parsed_date)


# In[6]:


import os

current_directory_files = os.listdir('.')
print(current_directory_files)


# In[7]:


parent_directory = os.path.abspath('..')
parent_directory_files = os.listdir(parent_directory)
print(parent_directory_files[:5])  # Displaying the first five files (if available)


# In[8]:


import multiprocessing
import random
import time
import datetime

def print_current_time():
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Process {multiprocessing.current_process().name}: Current time - {current_time}")

if __name__ == "__main__":
    processes = [multiprocessing.Process(target=print_current_time) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


# In[9]:


from datetime import date

# Replace the following with your actual birthdate
birthdate = date(1990, 10, 15)
print(birthdate)


# In[10]:


day_of_week = birthdate.strftime("%A")
print(f"The day of the week for my day of birth was: {day_of_week}")


# In[11]:


from datetime import timedelta

days_to_add = 10000
future_date = birthdate + timedelta(days=days_to_add)
print(f"I will be (or was) 10,000 days old on: {future_date}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Sure! Here are some practice programs that implement different control structures in Python:
# 
# 1. If-Else Statement:
# ```
# # Program to check if a number is positive, negative, or zero
# num = float(input("Enter a number: "))
# 
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")
# ```
# 
# 2. For Loop:
# ```
# # Program to print the elements of a list
# fruits = ["apple", "banana", "cherry"]
# 
# for fruit in fruits:
#     print(fruit)
# ```
# 
# 3. While Loop:
# ```
# # Program to find the sum of natural numbers up to a given number
# n = int(input("Enter a positive integer: "))
# sum = 0
# i = 1
# 
# while i <= n:
#     sum += i
#     i += 1
# 
# print("The sum is", sum)
# ```
# 
# 4. Nested Loop:
# ```
# # Program to print a pattern using nested loops
# rows = 5
# 
# for i in range(rows):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# ```
# 
# 5. Break Statement:
# ```
# # Program to search for an element in a list
# numbers = [1, 2, 3, 4, 5, 6]
# search_num = int(input("Enter the number to search: "))
# 
# for num in numbers:
#     if num == search_num:
#         print("Number found!")
#         break
# else:
#     print("Number not found!")
# ```
# 
# 6. Continue Statement:
# ```
# # Program to print all even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6]
# 
# for num in numbers:
#     if num % 2 != 0:
#         continue
#     print(num)
# ```
# 
# 7. Try-Except Statement:
# ```
# # Program to handle division by zero exception
# try:
#     dividend = int(input("Enter the dividend: "))
#     divisor = int(input("Enter the divisor: "))
#     result = dividend / divisor
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# ```
# 
# These programs cover various control structures in Python, including if-else statements, loops (for and while), nested loops, break and continue statements, and try-except statements. You can practice running and modifying these programs to deepen your understanding of control structures in Python.
# Certainly! Here are a few more practice programs that implement different control structures in Python:
# 
# 8. Nested If-Else Statement:
# ```
# # Program to check if a year is a leap year
# year = int(input("Enter a year: "))
# 
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")
# ```
# 
# 9. Range Function with Step:
# ```
# # Program to print even numbers using the range function with step
# start = 0
# end = 20
# step = 2
# 
# for num in range(start, end+1, step):
#     print(num)
# ```
# 
# 10. List Comprehension:
# ```
# # Program to create a new list with only the even numbers from an existing list
# numbers = [1, 2, 3, 4, 5, 6]
# 
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
# ```
# 
# 11. Enumerate Function:
# ```
# # Program to print the index and value of each element in a list
# fruits = ["apple", "banana", "cherry"]
# 
# for index, fruit in enumerate(fruits):
#     print("Index:", index, "Fruit:", fruit)
# ```
# 
# 12. Pass Statement:
# ```
# # Program to print the first 5 even numbers and skip the rest
# count = 0
# 
# for num in range(10):
#     if num % 2 == 0:
#         print(num)
#         count += 1
#     if count == 5:
#         break
#     pass
# ```
# 
# 13. Assert Statement:
# ```
# # Program to calculate the factorial of a number using recursion
# def factorial(n):
#     assert n >= 0, "Factorial not defined for negative numbers."
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# 
# num = int(input("Enter a non-negative integer: "))
# result = factorial(num)
# print("Factorial:", result)
# ```
# 
# These additional programs cover more control structures in Python, including nested if-else statements, range function with step, list comprehension, enumerate function, pass statement, and assert statement. Feel free to practice running and modifying these programs to further strengthen your understanding of control structures in Python.
