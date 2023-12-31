# -*- coding: utf-8 -*-
"""Assignment 1

1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
&#39;hello&#39;
-87.8
-
/
+
6

2. What is the difference between string and variable?

3. Describe three different data types.

4. What is an expression made up of? What do all expressions do?
5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?
6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

7. What should the values of the following two terms be?
&#39;spam&#39; + &#39;spamspam&#39;
&#39;spam&#39; * 3

8. Why is eggs a valid variable name while 100 is invalid?

9. What three functions can be used to get the integer, floating-point number, or string
version of a value?
10. Why does this expression cause an error? How can you fix it?
&#39;I have eaten &#39; + 99 + &#39; burritos.&#39;
"""

import logging
logging.basicConfig(filename='assignment1.log', level=logging.INFO, format= '%(asctime)s, %(levelname)s, %(message)s')
logging.info('Assignment 1 begins.')

#1. 'hello', -87.8, 6 are values. *, -, /, + are variables.

#2. Strings are sequences of characters that are used for conveying textual information. Variables are symbols that you can use to store data in a program.

#3. The three different data types in python are string, int, float.

#4. A combination of operands and operators is called an expression. The expression in Python produces some value or result after being interpreted by the Python interpreter. An expression in Python is a combination of operators and operands.

#5. A statement in Python is not evaluated for some results. An expression in Python is evaluated for some results. The execution of a statement changes the state of the variable. The expression evaluation does not result in any state change.

#6. bacon = 22 bacon + 1 = 23

#7. 'spam' + 'spamspam' 'spam' * 3 = spamspamspamspamspamspamspamspamspamspam

#8. Eggs is a valid variable name while 100 is invalid because variable name cannot begin with a number.

#9.  int(), float(), and str() functions will evaluate to the integer, floating-point number, and string.

#10. The expression 'I have eaten ' + 99 + ' burritos.' causes an error because it involves attempting to concatenate a string ('I have eaten ') with an integer (99) without converting the integer to a string first. In many programming languages, including Python, you cannot directly concatenate different data types.

#To fix this error, you need to convert the integer to a string before concatenating it with the other strings.
'I have eaten ' + str(99) + ' burritos.'

logging.info('Assignment 1 is done.')
