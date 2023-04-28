#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?
# 2. Write a Python program to convert Celsius to Fahrenheit?
# 3. Write a Python program to display calendar?
# 4. Write a Python program to solve quadratic equation?
# 5. Write a Python program to swap two variables without temp variable?

# In[6]:


kilometers = float(input("Enter value in kilometers: "))
conversion_factor = 0.621371 # 1 KM = 0.621371 miles
miles = kilometers * conversion_factor
print("{:.2f} kilometers is equal to {:.2f} miles.".format(kilometers, miles))


# In[5]:


kilometers = float(input("Enter value in KM :"))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(miles)


# In[7]:


#2
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("{:.1f}°C is equal to {:.1f}°F".format(celsius, fahrenheit))


# In[10]:


#3
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))


# In[11]:


#4
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print("The solutions are {0} and {1}".format(sol1, sol2))


# In[12]:


#5
x = 5
y = 10

print("Before swapping, x = ", x, " and y = ", y)

x, y = y, x

print("After swapping, x = ", x, " and y = ", y)


# In[ ]:




