#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# 2. Write a Python Program to Check if a Number is Odd or Even?
# 3. Write a Python Program to Check Leap Year?
# 4. Write a Python Program to Check Prime Number?
# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[4]:


num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[6]:


#2
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# In[7]:


#3
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# In[8]:


#4
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# In[9]:


#5
for num in range(1, 10001):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                break
        else:
            print(num)

