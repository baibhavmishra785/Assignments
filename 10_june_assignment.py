# -*- coding: utf-8 -*-
"""10 june assignment

1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
example of each.
2. How can you pass arguments to a function in Python? Explain the difference between positional
arguments and keyword arguments.
3. What is the purpose of the return statement in a function? Can a function have multiple return
statements? Explain with an example.
4. What are lambda functions in Python? How are they different from regular functions? Provide an
example where a lambda function can be useful.
5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
scope and global scope.
6. How can you use the "return" statement in a Python function to return multiple values?
7. What is the difference between the "pass by value" and "pass by reference" concepts when it
comes to function arguments in Python?
8. Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)
b. Exponential function (exp(x))
c. Power function with base 2 (2
x
)

d. Square root
9. Create a function that takes a full name as an argument and returns first name and last name.
"""

import logging
logging.basicConfig(filename='10juneassignmentlogs', level = logging.INFO, format- '%(asctime)s, %(name)s, %(message)s')
logging.info('10 june assignment start')

try:
  #1. Built-in functions are pre-defined functions provided by Python as part of its standard library.
     # Example: # Using a built-in function
    #numbers = [1, 2, 3, 4, 5]
    #length = len(numbers)
    #print(length)  # Output: 5
  # User-defined functions are created by users to perform specific tasks or encapsulate a block of reusable code.
    #Example : # Defining a user-defined function
     def calculate_square(num):
        return num ** 2

   # Using the user-defined function
    result = calculate_square(5)
    print(result)
    # Output: 25

  #2. Positional arguments are passed to a function based on their position or order.
    #Example :
    def greet(name, age):
      print(f"Hello, {name}! You are {age} years old.")

      # Calling the function with positional arguments
      greet("Alice", 25)

  # Keyword arguments are passed to a function using the name of the parameter they correspond to.
    #Example :
    def greet(name, age):
      print(f"Hello, {name}! You are {age} years old.")

      # Calling the function with keyword arguments
      greet(name="Bob", age=30)

  #3. The return statement in a function serves the purpose of exiting the function and returning a value or values back to the caller. It allows a function to compute a result or perform a task and provide the output to the code that called the function. The return statement is used to explicitly specify what value or values should be returned.

     #A function can have multiple return statements. However, as soon as a return statement is encountered during the execution of the function, the function immediately exits, and the specified value is returned. This means that any code or statements after the return statement will not be executed.

     def multiply(a, b):
      if a == 0 or b == 0:
        return 0
      else:
        return a * b


        result1 = multiply(5, 7)
        print(result1)  # Output: 35

        result2 = multiply(0, 10)
        print(result2)  # Output: 0

    # In this example, the multiply() function takes two arguments, a and b. If either of the arguments is zero, the function immediately returns zero using a return statement. If both arguments are non-zero, the function computes their product using the multiplication operator and returns the result.

  #4. Lambda functions, also known as anonymous functions, are small, one-line functions in Python that are defined without a name. They are typically used when a small, single-purpose function is needed and defining a named function would be unnecessary or cumbersome. Lambda functions are created using the lambda keyword.

    #Example:
      def square(x):
        return x ** 2

        square_lambda = lambda x: x ** 2

        result1 = square(5)
        print(result1)
        # Output: 25

        result2 = square_lambda(5)
        print(result2)
        # Output: 25

    #5. In Python, scope refers to the region or context in which a variable or name can be accessed. It determines the visibility and lifetime of variables and other objects within a program. The concept of scope applies to functions in Python, and there are two main types of scopes: local scope and global scope.

       # Local scope refers to the portion of a program where a variable is defined within a function.
       # Global scope refers to the top-level or outermost scope of a program or module.

    #6. In Python, you can use the return statement in a function to return multiple values by returning them as a tuple, list, or any other suitable data structure. Few approaches to accomplish this areReturn as a Tuple, Return as a List, Return as a Dictionary

    #7. In Python, the concept of "pass by value" and "pass by reference" can be a bit nuanced. Python uses a mechanism called "passing arguments by object reference." This means that when you pass an argument to a function, a reference to the object is passed rather than the actual value. However, the behavior can resemble both "pass by value" and "pass by reference" depending on the type of the object being passed.

    #8.
    import math

    def perform_operations(value):
      result = {}

      result['log'] = math.log(value)

      result['exp'] = math.exp(value)

      result['power'] = math.pow(2, value)

      result['sqrt'] = math.sqrt(value)

      return result

    #9.
    def get_first_and_last_name(full_name):
      names = full_name.split()
      first_name = names[0]
      last_name = names[-1]
      return first_name, last_name


except Exception as e:
  print('There is an issue.')

logging.info('10 june assignment is over.')
