# -*- coding: utf-8 -*-
"""Assignment 3

1. Why are functions advantageous to have in your programs?
2. When does the code in a function run: when it&#39;s specified or when it&#39;s called?
3. What statement creates a function?
4. What is the difference between a function and a function call?
5. How many global scopes are there in a Python program? How many local scopes?
6. What happens to variables in a local scope when the function call returns?
7. What is the concept of a return value? Is it possible to have a return value in an expression?
8. If a function does not have a return statement, what is the return value of a call to that function?
9. How do you make a function variable refer to the global variable?
10. What is the data type of None?
11. What does the sentence import areallyourpetsnamederic do?
12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
13. What can you do to save a programme from crashing if it encounters an error?
14. What is the purpose of the try clause? What is the purpose of the except clause?
"""

import logging
logging.basicConfig(filename='assignment3logs.log', level = logging.INFO, format= '%(asctime)s, %(name)s, %(level)s, %(message)s')
logging.info('Assignment 3 begins!')

#1. To avoid writing the same code multiple times we use functions. Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.
  #2. The code in a function executes when the function is called, not when the function is defined.
  #3. def will create a function.
  #4. A function is a piece of code which enhanced the reusability and modularity of your program. It means that piece of code need not be written again. A function call means invoking or calling that function. Unless a function is called there is no use of that function.
  #5. There's only one global Python scope per program execution. This scope remains in existence until the program terminates and all its names are forgotten. Otherwise, the next time you were to run the program, the names would remember their values from the previous run.
  #6. When the execution of the function terminates (returns), the local variables are destroyed.
  #7. A return is a value that a function returns to the calling script or function when it completes its task. A return value can be any one of the four variable types: handle, integer, object, or string. The type of value your function returns depends largely on the task it performs.
  #8. If no return statement appears in a function definition, control automatically returns to the calling function after the last statement of the called function is executed. In this case, the return value of the called function is undefined.
  #9. By using the global keywords we can do it.
  #10. None is a data type of its own (NoneType) and only None can be None.
  #11. That import statement imports a module named areallyourpetsnamederic.
  #12. spam.bacon()/
  #13. error handling can be used to notify the user of why the error occurred and gracefully exit the process that caused the error.
  #14. The try block lets you test a block of code for errors. The except block lets you handle the error.

logging.info('Assignment 3 done!')
