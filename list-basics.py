Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-2.py ====
>>> dir(help)
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list1 = [1,2,3,'hello',True, [1,2,4]]
>>> list1.append(10)
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10]
>>> list1.append('bye')
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye']
>>> list1.extend(100)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list1.extend(100)
TypeError: 'int' object is not iterable
>>> list1.extend([100])
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100]
>>> list1.extend(['python'])
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python']
>>> list1.append([43,54,'abc'])
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc']]
>>> list2 = [23,34,43]
>>> for i in range(list2):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for i in range(list2):
TypeError: 'list' object cannot be interpreted as an integer
>>> for i in range(len(list2)):
	print(i)

	
0
1
2
>>> for i in range(len(list2)):
	print(list2[i])

	
23
34
43
>>> for i in list2:
	print(i)

	
23
34
43
>>> for i in list2:
	list1.append(i)

	
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43]
>>> list1.extend(['abcd','xyz',100])
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100]
>>> list1.append(['abcd','xyz',100])
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list1.append(12,23)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list1.append(12,23)
TypeError: append() takes exactly one argument (2 given)
>>> list2 = list1
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list2
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list3 = list1.copy()
>>> list3
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list2.append(99)
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list2
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list3
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list3
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list2
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> id(list1) == id(list2)
True
>>> id(list1) == id(list3)
False
>>> list1[0]
1
>>> list1[5]
[1, 2, 4]
>>> list1[5][0]
1
>>> list1[10][2]
'abc'
>>> list1[10].append('ram')
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list2
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list3
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> id(list1[10])
4548373320
>>> id(list2[10])
4548373320
>>> id(list3[10])
4548373320
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list1[10]
[43, 54, 'abc', 'ram']
>>> list1[10].append('shyam')
>>> list1
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram', 'shyam'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list2
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram', 'shyam'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list3
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram', 'shyam'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100]]
>>> list4
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list4.count('abcd')
1
>>> list4.count(1)
2
>>> list4.count(43)
1
>>> list4.count(100)
2
>>> id(list1[-2]) == id(list4[-2])
False
>>> list4.count(2)
1
>>> list4.count(1)
2
>>> list4.append([1,2,3,4])
>>> list4
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99, [1, 2, 3, 4]]
>>> list4.count(1)
2
>>> list4.append(1)
>>> list4
[1, 2, 3, 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99, [1, 2, 3, 4], 1]
>>> list4.count(1)
3
>>> list4.index(1)
0
>>> list4.index(1, 1)
4
>>> int(True)
1
>>> list4.count([1,2,4])
1
>>> list4.index(1, 5)
20
>>> list4.index(10000)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    list4.index(10000)
ValueError: 10000 is not in list
>>> list4[2] = 'hello
SyntaxError: EOL while scanning string literal
>>> list4[2] = 'hello'
>>> list4
[1, 2, 'hello', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99, [1, 2, 3, 4], 1]
>>> list4.insert(2) = 'new'
SyntaxError: can't assign to function call
>>> list4.insert(2, 'new')
>>> list4
[1, 2, 'new', 'hello', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99, [1, 2, 3, 4], 1]
>>> list4.pop()
1
>>> list4.pop()
[1, 2, 3, 4]
>>> list4
[1, 2, 'new', 'hello', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, ['abcd', 'xyz', 100], 99]
>>> list4.pop(-2)
['abcd', 'xyz', 100]
>>> list4
[1, 2, 'new', 'hello', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc', 'ram'], 23, 34, 43, 'abcd', 'xyz', 100, 99]
>>> list4.pop(11,-1)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    list4.pop(11,-1)
TypeError: pop() takes at most 1 argument (2 given)
>>> list4.pop([11,-1])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    list4.pop([11,-1])
TypeError: 'list' object cannot be interpreted as an integer
>>> del list4[11][-1]
>>> list4
[1, 2, 'new', 'hello', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, 99]
>>> list4.remove('hello')
>>> list4
[1, 2, 'new', 'hello', True, [1, 2, 4], 10, 'bye', 100, 'python', [43, 54, 'abc'], 23, 34, 43, 'abcd', 'xyz', 100, 99]
>>> list4.remove('hello')
>>> list4.remove('hello')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    list4.remove('hello')
ValueError: list.remove(x): x not in list
>>> list4.remove('abc')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    list4.remove('abc')
ValueError: list.remove(x): x not in list
>>> list4.reverse()
>>> list4
[99, 100, 'xyz', 'abcd', 43, 34, 23, [43, 54, 'abc'], 'python', 100, 'bye', 10, [1, 2, 4], True, 'new', 2, 1]
>>> list4.sort()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    list4.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> list5 = [4,23,65,34,5,6,888,098876]
SyntaxError: invalid token
>>> list5 = [4,23,65,34,5,6,888,98876]
>>> list5.sort()
>>> list5
[4, 5, 6, 23, 34, 65, 888, 98876]
>>> list5 = [4,23,65,34,5,6,888,98876]
>>> list5.sort(True)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    list5.sort(True)
TypeError: sort() takes no positional arguments
>>> list5.sort(reverse=True)
>>> list5
[98876, 888, 65, 34, 23, 6, 5, 4]
>>> list6 = ['hello', '~', '$' ,'%', 'Hello', 'python']
>>> list6.sort()
>>> list6
['$', '%', 'Hello', 'hello', 'python', '~']
>>> list6 = [['hello', 'bye'], ['Hello', 'Python'], ['ram', 'Shyam']]
>>> list6.sort()
>>> list6
[['Hello', 'Python'], ['hello', 'bye'], ['ram', 'Shyam']]
>>> list6 = [['hello', 'bye'], ['Hello', 'Python'], ['Helli', 'Shyam']]
>>> list6.sort()
>>> list6
[['Helli', 'Shyam'], ['Hello', 'Python'], ['hello', 'bye']]
>>> list6 = [['hello', 'bye'], ['Hello', 'Python'], ['Hello', 'Shyam']]
>>> list6
[['hello', 'bye'], ['Hello', 'Python'], ['Hello', 'Shyam']]
>>> list6.sort()
>>> list6
[['Hello', 'Python'], ['Hello', 'Shyam'], ['hello', 'bye']]
>>> list6 = [[1, 'Ram'], [2, 'Shyam'], [3, 'Mohan']]
>>> list6.sort()
>>> list6
[[1, 'Ram'], [2, 'Shyam'], [3, 'Mohan']]
>>> list6 = [[1, 'Ram'], [2, 'Shyam'], [2, 'Mohan']]
>>> list6.sort()
>>> list6
[[1, 'Ram'], [2, 'Mohan'], [2, 'Shyam']]
>>> list6 = [[1, 'Ram'], [2, 'Shyam'], [3, 'Mohan']]
>>> 
