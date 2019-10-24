Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> student = {
	'id' : 101,
	'name
	
SyntaxError: EOL while scanning string literal
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'course' : 'BTech',
	'contact' : ['1234', '4567'],
	'address' : {
		'home' : 'rohini',
		'hostel' : 'ncr'
		}
	}
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> student['id']
101
>>> student['address']
{'home': 'rohini', 'hostel': 'ncr'}
>>> student.get('address')
{'home': 'rohini', 'hostel': 'ncr'}
>>> student.items()
dict_items([('id', 101), ('name', 'Ram'), ('course', 'BTech'), ('contact', ['1234', '4567']), ('address', {'home': 'rohini', 'hostel': 'ncr'})])
>>> student.keys()
dict_keys(['id', 'name', 'course', 'contact', 'address'])
>>> student.values()
dict_values([101, 'Ram', 'BTech', ['1234', '4567'], {'home': 'rohini', 'hostel': 'ncr'}])
>>> student.pop('course')
'BTech'
>>> student
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'address': {'home': 'rohini', 'hostel': 'ncr'}}
>>> student.popitem()
('address', {'home': 'rohini', 'hostel': 'ncr'})
>>> 
>>> marks = {
	'sem1':90,
	'sem2' : 80
	}
>>> 
>>> student.update(marks)
>>> student
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80}
>>> student['marks'] = marks
>>> student
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}}
>>> student.setdefault('course', 'BTech')
'BTech'
>>> student.setdefault('course', 'BCA')
'BTech'
>>> student['course'] = 'BCA'
>>> student
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}, 'course': 'BCA'}
>>> 
>>> keys = student.keys()
>>> newStudent = dict.fromkeys(keys, '')
>>> newStudent
{'id': '', 'name': '', 'contact': '', 'sem1': '', 'sem2': '', 'marks': '', 'course': ''}
>>> 
>>> # expression that will be appended    for loop     if(optional)
>>> 
>>> keys
dict_keys(['id', 'name', 'contact', 'sem1', 'sem2', 'marks', 'course'])
>>> values = student.values()
>>> values
dict_values([101, 'Ram', ['1234', '4567'], 90, 80, {'sem1': 90, 'sem2': 80}, 'BCA'])
>>> 
>>> 
>>> zip(keys,values)
<zip object at 0x10c130a48>
>>> list(zip(keys,values))
[('id', 101), ('name', 'Ram'), ('contact', ['1234', '4567']), ('sem1', 90), ('sem2', 80), ('marks', {'sem1': 90, 'sem2': 80}), ('course', 'BCA')]
>>> 
>>> student2 = {}
>>> for i,j in zip(keys,values):
	student[i] = j

	
>>> student2
{}
>>> for i,j in zip(keys,values):
	student2[i] = j

	
>>> student2
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}, 'course': 'BCA'}
>>> 
>>> 
>>> student3 = {student2[i] = j for i,j in zip(keys,values)}
SyntaxError: invalid syntax
>>> student3 = {i:j for i,j in zip(keys,values)}
>>> student3
{'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}, 'course': 'BCA'}
>>> 
>>> 
>>> print(f'''
Id : {id},
Name : {name},
Contact : {contact},
Sem1 : {sem1},
Sem2 : {sem2},
Marks : {marks},
Course : {course}
''')
Traceback (most recent call last):
  File "<pyshell#74>", line 9, in <module>
    ''')
NameError: name 'name' is not defined

>>> id(student3)
4462757352
>>> id
<built-in function id>
>>> print('''
Id : {id},
Name : {name},
Contact : {contact},
Sem1 : {sem1},
Sem2 : {sem2},
Marks : {marks},
Course : {course}
'''.format_map(student3))

Id : 101,
Name : Ram,
Contact : ['1234', '4567'],
Sem1 : 90,
Sem2 : 80,
Marks : {'sem1': 90, 'sem2': 80},
Course : BCA

>>> student3 = {'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}, 'course': 'BCA', 1 : 1}
>>> print('''
Id : {id},
Name : {name},
Contact : {contact},
Sem1 : {sem1},
Sem2 : {sem2},
Marks : {marks},
Course : {course},
1 : {1}
'''.format_map(student3))
Traceback (most recent call last):
  File "<pyshell#79>", line 10, in <module>
    '''.format_map(student3))
ValueError: Format string contains positional fields

>>> student3.get(1)
1
>>> student3 = {'id': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'sem1': 90, 'sem2': 80, 'marks': {'sem1': 90, 'sem2': 80}, 'course': 'BCA', '1' : 1}
>>> print('''
Id : {id},
Name : {name},
Contact : {contact},
Sem1 : {sem1},
Sem2 : {sem2},
Marks : {marks},
Course : {course},
1 : {1}
'''.format_map(student3))
Traceback (most recent call last):
  File "<pyshell#82>", line 10, in <module>
    '''.format_map(student3))
ValueError: Format string contains positional fields
>>> 
>>> tuple1 = (1,2,3,4,6, 'hello', True)
>>> #immutable
>>> tuple1[0] = 100
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    tuple1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> tuple1 = (1,2,3,4,5,[4,5,6,7])
>>> tuple1[-1].append(8)
>>> tuple1
(1, 2, 3, 4, 5, [4, 5, 6, 7, 8])
>>> 
>>> 
>>> set1 = {}  #no indexing, no key value pair, randomly memory is allocated (hashing), unique items
>>> 
>>> set1 = {1,2,3,5,6,'hello', 'python', True}
>>> set1
{1, 2, 3, 5, 6, 'python', 'hello'}
>>> set1.add(False)
>>> set1
{False, 1, 2, 3, 5, 6, 'python', 'hello'}
>>> set1
{False, 1, 2, 3, 5, 6, 'python', 'hello'}
>>> set1.add(0)
>>> {False, 1, 2, 3, 5, 6, 'python', 'hello'}
{False, 1, 2, 3, 5, 6, 'python', 'hello'}
>>> set1
{False, 1, 2, 3, 5, 6, 'python', 'hello'}
>>> 
>>> for element in set1:
	print(element)

	
False
1
2
3
5
6
python
hello
>>> set1.remove(6)
>>> set1.discard(5)
>>> set1.remove(6)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    set1.remove(6)
KeyError: 6
>>> set1.remove(6)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set1.remove(6)
KeyError: 6
>>> set1.discard(5)
>>> 
>>> 
>>> set1.pop()
False
>>> set1.pop()
1
>>> set1.pop()
2
>>> 
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> set1
{3, 'python', 'hello'}
>>> set2 = {'python' , 'hello', True}
>>> set1.difference(set2)
{3}
>>> set2.difference(set1)
{True}
>>> 
>>> set1.symmetric_difference(set2)
{True, 3}
>>> 
>>> set1 - set2
{3}
>>> (set1 - set2).union(set2 - set1)
{True, 3}
>>> set1.difference_update(set2)
>>> set1
{3}
>>> 
>>> set1.update(set2)
>>> set1
{True, 3, 'python', 'hello'}
>>> set1.intersection(set2)
{True, 'hello', 'python'}
\
>>> set3 = {11,22,33}
>>> set1.isdisjoint(set3)
True
>>> set1.isdisjoint(set2)
False
>>> 
>>> set1
{True, 3, 'python', 'hello'}
>>> set2
{'hello', True, 'python'}
>>> 
>>> set1.issuperset(set2)
True
>>> set2.issubset(set1)
True
>>> 
>>> fixedSet = frozenset(set1)
>>> fixedSet
frozenset({'hello', True, 3, 'python'})
>>> 
>>> dir(frozenset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> 
>>> 
>>> def1 = 'Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.'
>>> def2 = 'Machine Learning is the field of study that gives computers the capability to learn without being explicitly programmed. ML is one of the most exciting technologies that one would have ever come across. As it is evident from the name, it gives the computer that which makes it more similar to humans: The ability to learn. Machine learning is actively being used today, perhaps in many more places than one would expect.'
>>> 
>>> # intersection / union   *  100
>>> 
>>> 
>>> tokens_1 = def.split()
SyntaxError: invalid syntax
>>> tokens_1 = def1.split()
>>> tokens_!
SyntaxError: invalid syntax
>>> tokens_1
['Machine', 'learning', 'is', 'an', 'application', 'of', 'artificial', 'intelligence', '(AI)', 'that', 'provides', 'systems', 'the', 'ability', 'to', 'automatically', 'learn', 'and', 'improve', 'from', 'experience', 'without', 'being', 'explicitly', 'programmed.', 'Machine', 'learning', 'focuses', 'on', 'the', 'development', 'of', 'computer', 'programs', 'that', 'can', 'access', 'data', 'and', 'use', 'it', 'learn', 'for', 'themselves.']
>>> tokens_2 = def2.split()
>>> tokens_2
['Machine', 'Learning', 'is', 'the', 'field', 'of', 'study', 'that', 'gives', 'computers', 'the', 'capability', 'to', 'learn', 'without', 'being', 'explicitly', 'programmed.', 'ML', 'is', 'one', 'of', 'the', 'most', 'exciting', 'technologies', 'that', 'one', 'would', 'have', 'ever', 'come', 'across.', 'As', 'it', 'is', 'evident', 'from', 'the', 'name,', 'it', 'gives', 'the', 'computer', 'that', 'which', 'makes', 'it', 'more', 'similar', 'to', 'humans:', 'The', 'ability', 'to', 'learn.', 'Machine', 'learning', 'is', 'actively', 'being', 'used', 'today,', 'perhaps', 'in', 'many', 'more', 'places', 'than', 'one', 'would', 'expect.']
>>> stopwords = ['is', 'an', 'of', 'that', 'the', 'to', 'and', 'from', 'for', 'on', 'it', 'can', 'in']
>>> 
>>> words_1 = [token for token in tokens_1 if token not in stopwords]
>>> words_1
['Machine', 'learning', 'application', 'artificial', 'intelligence', '(AI)', 'provides', 'systems', 'ability', 'automatically', 'learn', 'improve', 'experience', 'without', 'being', 'explicitly', 'programmed.', 'Machine', 'learning', 'focuses', 'development', 'computer', 'programs', 'access', 'data', 'use', 'learn', 'themselves.']
>>> words_2 = [token for token in tokens_2 if token not in stopwords]
>>> words_@
SyntaxError: invalid syntax
>>> words_2
['Machine', 'Learning', 'field', 'study', 'gives', 'computers', 'capability', 'learn', 'without', 'being', 'explicitly', 'programmed.', 'ML', 'one', 'most', 'exciting', 'technologies', 'one', 'would', 'have', 'ever', 'come', 'across.', 'As', 'evident', 'name,', 'gives', 'computer', 'which', 'makes', 'more', 'similar', 'humans:', 'The', 'ability', 'learn.', 'Machine', 'learning', 'actively', 'being', 'used', 'today,', 'perhaps', 'many', 'more', 'places', 'than', 'one', 'would', 'expect.']
>>> stopwords = ['is', 'an', 'of', 'that', 'the', 'to', 'and', 'from', 'for', 'on', 'it', 'can', 'in', 'as']
>>> words_1 = [token.lower() for token in tokens_1 if token.lower() not in stopwords]
>>> words_2 = [token.lower() for token in tokens_2 if token.lower() not in stopwords]
>>> words_1
['machine', 'learning', 'application', 'artificial', 'intelligence', '(ai)', 'provides', 'systems', 'ability', 'automatically', 'learn', 'improve', 'experience', 'without', 'being', 'explicitly', 'programmed.', 'machine', 'learning', 'focuses', 'development', 'computer', 'programs', 'access', 'data', 'use', 'learn', 'themselves.']
>>> words_2
['machine', 'learning', 'field', 'study', 'gives', 'computers', 'capability', 'learn', 'without', 'being', 'explicitly', 'programmed.', 'ml', 'one', 'most', 'exciting', 'technologies', 'one', 'would', 'have', 'ever', 'come', 'across.', 'evident', 'name,', 'gives', 'computer', 'which', 'makes', 'more', 'similar', 'humans:', 'ability', 'learn.', 'machine', 'learning', 'actively', 'being', 'used', 'today,', 'perhaps', 'many', 'more', 'places', 'than', 'one', 'would', 'expect.']
>>> 
>>> intersection = len(set(words_1).intersection(set(words_2)))
>>> union = len(set(words_1).union(set(words_2)))
>>> intersection
9
>>> union
56
>>> JaccardsDistance = intersection / union * 100
>>> print(f"Text similarity is {JaccardsDistance}%")
Text similarity is 16.071428571428573%
>>> 
