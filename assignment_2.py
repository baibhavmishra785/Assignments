# -*- coding: utf-8 -*-
"""Assignment 2

1.What are the two values of the Boolean data type? How do you write them?
2. What are the three different types of Boolean operators?
3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
4. What are the values of the following expressions?
(5 &gt; 4) and (3 == 5)
not (5 &gt; 4)
(5 &gt; 4) or (3 == 5)
not ((5 &gt; 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
5. What are the six comparison operators?
6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print(&#39;eggs&#39;)
if spam &gt; 5:
print(&#39;bacon&#39;)
else:
print(&#39;ham&#39;)
print(&#39;spam&#39;)
print(&#39;spam&#39;)
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

9.If your programme is stuck in an endless loop, what keys you’ll press?
10. How can you tell the difference between break and continue?
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.
13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
"""

import logging
logging.basicConfig(filename='assignment2.log', level=logging.INFO, format= '%(asctime)s, %(levelname)s, %(message)s')
logging.info('Assignment 2 begins.')

try:
  #1. The two values of the Boolean data type are True and False. Here's an example of how you would write them in Python:
  my_variable = True
  another_variable = False

  #2. The 3 different Boolean operators are AND, OR, NOT

  #3. There are three possible tryth tables, Logical AND, Logical OR, Logical NOT.

  #4.  (5 > 4) and (3 == 5) not (5 > 4) (5 > 4) or (3 == 5) not ((5 > 4) or (3 == 5)) (True and True) and (True == False) (not False) or (not True) - invalid syntax.

  #5. six comparision operators includes - less than, greater than, less than or equal to, greater than or equal to, equal to, and not equal to.

  #6. Equal to (==) operator: The equal to operator is used to compare two values for equality. It checks if the values on both sides are equal and returns True if they are, and False otherwise.
      #Assignment (=) operator: The assignment operator is used to assign a value to a variable. It assigns the value on the right side to the variable on the left side.

  #7. Block 1: This block is triggered by the if statement and executes the print('eggs') statement if the condition spam == 10 evaluates to True.

      #Block 2: This block is part of an if-else statement. If the condition spam > 5 is True, it executes the print('bacon') statement. Otherwise, it executes the print('ham') statement.

      #Block 3: This block consists of two consecutive print statements. They are executed sequentially and are not conditional on any specific condition.

#8.
  spam = input(int())
  if spam == 1:
    print('Hello!')
  if spam == 2:
    print('Howdy!!')
  else:
    print('Greetings!!!')

#9. If your programme is stuck in an endless loop please press interrupt option.
  #10. Break statement will interrupt the process whereas continue statement will allow the process to go on.
  #11. range(10) will print from 0-9, range(0,10) will print from 1-9, and range (0,10,1) will print from 1-9 with a jump of 1

#12. Using a for loop
  for num in range(1, 11):
    print(num)

  # Using a while loop
  num = 1
  while num <= 10:
    print(num)
    num += 1

#13. After importing the spam module, you can call the bacon() function using the dot notation.
  import spam
  spam.bacon()

logging.info('Assignment 2 done.')

except Exception as e:
  print("This is suspicious!")
