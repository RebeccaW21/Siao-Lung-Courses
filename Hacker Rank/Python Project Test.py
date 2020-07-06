Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> exec('''#!/bin/python

import math
import os
import random
import re
import sys


class Multiset(object):


    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass
    
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(raw_input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#0>", line 56, in <module>
    fptr.close()''')
  File "<string>", line 54
    fptr.write('
               ^
SyntaxError: EOL while scanning string literal
>>> 
>>> exec(r'''#!/bin/python

import math
import os
import random
import re
import sys


class Multiset(object):


    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(raw_input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#2>", line 56, in <module>
    fptr.close()''')
  File "<string>", line 46, in <module>
NameError: name 'raw_input' is not defined

>>> exec(r'''#!/bin/python

import math
import os
import random
import re
import sys


class Multiset(object):


    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
12
Traceback (most recent call last):
  File "<pyshell#3>", line 56, in <module>
    fptr.close()''')
  File "<string>", line 48, in <module>
NameError: name 'xrange' is not defined
>>> 
>>> exec(r'''#!/bin/python

import math
import os
import random
import re
import sys


class Multiset(object):


    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(raw_input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
12
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> exec(r'''#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
12

'










Traceback (most recent call last):
  File "<pyshell#7>", line 55, in <module>
    fptr.close()''')
  File "<string>", line 50, in <module>
  File "<string>", line 33, in performOperations
IndexError: list index out of range
>>> 
>>> 
>>> exec(r'''#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
12
query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> result = performOperations('''query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size''')
Traceback (most recent call last):
  File "<pyshell#12>", line 12, in <module>
    size''')
  File "<string>", line 36, in performOperations
IndexError: list index out of range
>>> 
>>> result = performOperations('''query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size'''.split('\n'))
>>> 
>>> result
[False, False, False, 0, False, False, 0]
>>> 
>>> performOperations('''query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size'''.split('\n'))
[False, False, False, 0, False, False, 0]
>>> 
>>> exec('''fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#20>", line 4, in <module>
    fptr.close()''')
  File "<string>", line 2
    fptr.write('
    ^
IndentationError: unexpected indent

>>> exec('''fptr = open(os.environ['OUTPUT_PATH'], 'w')
fptr.write('\n'.join(map(str, result)))
fptr.write('\n')
fptr.close()''')

Traceback (most recent call last):
  File "<pyshell#21>", line 4, in <module>
    fptr.close()''')
  File "<string>", line 2
    fptr.write('
               ^
SyntaxError: EOL while scanning string literal
>>> 
>>> exec(r'''fptr = open(os.environ['OUTPUT_PATH'], 'w')
fptr.write('\n'.join(map(str, result)))
fptr.write('\n')
fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#23>", line 4, in <module>
    fptr.close()''')
  File "<string>", line 1, in <module>
  File "C:\ProgramData\Anaconda3\lib\os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: 'OUTPUT_PATH'

>>> exec(r'''#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(12)
    operations = """query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size""".split('\n')
##    for _ in range(q):
##        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')


Traceback (most recent call last):
  File "<pyshell#24>", line 66, in <module>
    fptr.close()''')
  File "<string>", line 63, in <module>
  File "C:\ProgramData\Anaconda3\lib\os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: 'OUTPUT_PATH'
>>> 
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Siao Lung\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-SIAOLUNG', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'GTK_BASEPATH': 'C:\\Program Files (x86)\\GtkSharp\\2.12\\', 'HOME': 'C:\\Users\\Siao Lung', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Siao Lung', 'LOCALAPPDATA': 'C:\\Users\\Siao Lung\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-SIAOLUNG', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\Siao Lung\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\ProgramData\\Anaconda3;C:\\ProgramData\\Anaconda3\\Library\\mingw-w64\\bin;C:\\ProgramData\\Anaconda3\\Library\\usr\\bin;C:\\ProgramData\\Anaconda3\\Library\\bin;C:\\ProgramData\\Anaconda3\\Scripts;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\GtkSharp\\2.12\\bin;C:\\Program Files\\MATLAB\\R2019b\\bin;C:\\Users\\Siao Lung\\AppData\\Local\\Microsoft\\WindowsApps;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3d04', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\SIAOLU~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\SIAOLU~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'DELL-SIAOLUNG', 'USERDOMAIN_ROAMINGPROFILE': 'DELL-SIAOLUNG', 'USERNAME': 'Siao Lung', 'USERPROFILE': 'C:\\Users\\Siao Lung', 'WINDIR': 'C:\\Windows'})
>>> 
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 'a' in object
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'a' in object
TypeError: argument of type 'type' is not iterable
>>> 
>>> 'a' in object()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'a' in object()
TypeError: argument of type 'object' is not iterable
>>> 
>>> 'a' in list()
False
>>> object()
<object object at 0x0000020A3387E3A0>
>>> 
>>> object('makan)
       
SyntaxError: EOL while scanning string literal
>>> object('makan')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    object('makan')
TypeError: object() takes no arguments
>>> 
>>> exec(r'''#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    List = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.List.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        self.List.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.List
    
    def __len__(self):
        # returns the number of elements in the multiset
        return 0

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(12)
    operations = """query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size""".split('\n')
##    for _ in range(q):
##        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#42>", line 68, in <module>
    fptr.close()''')
  File "<string>", line 65, in <module>
  File "C:\ProgramData\Anaconda3\lib\os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: 'OUTPUT_PATH'
>>> 
>>> result
[False, True, False, 0, True, True, 0]
>>> 
>>> operations
['query 1', 'add 1', 'query 1', 'remove 1', 'query 1', 'add 2', 'add 2', 'size', 'query 2', 'remove 2', 'query 2', 'size']
>>> 
>>> exec(r'''#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    List = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.List.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        self.List.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.List

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.List)

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(12)
    operations = """query 1
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size""".split('\n')
##    for _ in range(q):
##        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()''')
Traceback (most recent call last):
  File "<pyshell#48>", line 68, in <module>
    fptr.close()''')
  File "<string>", line 65, in <module>
  File "C:\ProgramData\Anaconda3\lib\os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: 'OUTPUT_PATH'
>>> 
>>> operations
['query 1', 'add 1', 'query 1', 'remove 1', 'query 1', 'add 2', 'add 2', 'size', 'query 2', 'remove 2', 'query 2', 'size']
>>> result
[False, True, False, 2, True, True, 1]
>>> 
>>> #!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, l, w): self.area = l*w
    def area(self): return self.area
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> class Rectangle:
    def __init__(self, l, w): self.area = l*w
    def area(self): return self.area

    
>>> class Circle:
    def __init__(self, d): self.area = 3.14*d
    def area(self): return self.area

    
>>> Rectangle(a, b)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    Rectangle(a, b)
NameError: name 'a' is not defined
>>> 
>>> Rectangle(2, 3)
<__main__.Rectangle object at 0x0000020A3442FE48>
>>> 
>>> Rectangle(2, 3).area
6
>>> 3.14*1000
3140.0
>>> 
