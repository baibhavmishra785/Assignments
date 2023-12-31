# -*- coding: utf-8 -*-
"""Assignment6

Q.1. What are keywords in python? Using the keyword library, print all the python keywords.

Q.2. What are the rules to create variables in python?

Q.3. What are the standards and conventions followed for the nomenclature of variables in
python to improve code readability and maintainability?

Q.4. What will happen if a keyword is used as a variable name?

Q.5. For what purpose def keyword is used?

Q.6. What is the operation of this special character ‘\’?

Q.7. Give an example of the following conditions:
(i) Homogeneous list
(ii) Heterogeneous set
(iii) Homogeneous tuple

Q.8. Explain the mutable and immutable data types with proper explanation & examples.

Q.9. Write a code to create the given structure using only for loop.
*
***
*****
*******
*********

Q.10. Write a code to create the given structure using while loop.
|||||||||
|||||||
|||||
|||
|
"""

import logging
logging.basicConfig(filename='Assignment6logs', level = logging.INFO, format='%(message)s, %(asctime)s, %(name)s')
logging.info('Assignment 6 begins.')

try:
  #!. Keywords are special terms which are used to perform specific tasks. To print the list of all keywords, we use "keyword. kwlist", which can be used after importing the "keyword" module, it returns a list of the keyword available in the current Python version.
  #2. Rules for declaring a variable are :
     #i. A variable name must start with a letter or the underscore character, A variable name cannot start with a number.
     #ii. A variable name can only contain alpha-numeric characters and underscores.
     #iii. Variable names are case-sensitive.
  #3. Instance variable names should follow the lowercase convention. Have the underscore as a separator while naming a multi-word instance variable. Begin a non-public instance variable name with a single underscore. Use two consecutive underscores at the beginning of an instance variable.
  #4. Keywords define the language's syntax rules and structure, and they cannot be used as variable names.
  #5. The def keyword is used to define a function.
  #6. '\' is used as a division operator.
  #7. i. Homogenous list : numbers = [1, 2, 3, 4, 5]
     #ii. Heterogenious set : my_set = {1, 'hello', 3.14, True}
     #iii. Homogenous tuple : fruits = ('apple', 'banana', 'orange', 'kiwi')
  #8. Immutable data types are those whose values cannot be modified once they are created. Any attempt to modify an immutable object results in creating a new object. Immutable objects are useful when you want to ensure data integrity and prevent unintentional modifications. Examples of immutable data types in Python include:
      #Numbers: int, float, complex
      #Strings: str
      #Tuples: tuple
      #Example : number = 5
                #name = "Alice"
                #point = (2, 4)
     #Mutable data types are those that can be modified after they are created. It means you can change the value or state of an object without creating a new object. Examples of mutable data types in Python include:
     #Lists: list
     #Sets: set
     #Dictionaries: dict
     #Example : numbers = [1, 2, 3, 4]
               #student = {"name": "Bob", "age": 20}

  #9.
  rows = 5

# Creating the structure using for loops
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

    #10.
    structure = "||||||||| ||||||| ||||| ||| |"

# Creating the structure using a while loop
index = 0
while index < len(structure):
    print(structure[:index+1])
    index += 1

except Exception as e:
  print('This is not good.')

logging.info('Assignment 6 is over.')
