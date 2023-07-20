#!/usr/bin/env python
# coding: utf-8

# Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

# In[1]:


class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

# Example usage:
n = 50
generator = DivisibleBySevenGenerator(n)
for num in generator.divisible_by_seven():
    print(num)


# Question 2:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
#     or:2
# to:1

# In[2]:


def compute_word_frequency(input_text):
    # Split the input text into words
    words = input_text.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        # Remove any non-alphanumeric characters from the word
        cleaned_word = ''.join(e for e in word if e.isalnum()).lower()

        # Increment the word frequency in the dictionary
        word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1

    return word_freq

if __name__ == "__main__":
    input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

    # Compute word frequency
    word_freq = compute_word_frequency(input_text)

    # Sort the dictionary by keys alphabetically
    sorted_word_freq = sorted(word_freq.items())

    # Output the result
    for word, freq in sorted_word_freq:
        print(f"{word}:{freq}")


# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# In[3]:


class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

if __name__ == "__main__":
    person1 = Male()
    person2 = Female()

    person1.getGender() 
    person2.getGender()  


# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# In[4]:


def generate_sentences(subjects, verbs, objects):
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}."
                sentences.append(sentence)
    return sentences

if __name__ == "__main__":
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    sentences = generate_sentences(subjects, verbs, objects)

    for sentence in sentences:
        print(sentence)


# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# In[5]:


import zlib

def compress_string(input_string):
    
    input_bytes = input_string.encode('utf-8')
   
    compressed_data = zlib.compress(input_bytes)
    
    return compressed_data

def decompress_string(compressed_data):
   
    decompressed_bytes = zlib.decompress(compressed_data)
    
    decompressed_string = decompressed_bytes.decode('utf-8')
    
    return decompressed_string

if __name__ == "__main__":
    input_string = "hello world!hello world!hello world!hello world!"
    
   
    compressed_data = compress_string(input_string)
  
    print("Compressed data:", compressed_data)
   
    decompressed_string = decompress_string(compressed_data)
    
    print("Decompressed string:", decompressed_string)


# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# 

# In[6]:


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

   
    target_value = 7
    result_index = binary_search(sorted_list, target_value)

    if result_index != -1:
        print(f"Element {target_value} found at index {result_index}.")
    else:
        print(f"Element {target_value} not found in the list.")


# In[ ]:




