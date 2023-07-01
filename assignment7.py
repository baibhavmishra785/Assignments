# -*- coding: utf-8 -*-
"""Assignment7

Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
and store the results in variables. Then print the data in the following format by calling the
variables:
First variable is __ & second variable is __.
Addition: __ + __ = __
Subtraction: __ - __ = __
Multiplication: __ * __ = __
Division: __ / __ = __

Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii) ‘**’ & ‘^’

Q.3. List the logical operators.

Q.4. Explain right shift operator and left shift operator with examples.

Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
present in the list or not.
"""

import logging
logging.basicConfig(filename='Assignment7logs', level= logging.INFO, format= '%(asctime)s, %(name)s, %(message)s')
logging.info('Assignment 7 started.')

try:
  #1.
  x = 1
  y = 2
  a = x + y
  b = x - y
  c = x*y
  d = x/y
  print('First variable is ', x)
  print('Second variable is ', y)
  print('Addition of', x, '+', y, '=', a)
  print('Subtraction : ', x, '-', y, '=', b)
  print('Multiplication : ', x, '*', y, '=', c)
  print('Division : ', x, '/', y, '=', d)

  #2. The '/' operator performs floating-point division, which means it returns the exact quotient (including decimal places) of the division operation.
  #   The '//' operator performs floor division, also known as integer division. It returns the floor value of the division operation, discarding any decimal places.
  #   The '**' operator is used for exponentiation in Python. It raises the left operand to the power of the right operand.
  #   The '^' operator, in Python, is not used for exponentiation. Instead, it is the bitwise XOR operator. It performs the XOR operation on the binary representations of the operands. It is used for bitwise operations.

  #3. There are 3 logical operators &&(AND), ~(NOT), ||(OR).

  #4. The left shift operator (<<) shifts the bits of a number to the left by a specified number of positions.
  # Example: x = 2
    #        y = 3

    #        result = x << y
    #        print(result)
    #    Output: 16 (Binary: 10000)
    # The right shift operator (>>) shifts the bits of a number to the right by a specified number of positions.
    #  Example : x = 8  # Binary: 1000
    #            y = 2

    #            result = x >> y
    #            print(result)
    #   Output: 2 (Binary: 10)

  #5.
  l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  for i in l:
    if i == 10:
      print('Yes, 10 is there.')
    else:
      print('10 is not there.')

except Exception as e:
  print('There is an issue')

logging.info('Assignment 7 is over.')
