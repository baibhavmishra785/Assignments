# -*- coding: utf-8 -*-
"""Assignment 4

1. What exactly is []?
2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Let&#39;s pretend the spam includes the list [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;] for the next three queries.
3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?
4. What is the value of spam[-1]?
5. What is the value of spam[:2]?
Let&#39;s pretend bacon has the list [3.14, &#39;cat,&#39; 11, &#39;cat,&#39; True] for the next three questions.
6. What is the value of bacon.index(&#39;cat&#39;)?
7. How does bacon.append(99) change the look of the list value in bacon?
8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?
9. What are the list concatenation and list replication operators?
10. What is difference between the list methods append() and insert()?
11. What are the two methods for removing items from a list?
12. Describe how list values and string values are identical.
13. What&#39;s the difference between tuples and lists?
14. How do you type a tuple value that only contains the integer 42?
15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?
16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they
contain?
17. How do you distinguish between copy.copy() and copy.deepcopy()?
"""

import logging
logging.basicConfig(filename='assognment4logs.log', level= logging.INFO, format= '%(asctime)s, %(levelname)s, %(name)s, %(message)s')
logging.info('Assignment 4 begins!')

try:
  #1. The empty list value, which is a list value that contains no items.
  #2.
  spam = [2, 4, 6, 8, 10]
  spam[2] = 'hello'
  #3. Answer of spam[int(int('3' * 2) / 11)] will be 8.
  #4. Answer of spam[-1] will be 10.
  #5. Answer of spam[:2] will be [2, 4].
  #6. The index of bacon.index('cat) will be 1.
  #7. After adding bacon.append(99) the new list will be bacon = [3.14, 'cat', 11, 'cat', True, 99]
  #8. bacon.remove('cat') will remove first 'cat' and the updated list will be bacon = [3.14, 11, 'cat', True, 99]
  #9. The operator for list concatenation is +, while the operator for replication is *.
  #10. append() adds an item to the end of a list, whereas . insert() inserts and item in a specified position in the list.
  #11. The methods are remove(), pop() and clear().
  #12. The values that make up a list are called its elements. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.
  #13. The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable. Therefore, it is possible to change a list but not a tuple.
  #14. We can use (42,).
  #15. Using the tuple() built-in function we can do both.
  #16. Variables will contain references to list values rather than list values themselves. But for strings and integer values, variables simply contain the string or integer value.
  #17. A shallow copy creates a new compound object and then adds a reference to the object found in the original. A deep copy creates a new compound object and then adds a reference to the object found in the original. We can copy arbitrary objects (including custom classes) with the copy module.

except Exception as e:
  logging.info('There is an error')
  print('This is suspicious.')

logging.info('Assignment 4 is done.')
