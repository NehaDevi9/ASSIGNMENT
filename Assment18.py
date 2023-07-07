#!/usr/bin/env python
# coding: utf-8

# 1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
# 

# In[ ]:





# 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
# 

# 3. Using the interpreter, explicitly import and call the hours() function from zoo.
# 

# In[ ]:


from zoo import hours

hours()


# 5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out

# In[7]:


plain_dict = {'a':1 , 'b':2 , 'c':3}
print(plain_dict)


# 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[3]:


from collections import OrderedDict

pairs = [('a', 1),('b',2),('c',3)]
fancy = OrderedDict(pairs)
print(fancy)


# 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[1]:


from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('somthing for a')
print(dict_of_lists['a'])


# In[ ]:





# In[ ]:





# In[ ]:





# 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
# 

# In[2]:


class Thing:
    pass

example = Thing()

print(Thing)
print(example)


# 2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.

# In[3]:


class Thing2:
    letters = 'abc'
    
print(Thing2.letters)


# 3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?

# In[4]:


class Thing3:
    def __init__(self):
        self.letters = 'xyz'
        
example = Thing3()

print(example.letters)


# 4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.

# In[1]:


class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
        
hydrogen = Element('Hydrogen','H',1)


# 5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.

# In[6]:


class Element:
    pass


element_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}


hydrogen = Element()
hydrogen.__dict__.update(element_dict)


# 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
# 

# In[7]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("Name:", self.name)
        print("Symbol:", self.symbol)
        print("Number:", self.number)

hydrogen = Element("Hydrogen", "H", 1)
hydrogen.dump()


# 7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.

# In[1]:


class Element:
    def __str__(self):
        return f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}"

# Creating a dictionary with keys and values
element_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

# Creating an object from the Element class using the dictionary
hydrogen = Element()
hydrogen.__dict__.update(element_dict)

# Printing the hydrogen object before the changes
print(hydrogen)

# Updating the Element class with the str method
class Element:
    def __str__(self):
        return f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}"

# Creating a new hydrogen object
hydrogen = Element()
hydrogen.__dict__.update(element_dict)

# Printing the hydrogen object after the changes
print(hydrogen)


# 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# In[3]:


class Element:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number


# 9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.

# In[6]:


class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


# Creating objects from the classes
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

# Printing what each object eats
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())


# 10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
# 

# In[9]:


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print("The robot's components:")
        print("Laser:", self.laser.does())
        print("Claw:", self.claw.does())
        print("Smartphone:", self.smartphone.does())


# Creating an instance of the Robot class
robot = Robot()

# Calling the does() method of the Robot object
robot.does()


# In[ ]:




