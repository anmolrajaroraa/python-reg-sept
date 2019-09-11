Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = "ahjmke654"
>>> str1.isalnum()
True
>>> str2 = "#4"
>>> str2.isalnum()
False
>>> str1.isalpha()
False
>>> str3 = "python is a programming language"
>>> str3.isalpha()
False
>>> "python".isalpha()
True
>>> str3.replace("python", "java")
'java is a programming language'
>>> str3
'python is a programming language'
>>> a = 10
>>> a + 1
11
>>> a
10
>>> a = a + 1
>>> a
11
>>> str3 = str3.replace("python", "java")
>>> str3
'java is a programming language'
>>> str3.replace(' ', '')
'javaisaprogramminglanguage'
>>> str3.replace(' ', '').isaplha() #function chaining
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str3.replace(' ', '').isaplha() #function chaining
AttributeError: 'str' object has no attribute 'isaplha'
>>> str3.replace(' ', '').isalpha() #function chaining
True
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
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
 |  __mod__(self, value, /)
 |      Return self%value.
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
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> str3
'java is a programming language'
>>> str3.replace(' ', '', 3)
'javaisaprogramming language'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> '#$%^&*((FGHJMMKK!@3156    '.isascii()
True
>>> 'æįßç'.isascii()
False
>>> 'æabcdf'.isascii()
False
>>> #isdecimal works for normal digits
>>> #isdigit works for normal digits as well as super and subscripts
>>> #isnumerical works for everything including fractions
>>> '12345'.isdecimal()
True
>>> '12345'.isnumerical()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    '12345'.isnumerical()
AttributeError: 'str' object has no attribute 'isnumerical'
>>> '12345'.isnumeric()
True
>>> '12345'.isdigit()
True
>>> 'str3'.isidentifier()
True
>>> 'str_$3'.isidentifier()
False
>>> 'str_3'.isidentifier()
True
>>> 'str'.isidentifier()
True
>>> $str3 = "ahjsks"
SyntaxError: invalid syntax
>>> str3@ = "ahjsks"
SyntaxError: invalid syntax
>>> 'str3@'.isidentifier()
False
>>> 'abcd'.isprintable()
True
>>> 'abcd\n'.isprintable()
False
>>> '.'.join('python','language')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    '.'.join('python','language')
TypeError: join() takes exactly one argument (2 given)
>>> '.'.join()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    '.'.join()
TypeError: join() takes exactly one argument (0 given)
>>> '.'.join(['python','lang'])
'python.lang'
>>> ' '.join(['python','lang'])'
SyntaxError: EOL while scanning string literal
>>> ' '.join(['python','lang'])
'python lang'
>>> str3
'java is a programming language'
>>> str3.split()
['java', 'is', 'a', 'programming', 'language']
>>> list1 = str3.split()
>>> ' '.join(list1)
'java is a programming language'
>>> str3
'java is a programming language'
>>> str3.split('a')
['j', 'v', ' is ', ' progr', 'mming l', 'ngu', 'ge']
>>> str3.split('a',2)
['j', 'v', ' is a programming language']
>>> str4 = 'python is some lang.it\'s easy to learn'
>>> str4.split('.')
['python is some lang', "it's easy to learn"]
>>> str4.partition('.')
('python is some lang', '.', "it's easy to learn")
>>> str3.partition()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str3.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> str3.partition('a')
('j', 'a', 'va is a programming language')
>>> str3.partition(' ')
('java', ' ', 'is a programming language')
>>> str3.rpartition(' ')
('java is a programming', ' ', 'language')
>>> #partition breaks our string in 3 parts - before sep, sep itself, after sep
>>> str3.split('a',2)
['j', 'v', ' is a programming language']
>>> str3.rsplit('a',2)
['java is a programming l', 'ngu', 'ge']
>>> str3.rsplit('a')
['j', 'v', ' is ', ' progr', 'mming l', 'ngu', 'ge']
>>> str3.split('a')
['j', 'v', ' is ', ' progr', 'mming l', 'ngu', 'ge']
>>> str5 = 'abcdghf\nakdhdjkcn\njkakjfklalfk'
>>> str5.splitlines()
['abcdghf', 'akdhdjkcn', 'jkakjfklalfk']
>>> '12'.zfill(5)
'00012'
>>> '12'.zfill(3)
'012'
>>> '12'.zfill(2)
'12'
>>> '12345'.zfill(5)
'12345'
>>> '12345'.zfill(7)
'0012345'
>>> '12345'.zfill(4)
'12345'
>>> str3
'java is a programming language'
>>> str3.maketrans('jav', 'abc')
{106: 97, 97: 98, 118: 99}
>>> table = str3.maketrans('jav', 'abc')
>>> str3.translate(table)
'abcb is b progrbmming lbngubge'
>>> str3.maketrans('jav', 'abc', 'a')
{106: 97, 97: None, 118: 99}
>>> str3.maketrans('jav', 'abc', 'a')
{106: 97, 97: None, 118: 99}
>>> None
>>> 
>>> True False None
SyntaxError: invalid syntax
>>> table = str3.maketrans('jav', 'abc', 'a')
>>> table = str3.maketrans('jav', 'abc')
>>> table = str3.maketrans('jav', 'abc', 'a')
>>> str3.translate(table)
'ac is  progrmming lnguge'
>>> table = str3.maketrans('jav', 'xaz', 'a')
>>> str3.translate(table)
'xz is  progrmming lnguge'
>>> import sys
>>> sys.path
['', '/Users/anmolrajarora/Documents', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/anmolrajarora/Library/Python/3.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x10f858080>
>>> turtle.forward(100)
>>> turtle.left(90)
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.reset()
>>> t = turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    t = turtle.Pen()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> t = turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    t = turtle.Pen()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in [0,1,2,3]:
	print(i)

	
0
1
2
3
>>> for i in [0,1,2,3]:
	print("Value is", i)

	
Value is 0
Value is 1
Value is 2
Value is 3
>>> for i in [0,1,2,3]:
	print("Value is", i)
	 print()
	 
SyntaxError: unexpected indent
>>> t.reset()
>>> for i in range(4):
	t.forward(100)
	t.left(90)
