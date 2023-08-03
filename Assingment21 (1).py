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





# # ASSINGMENT 22
1. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
print(X)


>>> func()
Ans. iNeuron  
# In[14]:


#2. What is the result of the code, and explain?


X = 'iNeuron'
def func():
    X = 'NI!'
    
func()
print(X)


3. What does this code print, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
print(X)


>>> func()
>>> print(X)
Inside the function func, a local variable X is defined and assigned the value 'NI'. This local variable X is distinct from the global variable X defined outside the function. When func() is called, it will print the value of the local variable X, which is 'NI'.

After calling func(), this line will print the value of the global variable X, which is 'iNeuron'. The function func() does not modify the global variable, so its value remains unchanged.

The final result is :  'NI'
                       'iNeuron'4. What output does this code produce? Why?


>>> X = 'iNeuron'
>>> def func():
global X
X = 'NI'


>>> func()
>>> print(X)


Ans : 'NI'
      Becouse The function func() uses the global statement to indicate that the variable X inside the function is referring to the global variable X. Therefore, any changes made to X inside the function affect the global variable X. The value 'iNeuron' assigned to X initially is replaced with the value 'NI' inside the function, and that modified value is printed outside the function.

5. What about this code—what’s the output, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
def nested():
print(X)
nested()


>>> func()
>>> X
NI
iNeron
becouse When func() is called, it defines a local variable X with the value 'NI', and then the nested function nested() is called.
Inside nested(), it prints the value of the local variable X from its parent function func(), which is 'NI'.
After func() finishes executing, print(X) outside the function prints the value of the global variable X, which remains 'iNeuron'. The local variable X inside func() does not affect the global variable.
# In[ ]:


get_ipython().run_line_magic('pinfo', 'explain')


>>> def func():
X = 'NI'
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


>>> func()




The func() function defines a local variable X with the value 'NI'.
Inside func(), the nested function nested() is defined, and it modifies the X variable using the nonlocal keyword, so it affects the variable X from the func() scope.
When func() is called, it calls nested(), which sets the value of X to 'Spam'.
After nested() finishes executing, func() proceeds to the print(X) statement, which prints the modified value of X, which is now 'Spam'.



