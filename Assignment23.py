#!/usr/bin/env python
# coding: utf-8
1. What is the result of the code, and why?
>>> def func(a, b=6, c=8):
print(a, b, c)
>>> func(1, 2)
Ans. 1,2,8
Here, you are calling the func function with two arguments: 1 for a and 2 for b. Since you didn't provide a value for c, it will take its default value, which is 8.
The function func will print the values of a, b, and c on the same line, separated by spaces. The output will show 1 2 8, which are the values of a, b, and c respectively.2. What is the result of this code, and why?
>>> def func(a, b, c=5):
print(a, b, c)
>>> func(1, c=3, b=2)
 Ans.:1 2 3 a function named func with three parameters: a, b, and c. The parameter c has a default value of 5.
      In this function call, we are passing three arguments: 1 for a, 3 for c, and 2 for b. Note that we used keyword arguments to specify the values for c and b. When using keyword arguments, the order of the arguments does not matter, as long as you explicitly mention the parameter names.
The function func will print the values of a, b, and c on the same line, separated by spaces. The output will show 1 2 3, which are the values of a, b, and c respectively.3. How about this code: what is its result, and why?
>>> def func(a, *pargs):
print(a, pargs)
>>> func(1, 2, 3)

Ans. 1, (2, 3)
In this function call, we are passing three arguments: 1, 2, and 3. Since *pargs collects all the additional positional arguments beyond the first one (a), the values 2 and 3 will be packed into a tuple. The function will treat a as 1, and pargs as (2, 3).
The function func will print 1 for the value of a, and (2, 3) for the value of pargs. The (2, 3) is a tuple containing the additional positional arguments provided to the function after a.4. What does this code print, and why?
>>> def func(a, **kargs):
print(a, kargs)
>>> func(a=1, c=3, b=2)
Ans.: 1 {'c': 3, 'b': 2}
    In this code, the function func has two parameters: a and **kargs. The double asterisks ** before kargs in the parameter list allows the function to accept a variable number of keyword arguments, which will be collected into a dictionary.
    In this function call, we are passing three keyword arguments: a=1, c=3, and b=2. The function will treat a as 1, and the rest of the keyword arguments (c=3 and b=2) will be packed into a dictionary with their respective keys and values.
The function func will print 1 for the value of a, and {'c': 3, 'b': 2} for the value of kargs. The {'c': 3, 'b': 2} is a dictionary containing the keyword arguments provided to the function (excluding the one already associated with named parameters like a). The keys of the dictionary are the parameter names, and the values are the corresponding values passed to the function.
    5. What gets printed by this, and explain?
>>> def func(a, b, c=8, d=5): print(a, b, c, d)
>>> func(1, *(5, 6))

Ans : 1 5 6 5
    In this code, the function func has four parameters: a, b, c, and d. The * before (5, 6) in the function call indicates that the tuple (5, 6) is being unpacked and its elements are passed as individual arguments to the function.
Here, we are passing three arguments to the function: 1, 5, and 6. The values 5 and 6 are unpacked from the tuple (5, 6) and passed as individual arguments to match the b and c parameters of the function. The parameter d will take its default value, which is 5
The function func will print 1 for the value of a, 5 for the value of b (unpacked from (5, 6)), 6 for the value of c (also unpacked from (5, 6)), and 5 for the value of d (default value).