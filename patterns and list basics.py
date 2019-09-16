Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
*
**
***
****
*****
'''
'\n*\n**\n***\n****\n*****\n'
>>> for i in range(10):
	for j in range(i):
		print('*')

		
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> for i in range(10):
	for j in range(i):
		print('*',end='')

		
*********************************************
>>> for i in range(10):
	for j in range(i):
		print('*',end='')
	print('\n')

	


*

**

***

****

*****

******

*******

********

*********

>>> for i in range(10):
	for j in range(i):
		print('*',end='')
	print()

	

*
**
***
****
*****
******
*******
********
*********
>>> print()

>>> print('hello',end='')
hello
>>> print('\n',end='')

>>> print('\n',)


>>> '''
    *
   **
  ***
 ****
*****
'''
'\n    *\n   **\n  ***\n ****\n*****\n'
>>> for i in range(10,0,-1):
	for j in range(i):
		print('*',end='')
	print()

	
**********
*********
********
*******
******
*****
****
***
**
*
>>> for i in range(10):
	for j in range(9-i):
		print(' ',end='')
		for k in range(i):
			print('*',end='')
	print()

	
         
 * * * * * * * *
 ** ** ** ** ** ** **
 *** *** *** *** *** ***
 **** **** **** **** ****
 ***** ***** ***** *****
 ****** ****** ******
 ******* *******
 ********

>>> for i in range(10):
	for j in range(9-i):
		print(' ',end='')
	for k in range(i):
		print('*',end='')
	print()

	
         
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********
>>> '''
    *
   ***
  *****
 *******
*********
'''
'\n    *\n   ***\n  *****\n *******\n*********\n'
>>> for i in range(10):
	for j in range(9-i):
		print(' ',end='')
	for k in range(2 * i + 1):
		print('*',end='')
	print()

	
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
>>> for i in range(10):
	print('*' * i)

	

*
**
***
****
*****
******
*******
********
*********
>>> for i in range(10):
	for j in range(9-i):
		print(' ',end='"*" * i')
	for k in range(i):
		print('*',end='')
	print()

	
 "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i
 "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i*
 "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i**
 "*" * i "*" * i "*" * i "*" * i "*" * i "*" * i***
 "*" * i "*" * i "*" * i "*" * i "*" * i****
 "*" * i "*" * i "*" * i "*" * i*****
 "*" * i "*" * i "*" * i******
 "*" * i "*" * i*******
 "*" * i********
*********
>>> for i in range(10):
	for j in range(9-i):
		print(' ',end='')
		print('*' * i)

		
 
 
 
 
 
 
 
 
 
 *
 *
 *
 *
 *
 *
 *
 *
 **
 **
 **
 **
 **
 **
 **
 ***
 ***
 ***
 ***
 ***
 ***
 ****
 ****
 ****
 ****
 ****
 *****
 *****
 *****
 *****
 ******
 ******
 ******
 *******
 *******
 ********
>>> for i in range(10):
	print(' ' * (9-i))
	print('*' * i)

	
         

        
*
       
**
      
***
     
****
    
*****
   
******
  
*******
 
********

*********
>>> for i in range(10):
	print(' ' * (9-i),end='')
	print('*' * i)

	
         
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********
>>> for i in range(10):
	print(' ' * (9-i),end='')
	print('*' * (2 * i + 1))

	
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list1 = [1,2,3,5,'hello', 'bye', True, False]
>>> list1
[1, 2, 3, 5, 'hello', 'bye', True, False]
>>> list1 = [1,2,3,5,['hello', 'bye'], [True, False]]
>>> list1[0]
1
>>> list1[3]
5
>>> list1[34]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list1[34]
IndexError: list index out of range
>>> list1[4]
['hello', 'bye']
>>> list1[-1]
[True, False]
>>> list1[0:3]
[1, 2, 3]
>>> list1[0:3:-1]
[]
>>> list1[0::-1]
[1]
>>> list1[0:]
[1, 2, 3, 5, ['hello', 'bye'], [True, False]]
>>> list1[0::-1]
[1]
>>> str1 = 'hello'
>>> str1 = [0::-1
	
SyntaxError: invalid syntax
>>> str1 = [0::-1]
SyntaxError: invalid syntax
>>> str1[0::-1]
'h'
>>> list1[:0:-1]
[[True, False], ['hello', 'bye'], 5, 3, 2]
>>> list1[:-1:-1]
[]
>>> list1[:-1:1]
[1, 2, 3, 5, ['hello', 'bye']]
>>> 'hello' in list1
False
>>> ['hello', 'bye'] in list1
True
>>> len(list1)
6
>>> id(list1)
4318614152
>>> hex(id(list1))
'0x10168d288'
>>> hex(id(str1))
'0x103fc7b58'
>>> str1 = 'hello'
>>> str1[0] = 'h'
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    str1[0] = 'h'
TypeError: 'str' object does not support item assignment
>>> str1 = 'bye'
>>> str2 = 'python'
>>> hex(id(str1)) == hex(id(str1))
True
>>> hex(id(str1)) == hex(id(str2))
False
>>> hex(id(str1))
'0x103fc7ae8'
>>> hex(id(str2))
'0x10251b228'
>>> str2 = 'java'
>>> hex(id(str2))
'0x1010c6c00'
>>> type(str2)
<class 'str'>
>>> list1
[1, 2, 3, 5, ['hello', 'bye'], [True, False]]
>>> 2 in list1
True
>>> 22 not in list1
True
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> list1 = [['hello', 'bye'],['python', 'java']]
>>> list1.sort()
>>> list1
[['hello', 'bye'], ['python', 'java']]
>>> 
