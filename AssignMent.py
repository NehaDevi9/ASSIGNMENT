#!/usr/bin/env python
# coding: utf-8

# Write a Python program to print &quot;Hello Python&quot;?
# 2. Write a Python program to do arithmetical operations addition and division.?
# 3. Write a Python program to find the area of a triangle?
# 4. Write a Python program to swap two variables?
# 5. Write a Python program to generate a random number?

# In[2]:


#Write a Python program to print Hello Python?
print("Hello")


# In[4]:


# 2. Write a Python program to do arithmetical operations addition and division.?
a = 10
b = 5
print(a+b)
print(a/b)


# In[6]:


#3. Write a Python program to find the area of a triangle?
h = float(input("Enter a height of the triangle : "))
b = float(input("Enter a base of the triangle : "))
area = (0.5 * b *h)
print("area of triangle = ",area)


# In[8]:


#4. Write a Python program to swap two variables?
b = int(input("Enter value for b: "))
a =  int(input("Enter value for a: "))

a, b = b, a

print("The value of a after swapping: ", a)
print("The value of b after swapping: ",b)


# In[11]:


#5. Write a Python program to generate a random number?
import random

print(random.randint(0,9))


# 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
# the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
# [1980, 1981, 1982, 1983, 1984, 1985].

# In[1]:


year_list = [1997, 1998, 1999, 2000, 2001, 2002]


# In[3]:


year_list


# In which year in years_list was your third birthday? Remember, you were 0 years of age for your
# first year.

# In[10]:


year_list = [1997, 1998, 1999, 2000, 2001, 2002]
birth_year = 1997
fifth_year_birthday = birth_year + 5
year_list = list(range (birth_year , fifth_year_birthday))
third_year_birthday = birth_year + 3
index_of_year_of_third_birthday = third_year_birthday - year_list[0]
print("The year of my third birthday was", year_list[index_of_year_of_third_birthday])



# 3.In the years list, which year were you the oldest?
# 

# In[11]:


year_list = [1997, 1998, 1999, 2000, 2001, 2002]
oldest_year = max(year_list)
print("The oldest year is :", oldest_year)


# 4. Make a list called things with these three strings as elements: "mozzarell", "cinderella",
# "salmonella".

# In[12]:


things = ["mozzarella", "cinderella", "salmonella"]


# In[13]:


things


# 5. Capitalize the element in things that refers to a person and then print the list. Did it change the
# element in the list?

# In[14]:


things = ["mozzarella", "cinderella", "salmonella"]
person_index = 1
things[person_index] = things[person_index].capitalize()

print(things)


# 
# Did it change the element in the list?
# As you can see, the element "cinderella" in the original list has been capitalized to "Cinderella". Yes, the element in the list has been changed.

# 6. Make a surprise list with the elements "Groucho" ,"Chico" ,"Harpo".

# In[17]:


surprise = ["Groucho" ,"Chico" ,"Harpo"]


# In[18]:


surprise


# 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[ ]:


surprise = ["Groucho", "Chico", "Harpo"]
last_element = surprise[-1]
lowercase_last_element = last_element.lower()
reversed_last_element = lowercase_last_element[::-1]
capitalized_reversed_last_element = reversed_last_element.capitalize()

print(capitalized_reversed_last_element)


# In[7]:


surprise = ["Groucho" ,"Chico" ,"Harpo"]
last_ele =  surprise[-1] 
lowercase_last_ele = last_ele.lower()
reversed_last_ele = lowercase_last_ele[::-1] 
capitalized_reversed_last_ele = reversed_last_ele.capitalize()
print(capitalized_reversed_last_ele)
print(surprise)


# In[2]:


print(reversed_last_ele)


# In[3]:


print(lowercase_last_ele)


# In[4]:


print(last_ele)


# In[6]:


print(last_ele, lowercase_last_ele, reversed_last_ele, capitalized_reversed_last_ele )


# In[8]:


surprise = ["Groucho", "Chico", "Harpo"]
last_element = surprise[-1]
lowercase_last_element = last_element.lower()
reversed_last_element = lowercase_last_element[::-1]
capitalized_last_element = reversed_last_element.capitalize()
surprise[-1] = capitalized_last_element

print(surprise)


# 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
# chien, cat is chat, and walrus is morse.

# In[9]:


e2f = { "dog ": "chien",
        "cat" : "chat",
        "walrus" :" morse"}
print(e2f)


# 9. Write the French word for walrus in your three-word dictionary e2f.

# In[10]:


e2f =  { "dog ": "chien",
        "cat" : "chat",
        "walrus" :" morse"}
french_word_for_walrus = e2f["walrus"]
print(french_word_for_walrus)


# 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[16]:


e2f={ "dog ": "chien",
        "cat" : "chat",
        "walrus" :" morse"}
f2e = {}

for english,french in e2f.items():
    f2e[french] = english


# In[17]:


print(f2e)


# 11. Print the English version of the French word chien using f2e.

# In[18]:


e2f = {'dog': 'chien',
      'cat': 'chat',
      'walrus': 'horse'} 
f2e = {}
for english , french in e2f.items():
    f2e[french] = english
    
for_chien = f2e['chien']
print(for_chien)


# 12. Make and print a set of English words from the keys in e2f.

# In[19]:


e2f = {'dog': 'chien',
      'cat': 'chat',
      'walrus': 'horse'} 
english_word = set(e2f.keys())


# In[20]:


print(english_word)


# 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: &#39;animals&#39;, &#39;plants&#39;,
# and &#39;other&#39;. Make the &#39;animals&#39; key refer to another dictionary with the keys &#39;cats&#39;, &#39;octopi&#39;, and
# &#39;emus&#39;. Make the &#39;cats&#39; key refer to a list of strings with the values &#39;Henri&#39;, &#39;Grumpy&#39;, and &#39;Lucy&#39;.
# Make all the other keys refer to empty dictionaries.

# In[21]:


life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {} },'plants': {}, 'other': {}}

print(life)


# 14. Print the top-level keys of life.

# In[23]:


life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {} },'plants': {}, 'other': {}}

top_level_key = life.keys()


# In[24]:


print(top_level_key)


# 15. Print the keys for life[animal].

# In[29]:


life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {} },'plants': {}, 'other': {}}
animal_keys = life['animals'].keys()


# In[30]:


print(animal_keys)


# Print the values for life['animal']['cats']

# In[35]:


cats_value = life['animals']['cats']


# In[36]:


print(cats_value)


# In[ ]:




