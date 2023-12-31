# -*- coding: utf-8 -*-
"""11 june assignment

1. What is a lambda function in Python, and how does it differ from a regular function?
2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
them?
3. How are lambda functions typically used in Python? Provide an example use case.
4. What are the advantages and limitations of lambda functions compared to regular functions in
Python?
5. Are lambda functions in Python able to access variables defined outside of their own scope?
Explain with an example.
6. Write a lambda function to calculate the square of a given number.
7. Create a lambda function to find the maximum value in a list of integers.
8. Implement a lambda function to filter out all the even numbers from a list of integers.
9. Write a lambda function to sort a list of strings in ascending order based on the length of each
string.
10. Create a lambda function that takes two lists as input and returns a new list containing the
common elements between the two lists.
11. Write a recursive function to calculate the factorial of a given positive integer.
12. Implement a recursive function to compute the nth Fibonacci number.
13. Create a recursive function to find the sum of all the elements in a given list.
14. Write a recursive function to determine whether a given string is a palindrome.
15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
"""

import logging
logging.basicConfig(filename='11juneassignmentlogs', level = logging.INFO, format- '%(asctime)s, %(name)s, %(message)s')
logging.info('11 june assignment start')

try:
  #1. A lambda function is an anonymous function (i.e., defined without a name) that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression. Note that, unlike a normal function, we don't surround the parameters of a lambda function with parentheses.
  #2. Python lambda can be used with multiple arguments and these arguments are used in evaluating an expression to return a single value. A Python lambda function is used to execute an anonymous function, an anonymous meaning function without a name.
  #3. In Python, we generally use Lambda Functions as an argument to a higher-order function (a function that takes in other functions as arguments). For Example, These are used together with built-in functions like filter(), map(), and reduce(), etc, which we will discuss later in this article.
  #4. Lambda helps you use a function only once, and hence, avoids cluttering up the code with function definitions. In short, Python's lambda keyword lets you define a function in a single line of code and use it immediately.
     #The disadvantages of lambda function are Lambda functions can have only one expression, Lambda functions cannot have a docstring, Many times lambda functions make code difficult to read.
  #5. Yes, lambda functions in Python can access variables defined outside of their own scope. They can access variables from the surrounding scope, including global variables and variables defined in the enclosing function. Here's an example to illustrate this behavior:
  def outer_function():
    message = "Hello"


    greet = lambda name: f"{message}, {name}!"

    return greet
    greeter = outer_function()

    result = greeter("John")
    print(result)
    # Output: Hello, John!

  #6.
  square = lambda x: x**2
  result = square(5)
  print(result)
  # Output: 25

  #7.
  find_max = lambda lst: max(lst)
  numbers = [10, 5, 8, 20, 3]
  result = find_max(numbers)
  print(result)
  # Output: 20

  #8.
  filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  result = filter_even(numbers)
  print(result)
  # Output: [2, 4, 6, 8, 10]

  #9.
  sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))
  strings = ["apple", "banana", "cherry", "date", "elderberry"]
  result = sort_by_length(strings)
  print(result)
  # Output: ['date', 'apple', 'cherry', 'banana', 'elderberry']

  #10.
  find_common_elements = lambda list1, list2: list(filter(lambda x: x in list2, list1))
  list1 = [1, 2, 3, 4, 5]
  list2 = [4, 5, 6, 7, 8]
  result = find_common_elements(list1, list2)
  print(result)
  # Output: [4, 5]

  #11.
  def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

  result = factorial(5)
  print(result)
  # Output: 120

  #12.
  def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

  result = fibonacci(6)
  print(result)
  # Output: 8

  #13.
  def sum_list_elements(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list_elements(lst[1:])

  numbers = [1, 2, 3, 4, 5]
  result = sum_list_elements(numbers)
  print(result)
  # Output: 15

  #14.
  def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        first = string[0]
        last = string[-1]
        if first == last:
            return is_palindrome(string[1:-1])
        else:
            return False

  result1 = is_palindrome("radar")
  print(result1)
  # Output: True

  result2 = is_palindrome("hello")
  print(result2)
  # Output: False

  #15.
  def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

  result = gcd(48, 36)
  print(result)
  # Output: 12

except Exception as e:
  print('There is a problem.')

logging.info('11 june assignment is done.')
