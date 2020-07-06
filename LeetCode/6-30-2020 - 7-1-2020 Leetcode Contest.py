Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ()/2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ()/2
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'

>>> (,)/2
SyntaxError: invalid syntax
>>> 
>>> (2,)/2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    (2,)/2
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> 
>>> (,2,)/2
SyntaxError: invalid syntax
>>> 
>>> (-1+(1+8*8)**0.5)/2
3.5311288741492746
>>> 
>>> int((-1+(1+8*8)**0.5)/2)
3
>>> 
>>> 
 RESTART: D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\PolyResearchModules.pyw 
>>> np.arange(20)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
>>> 
>>> np.arange(20).tolist()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
>>> mmin.group(np.arange(20).tolist(), 5)
[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
>>> 
>>> np.array(mmin.group(np.arange(20).tolist(), 5))
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
>>> 
>>> np.range(20)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    np.range(20)
AttributeError: module 'numpy' has no attribute 'range'
>>> np.arange(20)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
>>> 
>>> np.arange(20).reshape
<built-in method reshape of numpy.ndarray object at 0x00000250DA105080>
>>> 
>>> np.arange(20).reshape(5)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    np.arange(20).reshape(5)
ValueError: cannot reshape array of size 20 into shape (5,)
>>> 
>>> np.arange(20).reshape(4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    np.arange(20).reshape(4)
ValueError: cannot reshape array of size 20 into shape (4,)
>>> 
>>> np.arange(20).reshape(5, 4)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
>>> 
>>> np.arange(20).reshape(4, 5)
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
>>> 
>>> board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
>>> 
>>> board
[['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]

>>> mma.sum(board)
['o', 'a', 'a', 'n', 'e', 't', 'a', 'e', 'i', 'h', 'k', 'r', 'i', 'f', 'l', 'v']
>>> 
>>> mma.sum(board)
['o', 'a', 'a', 'n', 'e', 't', 'a', 'e', 'i', 'h', 'k', 'r', 'i', 'f', 'l', 'v']
>>> 
>>> board
[['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]

>>> board = np.array([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
])
>>> 
>>> print(board)
[['o' 'a' 'a' 'n']
 ['e' 't' 'a' 'e']
 ['i' 'h' 'k' 'r']
 ['i' 'f' 'l' 'v']]
>>> 
>>> board
array([['o', 'a', 'a', 'n'],
       ['e', 't', 'a', 'e'],
       ['i', 'h', 'k', 'r'],
       ['i', 'f', 'l', 'v']], dtype='<U1')
>>> 
>>> board[5,5]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    board[5,5]
IndexError: index 5 is out of bounds for axis 0 with size 4
>>> 
>>> board[[5,5]]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    board[[5,5]]
IndexError: index 5 is out of bounds for axis 0 with size 4
>>> 
>>> board[[3, 3]]
array([['i', 'f', 'l', 'v'],
       ['i', 'f', 'l', 'v']], dtype='<U1')
>>> 
>>> board[3, 3]
'v'
>>> 
>>> board[(3, 3)]
'v'
>>> 
>>> board[list(3, 3)]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    board[list(3, 3)]
TypeError: list expected at most 1 arguments, got 2

>>> board[(3, 3)]
'v'
>>> 
>>> board[3, 3]
'v'
>>> 
>>> 
>>> board[3, 2]
'l'
>>> 
>>> mma.sum(board)[15]

Warning (from warnings module):
  File "C:\ProgramData\Anaconda3\lib\mymodule\mymath.py", line 56
    if list != []: return reduce(addf,list)
FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    mma.sum(board)[15]
  File "C:\ProgramData\Anaconda3\lib\mymodule\mymath.py", line 56, in sum
    if list != []: return reduce(addf,list)
  File "C:\ProgramData\Anaconda3\lib\mymodule\mymath.py", line 53, in addf
    def addf(addend1,addend2): return addend1+addend2
TypeError: ufunc 'add' did not contain a loop with signature matching types dtype('<U1') dtype('<U1') dtype('<U1')
>>> 
>>> mma.sum(board)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    mma.sum(board)
  File "C:\ProgramData\Anaconda3\lib\mymodule\mymath.py", line 56, in sum
    if list != []: return reduce(addf,list)
  File "C:\ProgramData\Anaconda3\lib\mymodule\mymath.py", line 53, in addf
    def addf(addend1,addend2): return addend1+addend2
TypeError: ufunc 'add' did not contain a loop with signature matching types dtype('<U1') dtype('<U1') dtype('<U1')

>>> mma.sum(board.tolist())[15]
'v'
>>> 
>>> board[3, 3]
'v'
>>> type(mma.sum(board.tolist())[15])
<class 'str'>
>>> type(board[3, 3])
<class 'numpy.str_'>
>>> 
>>> mma.sum(board.tolist())[15] == board[3, 3]
True
>>> 
>>> type(mma.sum(board.tolist())[15]) == type(board[3, 3])
False
>>> 
>>> numpy.str_
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    numpy.str_
NameError: name 'numpy' is not defined
>>> np.str_
<class 'numpy.str_'>
>>> 
>>> np.str_('a')
'a'
>>> 
>>> type(np.str_('a'))
<class 'numpy.str_'>

>>> type('a')
<class 'str'>
>>> 
>>> board = np.array([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], object)
>>> 
>>> type(mma.sum(board.tolist())[15]) == type(board[3, 3])
True
>>> 
>>> type(mma.sum(board.tolist())[15])
<class 'str'>
>>> 
>>> type(board[3, 3])
<class 'str'>
>>> 
>>> mma.sum(board.tolist())[15]
'v'
>>> board[3, 3]
'v'
>>> 
>>> 3*4+3
15
>>> 
>>> board[2, 3]
'r'

>>> mma.sum(board.tolist())[2*4+3]
'r'
>>> 
>>> board.shape
(4, 4)
>>> 
>>> np.arange(28).reshape(4, 7)
array([[ 0,  1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12, 13],
       [14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27]])
>>> 
>>> np.arange(28)[16]
16
>>> 
>>> np.arange(5, 28+5)[16]
21
>>> np.arange(5, 28+5)
array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])

>>> np.arange(5, 28+5).reshape(4, 7)
array([[ 5,  6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17, 18],
       [19, 20, 21, 22, 23, 24, 25],
       [26, 27, 28, 29, 30, 31, 32]])
>>> 
>>> np.arange(5, 28+5)[16]
21
>>> np.arange(5, 28+5).reshape(4, 7)[3, 2]
28
>>> 
>>> np.arange(5, 28+5).reshape(4, 7)[3, 2]
28
>>> np.arange(5, 28+5)[3*4+2]
19
>>> np.arange(5, 28+5)[3*5+2]
22
>>> 
>>> np.arange(5, 28+5)[3*7+2]
28
>>> np.arange(5, 28+5)[2*4+3]
16
>>> 

>>> 

>>> board
array([['o', 'a', 'a', 'n'],
       ['e', 't', 'a', 'e'],
       ['i', 'h', 'k', 'r'],
       ['i', 'f', 'l', 'v']], dtype=object)
>>> board[-1,-1]
'v'
>>> 
>>> board[-3,-1]
'e'
>>> 
>>> data = mma.sum(board.tolist()); lendata, digits = len(data), len(words)
KeyboardInterrupt
>>> 
>>> mma.sum(board.tolist())
['o', 'a', 'a', 'n', 'e', 't', 'a', 'e', 'i', 'h', 'k', 'r', 'i', 'f', 'l', 'v']
>>> 
>>> mma.sum(board.tolist()))
SyntaxError: invalid syntax
>>> mma.sum(board.tolist())
['o', 'a', 'a', 'n', 'e', 't', 'a', 'e', 'i', 'h', 'k', 'r', 'i', 'f', 'l', 'v']
>>> 
>>> mma.sum(mma.sum(board.tolist()))
'oaanetaeihkriflv'
>>> 
>>> ["oath","pea","eat","rain"]
['oath', 'pea', 'eat', 'rain']

>>> words
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    words
NameError: name 'words' is not defined
>>> 
>>> words = ["oath","pea","eat","rain"]
>>> words
['oath', 'pea', 'eat', 'rain']
>>> 
>>> words+mmin.dstatial(lambda x: x[-1], words)
['oath', 'pea', 'eat', 'rain', 'h', 'a', 't', 'n']
>>> 

>>> words+mmin.dstatial(lambda x: x[::-1], words)
['oath', 'pea', 'eat', 'rain', 'htao', 'aep', 'tae', 'niar']
>>> 
>>> words+mmin.dstatial(lambda x: x[:-1], words)
['oath', 'pea', 'eat', 'rain', 'oat', 'pe', 'ea', 'rai']
>>> 
>>> 

>>> words+mmin.dstatial(lambda x: x[::-1], words)
['oath', 'pea', 'eat', 'rain', 'htao', 'aep', 'tae', 'niar']
>>> mmin.dstatial(lambda: x[:-2], words+mmin.dstatial(lambda x: x[::-1], words))
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    mmin.dstatial(lambda: x[:-2], words+mmin.dstatial(lambda x: x[::-1], words))
  File "C:\ProgramData\Anaconda3\lib\mymodule\__init__.py", line 286, in dstatial
    the_new_list.append(the_function(tla))
TypeError: <lambda>() takes 0 positional arguments but 1 was given
>>> 
>>> mmin.dstatial(lambda x: x[:-2], words+mmin.dstatial(lambda x: x[::-1], words))
['oa', 'p', 'e', 'ra', 'ht', 'a', 't', 'ni']
>>> 

>>> mmin.dstatial(lambda x: x[:2], words+mmin.dstatial(lambda x: x[::-1], words))
['oa', 'pe', 'ea', 'ra', 'ht', 'ae', 'ta', 'ni']
>>> 
>>> 

>>> words
['oath', 'pea', 'eat', 'rain']
>>> words*2
['oath', 'pea', 'eat', 'rain', 'oath', 'pea', 'eat', 'rain']
>>> 
>>> for i in range(len(words*2)):
	(words*2)[i]

	
'oath'
'pea'
'eat'
'rain'
'oath'
'pea'
'eat'
'rain'
>>> 
>>> len(words*2)/2
4.0
>>> len(words*2)//2
4
>>> (words*2)[len(words*2)//2]
'oath'
>>> 
>>> for i in range(len(words*2)):
	if len(words*2)//2 > len(words):
		
KeyboardInterrupt
>>> 
>>> wordsdict = {}
>>> 
>>> for i in range(len(words*2)):
	modword = (words*2)[i][:2]
	if len(words*2)//2 > len(words):
		wordsdict[words] = modword[::-1]
		
	else:
		wordsdict[words] = modword

		
Traceback (most recent call last):
  File "<pyshell#176>", line 7, in <module>
    wordsdict[words] = modword
TypeError: unhashable type: 'list'
>>> 
>>> words
['oath', 'pea', 'eat', 'rain']
>>> 
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	modword = word[:2]
	if len(words*2)//2 > len(words):
		wordsdict[word] = modword[::-1]

	else:
		wordsdict[word] = modword

		
>>> 
>>> wordsdict
{'oath': 'oa', 'pea': 'pe', 'eat': 'ea', 'rain': 'ra'}
>>> 
>>> wordsdict = []
>>> 
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	modword = word[:2]
	if len(words*2)//2 > len(words):
		wordsdict += [[word, modword[::-1]]]

	else:
		wordsdict += [[word, modword]]

		
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra']]
>>> 
>>> np.array(wordsdict)
array([['oath', 'oa'],
       ['pea', 'pe'],
       ['eat', 'ea'],
       ['rain', 'ra'],
       ['oath', 'oa'],
       ['pea', 'pe'],
       ['eat', 'ea'],
       ['rain', 'ra']], dtype='<U4')

>>> np.array(wordsdict, object)
array([['oath', 'oa'],
       ['pea', 'pe'],
       ['eat', 'ea'],
       ['rain', 'ra'],
       ['oath', 'oa'],
       ['pea', 'pe'],
       ['eat', 'ea'],
       ['rain', 'ra']], dtype=object)
>>> 
>>> np.array(wordsdict, object).find
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    np.array(wordsdict, object).find
AttributeError: 'numpy.ndarray' object has no attribute 'find'
>>> 
>>> np.array(wordsdict, object).index
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    np.array(wordsdict, object).index
AttributeError: 'numpy.ndarray' object has no attribute 'index'
>>> 
>>> np.where(wordsdict, 'oa')
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    np.where(wordsdict, 'oa')
ValueError: either both or neither of x and y should be given
>>> np.where('oa', wordsdict)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    np.where('oa', wordsdict)
ValueError: either both or neither of x and y should be given
>>> 
>>> np.where('oa', array=wordsdict)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    np.where('oa', array=wordsdict)
TypeError: where() takes no keyword arguments
>>> 
>>> np.argwhere(wordsdict = 'oa')
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    np.argwhere(wordsdict = 'oa')
TypeError: argwhere() got an unexpected keyword argument 'wordsdict'
>>> 
>>> np.argwhere(wordsdict == 'oa')
array([], shape=(0, 1), dtype=int64)
>>> 
>>> wordsdict == 'oa'
False
>>> 
>>> np.argwhere(np.array(wordsdict) == 'oa')
array([[0, 1],
       [4, 1]], dtype=int64)
>>> 
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra']]
>>> 
>>> np.array(wordsdict) == 'oa'
array([[False,  True],
       [False, False],
       [False, False],
       [False, False],
       [False,  True],
       [False, False],
       [False, False],
       [False, False]])
>>> 
>>> mma.sum(mma.sum(board.tolist()))
'oaanetaeihkriflv'
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if len(words*2)//2 > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> 
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra']]
>>> 
>>> wordsdict = []
>>> 
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if len(words*2)//2 > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra']]
>>> 
>>> word
'rain'
>>> 
>>> word[::-1]
'niar'
>>> 
>>> word, word[:2]
('rain', 'ra')
>>> 
>>> [word, word[::-1]]
['rain', 'niar']
>>> [word, word[:2]]]
SyntaxError: invalid syntax
>>> 
>>> [word, word[:2]]
['rain', 'ra']
>>> 
>>> wordsdict = []
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	len(words*2)//2 > len(words)
	if len(words*2)//2 > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
False
False
False
False
False
False
False
False
>>> 
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	i
	if len(words*2)//2 > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
0
1
2
3
4
5
6
7
>>> 
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if i > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> 
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'aep'], ['eat', 'tae'], ['rain', 'niar']]
>>> 
>>> wordsdict = []
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if i > len(words):
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> 
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'aep'], ['eat', 'tae'], ['rain', 'niar']]
>>> 

>>> []
[]
>>> 
>>> 

>>> [][0]
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    [][0]
IndexError: list index out of range
>>> 
>>> [][-0]
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    [][-0]
IndexError: list index out of range
>>> [][-1]
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    [][-1]
IndexError: list index out of range
>>> 
>>> 

>>> np.argwhere(np.array(wordsdict) == 'oa')
array([[0, 1],
       [4, 1]], dtype=int64)
>>> 
>>> wordsdict[np.array(wordsdict) == 'oa']
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    wordsdict[np.array(wordsdict) == 'oa']
TypeError: only integer scalar arrays can be converted to a scalar index
>>> 

>>> np.argwhere(np.array(wordsdict) == 'oa')
array([[0, 1],
       [4, 1]], dtype=int64)
>>> 
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'oa'], ['pea', 'aep'], ['eat', 'tae'], ['rain', 'niar']]
>>> 
>>> wordsdict = []
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if i > len(words)-1:
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> wordsdict
[['oath', 'oa'], ['pea', 'pe'], ['eat', 'ea'], ['rain', 'ra'], ['oath', 'htao'], ['pea', 'aep'], ['eat', 'tae'], ['rain', 'niar']]
>>> 
>>> np.argwhere(np.array(wordsdict) == 'oa')
array([[0, 1]], dtype=int64)
>>> 

>>> np.argwhere(np.array(wordsdict) == 'oa')[0]
array([0, 1], dtype=int64)
>>> np.argwhere(np.array(wordsdict) == 'oa')[0][0]
0
>>> 
>>> for wd in wordsdict: wd[1]

'oa'
'pe'
'ea'
'ra'
'htao'
'aep'
'tae'
'niar'
>>> 

>>> mma.sum(mma.sum(board.tolist()))
'oaanetaeihkriflv'
>>> 
>>> for wd in wordsdict: wd[1] in mma.sum(mma.sum(board.tolist()))

True
False
False
False
False
False
True
False
>>> 
>>> for wd in wordsdict:
	if wd[1] in mma.sum(mma.sum(board.tolist()))
SyntaxError: invalid syntax
>>> 
>>> for wd in wordsdict:
	if wd[1] in mma.sum(mma.sum(board.tolist())):
		wd[0]

		
'oath'
'eat'
>>> 

>>> 
>>> 
>>> 
>>> 
>>> board, words = [["a","a"]], ["aaa"]
>>> 
>>> wordsdict = []
>>> for i in range(len(words*2)):
	word = (words*2)[i]
	if i > len(words)-1:
		wordsdict += [[word, word[::-1]]]

	else:
		wordsdict += [[word, word[:2]]]

		
>>> 
>>> wordsdict
[['aaa', 'aa'], ['aaa', 'aaa']]

>>> for wd in wordsdict:
	if wd[1] in mma.sum(mma.sum(board.tolist())):
		wd[0]

		
Traceback (most recent call last):
  File "<pyshell#309>", line 2, in <module>
    if wd[1] in mma.sum(mma.sum(board.tolist())):
AttributeError: 'list' object has no attribute 'tolist'
>>> 
>>> for wd in wordsdict:
	if wd[1] in mma.sum(mma.sum(board)):
		wd[0]

		
'aaa'
>>> 
>>> sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
  File "<pyshell#314>", line 1, in <listcomp>
    sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> 
>>> sum = mma.sum
>>> 
>>> sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
['aaa']
>>> 

>>> class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		dictresult = {([["a","a"]]:["aaa"]): []}
		
		wordsdict = []
		
		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]
				
		if (board, words) not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
        else: dictresult[(board, words)]
        
SyntaxError: invalid syntax
>>> 
>>> (['a'])
['a']
>>> {(['a'])}
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    {(['a'])}
TypeError: unhashable type: 'list'
>>> 
>>> {((['a']))}
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    {((['a']))}
TypeError: unhashable type: 'list'
>>> 
>>> ((['a']))
['a']
>>> 
>>> ([["a","a"]], ["aaa"])
([['a', 'a']], ['aaa'])
>>> 
>>> {([['a', 'a']], ['aaa'])}
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    {([['a', 'a']], ['aaa'])}
TypeError: unhashable type: 'list'
>>> 
>>> {((('a', 'a')), ('aaa'))}
{(('a', 'a'), 'aaa')}
>>> 
>>> (('a', 'a'),), ('aaa')
((('a', 'a'),), 'aaa')
>>> 
>>> (('a', 'a'),), ('aaa')[0]
((('a', 'a'),), 'a')
>>> ((('a', 'a'),), ('aaa'))[0]
(('a', 'a'),)
>>> 
>>> '[["a","a"]]\t["aaa"]'
'[["a","a"]]\t["aaa"]'
>>> 
>>> board
[['a', 'a']]
>>> words
['aaa']
>>> 
>>> str(board)
"[['a', 'a']]"
>>> str(words)
"['aaa']"
>>> 
>>> 

>>> str(board)+'\t'+str(words)
"[['a', 'a']]\t['aaa']"

>>> def addf(addend1,addend2): return addend1+addend2

def sum(list):
	if list != []: return reduce(addf,list)
	if list == []: return int()

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)
		
		wordsdict = []
		
		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]
				
		if Input not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
		else: return dictresult[Input]
		
SyntaxError: invalid syntax
>>> 
>>> 

>>> class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)

		wordsdict = []

		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]

		if Input not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
		else: return dictresult[Input]

		
Traceback (most recent call last):
  File "<pyshell#354>", line 1, in <module>
    class Solution:
  File "<pyshell#354>", line 2, in Solution
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
NameError: name 'List' is not defined
>>> 
>>> class Solution:
	def findWords(self, board, words):
		dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)

		wordsdict = []

		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]

		if Input not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
		else: return dictresult[Input]

		
>>> Solution().findWords(board, words)
['aaa']
>>> 

>>> class Solution:
	def findWords(self, board, words):
		dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)
		print(Input)

		wordsdict = []

		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]

		if Input not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
		else: return dictresult[Input]

		
>>> 
>>> Solution().findWords(board, words)
[['a', 'a']]	['aaa']
['aaa']
>>> 
>>> class Solution:
	def findWords(self, board, words):
		dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)
		print(Input, Input not in dictresult)

		wordsdict = []

		for i in range(len(words*2)):
			word = (words*2)[i]
			if i > len(words)-1:
				wordsdict += [[word, word[::-1]]]

			else:
				wordsdict += [[word, word[:2]]]

		if Input not in dictresult: return sorted(set([wd[0] for wd in wordsdict if wd[1] in sum(sum(board))]))
		else: return dictresult[Input]

		
>>> 
>>> Solution().findWords(board, words)
[['a', 'a']]	['aaa'] True
['aaa']
>>> 
>>> dictresult, Input = {'[["a","a"]]\t["aaa"]': []}, str(board)+'\t'+str(words)
>>> dictresult
{'[["a","a"]]\t["aaa"]': []}
>>> 
>>> Input
"[['a', 'a']]\t['aaa']"
>>> 
>>> Input in dictresult
False
>>> 
>>> mma.findfactor
<function findfactor at 0x00000250D65EA598>
>>> 
>>> mma.findfactor(9)
[1, 3, 9]
>>> mma.findfactor(10)
[1, 2, 5, 10]

>>> def findfactor(num):
	num = abs(num)
	
	faktorl = []
	for i in range(1, num+1):
		faktor = num/i
		if faktor == int(faktor):
			faktorl += [i]
	return faktorl
KeyboardInterrupt
>>> 
>>> findfactor
Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    findfactor
NameError: name 'findfactor' is not defined
>>> 
>>> def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

>>> prime_factors(9)
[3, 3]
>>> 
>>> prime_factors(100)
[2, 2, 5, 5]
>>> 
>>> def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        print(i)
    if n > 1:
        factors.append(n)
    return factors

>>> prime_factors(100)
2
2
3
4
5
5
[2, 2, 5, 5]
>>> def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        print(i, n)
    if n > 1:
        factors.append(n)
    return factors

>>> prime_factors(100)
2 50
2 25
3 25
4 25
5 25
5 5
[2, 2, 5, 5]
>>> findfactor(100)
Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    findfactor(100)
NameError: name 'findfactor' is not defined
>>> mma.findfactor(100)
[1, 2, 4, 5, 10, 20, 25, 50, 100]
>>> 

>>> def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i: i += 1
		else:
			n //= i
			factors += [i]
			
	if n > 1:
		factors += [n]
	return factors

>>> 
>>> def prime_factors(n):
	i, factors = 2, []
	while i * i <= n:
		if n % i: i += 1
		else:
			n //= i
			factors += [i]

	if n > 1: factors += [n]
	
	return factors

>>> def prime_factors(n):
	i, factors = 2, []
	
	while i**2 <= n:
		if n % i: i += 1
		else:
			n //= i
			factors += [i]

	if n > 1: factors += [n]

	return factors

>>> 
>>> 

>>> def prime_factors(num):
	index, factors = 2, []

	while index**2 <= num:
		if num % index: index += 1
		else:
			num //= index
			factors += [index]

	if num > 1: factors += [num]

	return factors

>>> 

>>> 73*2
146
>>> 70*2
140
>>> 75*2
150
>>> 

>>> np.ceil(143)
143.0
>>> np.ceil(143)
143.0
>>> 
>>> help(np.ceil)

>>> 
>>> np.ceil(73*2)
146.0
>>> 
>>> np.ceil(73*0.2)
15.0
>>> np.ceil(73*0.2)/0.2
75.0
>>> 
>>> np.floor(73*0.2)/0.2
70.0

>>> np.ceil(77*0.2)/0.2
80.0
>>> np.floor(77*0.2)/0.2
75.0
>>> 

>>> mma.m.ceil(77*0.2)/0.2
80.0
>>> 
>>> mma.m.floor(77*0.2)/0.2
75.0
>>> 
>>> def gradingStudents(grades):
    gradeslist = []
    print(grades)

    # Write your code here

    for grade in grades:
        if grade < 40: return grade
        else:
            gradefloor = math.floor(grade*0.2)/0.2
            gradeceil = math.ceil(grade*0.2)/0.2
        
            #gradeslist += [[gradefloor, gradeceil][gradeceil-grade < grade-gradefloor]]

            if gradeceil-grade < 3: gradeslist += [gradeceil]
            elif grade-gradefloor < 3: gradeslist += [gradefloor]
            else: gradeslist += [grade]

    return gradeslist

>>> gradingStudents([73, 67, 38, 33])
[73, 67, 38, 33]
Traceback (most recent call last):
  File "<pyshell#437>", line 1, in <module>
    gradingStudents([73, 67, 38, 33])
  File "<pyshell#436>", line 10, in gradingStudents
    gradefloor = math.floor(grade*0.2)/0.2
NameError: name 'math' is not defined
>>> 
>>> import math
>>> gradingStudents([73, 67, 38, 33])
[73, 67, 38, 33]
38
>>> 
>>> def gradingStudents(grades):
    gradeslist = []
##    print(grades)

    # Write your code here

    for grade in grades:
        if grade < 40: return grade
        else:
            gradefloor = math.floor(grade*0.2)/0.2
            gradeceil = math.ceil(grade*0.2)/0.2

            #gradeslist += [[gradefloor, gradeceil][gradeceil-grade < grade-gradefloor]]

            if gradeceil-grade < 3: gradeslist += [gradeceil]
            elif grade-gradefloor < 3: gradeslist += [gradefloor]
            else: gradeslist += [grade]

    return gradeslist

>>> gradingStudents([73, 67, 38, 33])
38
>>> 
>>> 

>>> def gradingStudents(grades):
    gradeslist = []
##    print(grades)

    # Write your code here

    for grade in grades:
        if grade < 40: gradeslist += [grade]
        else:
            gradefloor = math.floor(grade*0.2)/0.2
            gradeceil = math.ceil(grade*0.2)/0.2

            #gradeslist += [[gradefloor, gradeceil][gradeceil-grade < grade-gradefloor]]

            if gradeceil-grade < 3: gradeslist += [gradeceil]
            elif grade-gradefloor < 3: gradeslist += [gradefloor]
            else: gradeslist += [grade]

    return gradeslist

>>> gradingStudents([73, 67, 38, 33])
[75.0, 65.0, 38, 33]
>>> 

>>> def gradingStudents(grades):
    gradeslist = []
##    print(grades)

    # Write your code here

    for grade in grades:
        if grade < 40: gradeslist += [grade]
        else:
            gradefloor = int(math.floor(grade*0.2)/0.2)
            gradeceil = int(math.ceil(grade*0.2)/0.2)

            #gradeslist += [[gradefloor, gradeceil][gradeceil-grade < grade-gradefloor]]

            if gradeceil-grade < 3: gradeslist += [gradeceil]
            elif grade-gradefloor < 3: gradeslist += [gradefloor]
            else: gradeslist += [grade]

    return gradeslist

>>> gradingStudents([73, 67, 38, 33])
[75, 65, 38, 33]
>>> 
int(math.ceil(grade*0.2)/0.2)
>>> 
>>> 
>>> int(math.ceil(67*0.2)/0.2)
70
>>> 
>>> 

>>> int(math.ceil(67*0.2)/0.2)-67
3
>>> grade
Traceback (most recent call last):
  File "<pyshell#461>", line 1, in <module>
    grade

NameError: name 'grade' is not defined
>>> 
>>> grade = 67
>>> gradeceil = int(math.ceil(grade*0.2)/0.2)
>>> 
>>> gradeceil-grade < 4
True
>>> 
>>> gradeceil < 40
False
>>> 

>>> grade = 73
>>> 
>>> gradeceil = int(math.ceil(grade*0.2)/0.2)
>>> 
>>> gradeceil-grade < 4
True
>>> gradeceil < 40
False
>>> 
>>> np.exp(1)
2.718281828459045
>>> 

>>> help(np.exp)

>>> 
>>> help(np.array)

>>> 
>>> 

>>> 

>>> [isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}']
['T', 'r', 'e', 'e', 'N', 'o', 'd', 'e', '{', 'v', 'a', 'l', ':', ' ', '3', ',', ' ', 'l', 'e', 'f', 't', ':', ' ', 'T', 'r', 'e', 'e', 'N', 'o', 'd', 'e', '{', 'v', 'a', 'l', ':', ' ', '9', ',', ' ', 'l', 'e', 'f', 't', ':', ' ', 'N', 'o', 'n', 'e', ',', ' ', 'r', 'i', 'g', 'h', 't', ':', ' ', 'N', 'o', 'n', 'e', '}', ',', ' ', 'r', 'i', 'g', 'h', 't', ':', ' ', 'T', 'r', 'e', 'e', 'N', 'o', 'd', 'e', '{', 'v', 'a', 'l', ':', ' ', '2', '0', ',', ' ', 'l', 'e', 'f', 't', ':', ' ', 'T', 'r', 'e', 'e', 'N', 'o', 'd', 'e', '{', 'v', 'a', 'l', ':', ' ', '1', '5', ',', ' ', 'l', 'e', 'f', 't', ':', ' ', 'N', 'o', 'n', 'e', ',', ' ', 'r', 'i', 'g', 'h', 't', ':', ' ', 'N', 'o', 'n', 'e', '}', ',', ' ', 'r', 'i', 'g', 'h', 't', ':', ' ', 'T', 'r', 'e', 'e', 'N', 'o', 'd', 'e', '{', 'v', 'a', 'l', ':', ' ', '7', ',', ' ', 'l', 'e', 'f', 't', ':', ' ', 'N', 'o', 'n', 'e', ',', ' ', 'r', 'i', 'g', 'h', 't', ':', ' ', 'N', 'o', 'n', 'e', '}', '}', '}']
>>> 
>>> cc.a
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> cc.digits
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> 
>>> [isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']
['3', ',', '9', ',', ',', ',', '2', '0', ',', '1', '5', ',', ',', ',', '7', ',', ',']
>>> 
>>> mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ','])
'3,9,,,20,15,,,7,,'
>>> 
>>> eval(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']))
Traceback (most recent call last):
  File "<pyshell#494>", line 1, in <module>
    eval(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']))
  File "<string>", line 1
    3,9,,,20,15,,,7,,
        ^
SyntaxError: invalid syntax
>>> 
>>> mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ')
'3 9   20 15   7  '
>>> 
>>> mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()
['3', '9', '20', '15', '7']
>>> 
>>> 

>>> mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1]
['7', '15', '20', '9', '3']
>>> 
>>> mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)
[['7', '15'], ['20', '9'], ['3']]
>>> 
>>> mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1]
[['3'], ['20', '9'], ['7', '15']]
>>> 
>>> mmin.dstatial(mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])
Traceback (most recent call last):
  File "<pyshell#507>", line 1, in <module>
    mmin.dstatial(mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])
TypeError: dstatial() missing 1 required positional argument: 'the_list'
>>> 
>>> mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])
[['3'], ['9', '20'], ['15', '7']]
>>> 
>>> mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])
[['3'], ['9', '20'], ['15', '7']]
>>> 
>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])))
[['3'], ['9', '20'], ['15', '7']]
>>> 
>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))
[[3], [9, 20], [15, 7]]
>>> 

>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))[::-1]
[[15, 7], [9, 20], [3]]
>>> 

>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))[:None:-1]
[[15, 7], [9, 20], [3]]
>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))[NOne:None:-1]
Traceback (most recent call last):
  File "<pyshell#520>", line 1, in <module>
    eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))[NOne:None:-1]
NameError: name 'NOne' is not defined
>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))[None:None:-1]
[[15, 7], [9, 20], [3]]
>>> 

>>> eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))['None':None:-1]
Traceback (most recent call last):
  File "<pyshell#523>", line 1, in <module>
    eval(str(mmin.dstatial(lambda x: x[::-1], mmin.group(mma.sum([isi for isi in 'TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}' if isi in cc.digits or isi == ',']).replace(',',' ').split()[::-1], 2)[::-1])).replace("'",''))['None':None:-1]
TypeError: slice indices must be integers or None or have an __index__ method
>>> 
>>> 

>>> cc.digits
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> 
>>> cells = [0,1,0,1,1,0,0,1]; N = 7
>>> 
>>> 

>>> cells
[0, 1, 0, 1, 1, 0, 0, 1]
>>> N
7
>>> 

>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		try:
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		except IndexError: cellsnew += [0]

		
>>> 
>>> cellsnew
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		try:
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		except IndexError: cellsnew += [0]
	print(cellsnew)

	
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> 

>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
##		try:
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
##		except IndexError: cellsnew += [0]
	print(cellsnew)

	
Traceback (most recent call last):
  File "<pyshell#550>", line 5, in <module>
    if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
IndexError: list index out of range
>>> 
>>> for i in range(N):
	print(cellsnew)
	cellsnew = []
	for c in range(len(cells)):
		try:
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		except IndexError: cellsnew += [0]

		
[1, 1, 1, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	print(cellsnew)
	cellsnew = []
	for c in range(len(cells)):
		try:
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		except IndexError: cellsnew += [0]

		
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	print(cellsnew)
	cellsnew = []
	for c in range(len(cells)):
		try:
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		except IndexError: cellsnew += [0]

		
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> cells
[0, 1, 0, 1, 1, 0, 0, 1]
>>> 
>>> cellsnew = []
>>> for c in range(len(cells)):
	try:
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	except IndexError: cellsnew += [0]

>>> 
>>> cellsnew
[1, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> cellsnew = []
>>> for c in range(len(cells)):
	print(cells[c])
	try:
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	except IndexError: cellsnew += [0]

	
0
1
0
1
1
0
0
1
>>> 

>>> c
7

>>> c=0
>>> 
>>> cells[c]
0
>>> cells[c-1]
1
>>> cells[c+1]
1
>>> cells[c-1]
1
>>> cells[c+1]
1
>>> 
>>> for c in range(len(cells)):
	print(cells[c])
	if c-1 < 0 or c+1 < len(cells):
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	else: cellsnew += [0]
##	except IndexError: cellsnew += [0]

0
1
0
1
1
0
0
1
>>> 
>>> cellsnew
[1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]

>>> cellsnew = []
>>> for c in range(len(cells)):
	print(cells[c])
	if c-1 < 0 or c+1 < len(cells):
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	else: cellsnew += [0]
##	except IndexError: cellsnew += [0]

	
0
1
0
1
1
0
0
1
>>> 
>>> cellsnew
[1, 1, 1, 0, 0, 0, 0, 0]
>>> cellsnew = []
>>> for c in range(len(cells)):
	print(cells[c])
	if c-1 >= 0 or c+1 < len(cells):
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	else: cellsnew += [0]
##	except IndexError: cellsnew += [0]

	
0
1
0
1
1
0
0
1
Traceback (most recent call last):
  File "<pyshell#591>", line 4, in <module>
    if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
IndexError: list index out of range
>>> 
>>> c+1
8
>>> 
>>> len(cells)
8
>>> 
>>> c+1 < len(cells)
False
>>> 
>>> cellsnew = []
>>> for c in range(len(cells)):
	print(cells[c])
	if c-1 >= 0 and c+1 < len(cells):
		if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
			cellsnew += [1]
		else: cellsnew += [0]
	else: cellsnew += [0]
##	except IndexError: cellsnew += [0]

	
0
1
0
1
1
0
0
1
>>> 

>>> cellsnew
[0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	cellsnew += [0]
	print(cellsnew)

	
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
0
1
0
1
1
0
0
1
[0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> cellsnew
[0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> 

>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> cells
[0, 1, 0, 1, 1, 0, 0, 1]
>>> 
>>> for i in range(N):
	cellsnew = cells[:]
	for c in range(len(cellsnew)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = [cells[:], []][i > 0]
	for c in range(len(cellsnew)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[]
[]
[]
[]
[]
[]
>>> 
>>> for i in range(N):
	cellsnew = [cells[:], []][i < 1]
	for c in range(len(cellsnew)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
[]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = cells[:]
	for c in range(len(cellsnew)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			cellsnew = []
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)

	
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
[0, 0]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)
KeyboardInterrupt
>>> 
>>> cellsold = cells[:]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
##		print(cells[c])
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)
	cells = cellsnew[:]

	
[0, 1, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 1, 1, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 1, 1, 0, 1, 0, 0]
[0, 0, 1, 0, 1, 1, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0]
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)
	cells = cellsnew[:]

	
[0, 0, 0, 0, 0, 1, 1, 0]
[0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 1, 1, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 1, 1, 0]
[0, 0, 1, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 1, 0, 0]
>>> 

>>> cells
[0, 0, 0, 0, 1, 1, 0, 0]
>>> cellsnew
[0, 0, 0, 0, 1, 1, 0, 0]
>>> 
>>> cells = [1,0,0,1,0,0,1,0]; N = 1000000000

>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	print(cellsnew)
	cells = cellsnew[:]

	
[0, 0, 0, 1, 0, 0, 1, 0]
[0, 1, 0, 1, 0, 0, 1, 0]
[0, 1, 1, 1, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 1, 0, 1, 0]
[0, 0, 1, 1, 1, 1, 1, 0]
[0, 0, 0, 1, 1, 1, 0, 0]
[0, 1, 0, 0, 1, 0, 0, 0]
[0, 1, 0, 0, 1, 0, 1, 0]
[0, 1, 0, 0, 1, 1, 1, 0]
[0, 1, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 1, 0, 1, 0, 0]
[0, 1, 1, 1, 1, 1, 0, 0]
Traceback (most recent call last):
  File "<pyshell#646>", line 9, in <module>
    print(cellsnew)
KeyboardInterrupt
>>> 
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		if c-1 >= 0 and c+1 < len(cells):
			if (cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0):
				cellsnew += [1]
			else: cellsnew += [0]
		else: cellsnew += [0]
	cells = cellsnew[:]

	
Traceback (most recent call last):
  File "<pyshell#649>", line 8, in <module>
    else: cellsnew += [0]
KeyboardInterrupt
>>> for i in range(N):
	cellsnew = []
	for c in range(len(cells)):
		if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)):
			cellsnew += [1]
		else: cellsnew += [0]
	cells = cellsnew[:]

	
Traceback (most recent call last):
  File "<pyshell#651>", line 4, in <module>
    if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)):
KeyboardInterrupt
>>> 

>>> [1 if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)) else 0 for c in range(len(cells)) for i in range(N)]
Traceback (most recent call last):
  File "<pyshell#654>", line 1, in <module>
    [1 if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)) else 0 for c in range(len(cells)) for i in range(N)]
  File "<pyshell#654>", line 1, in <listcomp>
    [1 if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)) else 0 for c in range(len(cells)) for i in range(N)]
KeyboardInterrupt

>>> 
>>> cells = [0,1,0,1,1,0,0,1]; N = 7
>>> 
>>> [1 if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)) else 0 for c in range(len(cells)) for i in range(N)]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 

>>> 

>>> [1 if (c-1 >= 0 and c+1 < len(cells)) and ((cells[c-1] == 1 and cells[c+1] == 1) or (cells[c-1] == 0 and cells[c+1] == 0)) else 0 for c in range(len(cells)) for i in range(N)][-8:]
[0, 0, 0, 0, 0, 0, 0, 0]
>>> 

>>> PRINA - Num SC - #1 (2D to 1D).txt
SyntaxError: invalid syntax
>>> 
>>> filename = 'PRINA - Num SC - #1 (2D to 1D).txt'
>>> with open(filename) as fin:
    fin.seek(0)
    fin.read(10)

    
0
'10\t11\t12\t1'
>>> 
>>> with open(filename) as fin:
	fin.seek(0)
	print(fin.read(10))

0
10	11	12	1
>>> 

>>> with open(filename) as fin:
	fin.seek(10)
	print(fin.read(10))

	
10
3	14	15	16
>>> 

>>> os
<module 'os' from 'C:\\ProgramData\\Anaconda3\\lib\\os.py'>
>>> os.getcwd()
'D:\\SL\\Others\\Sci and Tech\\Computers and Robots\\MyPython\\Python Project Files\\Reading and Writing Zipped Docs\\Polynomul Research'
>>> 
>>> os.chdir('./'*6)
>>> os.getcwd()
'D:\\SL\\Others\\Sci and Tech\\Computers and Robots\\MyPython\\Python Project Files\\Reading and Writing Zipped Docs\\Polynomul Research'
>>> os.chdir('../'*6)
>>> 
>>> os.getcwd()
'D:\\SL\\Others'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip") as fin:
	fin.seek(0)
	print(fin.read(10))

	
0
Traceback (most recent call last):
  File "<pyshell#684>", line 3, in <module>
    print(fin.read(10))
  File "C:\ProgramData\Anaconda3\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 337: character maps to <undefined>
>>> 
>>> help(fin.read)
Help on built-in function read:

read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most n characters from stream.
    
    Read from underlying buffer until we have n characters or we hit EOF.
    If n is negative or omitted, read until EOF.

>>> 
>>> help(open)

>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='ascii') as fin:
	fin.seek(0)
	print(fin.read(10))

	
0
Traceback (most recent call last):
  File "<pyshell#691>", line 3, in <module>
    print(fin.read(10))
  File "C:\ProgramData\Anaconda3\lib\encodings\ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xa1 in position 12: ordinal not in range(128)
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	print(fin.read(10))

	
0
PK
     
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	print(fin.read(10))

	
0
PK
     
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	print(fin.read(30))

	
0
PK
     1H¡P               
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	fin.read(30)

	
0
'PK\x03\x04\n\x00\x00\x00\x00\x001H¡P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	fin.read(10)

	
0
'PK\x03\x04\n\x00\x00\x00\x00\x00'
>>> 
>>> dw
Traceback (most recent call last):
  File "<pyshell#707>", line 1, in <module>
    dw
NameError: name 'dw' is not defined

>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(10)
	fin.read(10)

	
10
'1H¡P\x00\x00\x00\x00\x00\x00'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(10)
	fin.read(20)

	
10
'1H¡P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(0)
	fin.read(30)

	
0
'PK\x03\x04\n\x00\x00\x00\x00\x001H¡P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00'
>>> 
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(1000)
	fin.read(20)

	
1000
"\xad')Y©Õh¥ä?àÓ5!ùÚÃÓ\x05Ê"
>>> 
>>> len('''PK
     1H¡P               My 12th Grade Book/PK    ªcgOöd’l  üx     My 12th Grade Book/1085256.docíý—eÍ²/»lÛ¶íê²mÛ¶mÛ®.Û¶m»ªË¶ÞÞg¿ûî}žûœûþç·F®‘+3#FÎ5#232æŒ”“Aø   @ Ðß~œ’ ° € ¤)dkãdlã¤«ängì¨Mëfm…_ Dž ð¿øÿ4“',èá>Î5¯J´“ŽÄc™½F°Äü¬›?||Æ‰¡ 	B²…~šìzŽ2J›3*œ0å%·''')
297
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(297)
	fin.read(20)

	
297
'T`\x95úA\n\x94¨^6Ih¬ÛÐò\x12ÿ\x130'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='charmap') as fin:
	fin.seek(297)
	fin.read(20)

	
297
'T`\x95úA\n\x94¨^6Ih¬ÛÐò\x12ÿ\x130'
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-8') as fin:
	fin.seek(297)
	fin.read(20)

	
297
Traceback (most recent call last):
  File "<pyshell#731>", line 3, in <module>
    fin.read(20)
  File "C:\ProgramData\Anaconda3\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x95 in position 2: invalid start byte
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='unicode') as fin:
	fin.seek(297)
	fin.read(20)

	
Traceback (most recent call last):
  File "<pyshell#734>", line 1, in <module>
    with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='unicode') as fin:
LookupError: unknown encoding: unicode
>>> 

>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-10') as fin:
	fin.seek(297)
	fin.read(20)

	
Traceback (most recent call last):
  File "<pyshell#737>", line 1, in <module>
    with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-10') as fin:
LookupError: unknown encoding: utf-10
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-16') as fin:
	fin.seek(297)
	fin.read(20)

	
297
Traceback (most recent call last):
  File "<pyshell#740>", line 3, in <module>
    fin.read(20)
  File "C:\ProgramData\Anaconda3\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  File "C:\ProgramData\Anaconda3\lib\encodings\utf_16.py", line 69, in _buffer_decode
    return self.decoder(input, self.errors, final)
UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 12-13: illegal UTF-16 surrogate
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-32') as fin:
	fin.seek(297)
	fin.read(20)

	
297
Traceback (most recent call last):
  File "<pyshell#743>", line 3, in <module>
    fin.read(20)
  File "C:\ProgramData\Anaconda3\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  File "C:\ProgramData\Anaconda3\lib\encodings\utf_32.py", line 64, in _buffer_decode
    return self.decoder(input, self.errors, final)
UnicodeDecodeError: 'utf-32-le' codec can't decode bytes in position 0-3: code point not in range(0x110000)
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-128') as fin:
	fin.seek(297)
	fin.read(20)

	
Traceback (most recent call last):
  File "<pyshell#746>", line 1, in <module>
    with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-128') as fin:
LookupError: unknown encoding: utf-128
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-64') as fin:
	fin.seek(297)
	fin.read(20)

	
Traceback (most recent call last):
  File "<pyshell#749>", line 1, in <module>
    with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-64') as fin:
LookupError: unknown encoding: utf-64
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf_8_sig') as fin:
	fin.seek(297)
	fin.read(20)

	
297
Traceback (most recent call last):
  File "<pyshell#752>", line 3, in <module>
    fin.read(20)
  File "C:\ProgramData\Anaconda3\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  File "C:\ProgramData\Anaconda3\lib\encodings\utf_8_sig.py", line 69, in _buffer_decode
    return codecs.utf_8_decode(input, errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x95 in position 2: invalid start byte
>>> 
>>> with open("Siao Lung's Courses\Siao Lung's School Courses\My 12th Grade Book.zip", encoding='utf-16') as fin:
	fin.seek(297)
	fin.read(20)

	
297
Traceback (most recent call last):
  File "<pyshell#755>", line 3, in <module>
    fin.read(20)
  File "C:\ProgramData\Anaconda3\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  File "C:\ProgramData\Anaconda3\lib\encodings\utf_16.py", line 69, in _buffer_decode
    return self.decoder(input, self.errors, final)
UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 12-13: illegal UTF-16 surrogate
>>> 

>>> 

>>> def prime_factors(num):
	index, factors = 2, []

	while index**2 <= num:
		if num % index: index += 1
		else:
			num //= index
			factors += [index]

	if num > 1: factors += [num]

	return factors

>>> 
>>> 

>>> '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', ')
['1', '2', '3', '4', '5', '6', '8', '9', '10', '12']

>>> 

>>> 

>>> mmin.dstatial(int, '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
>>> 
>>> 

>>> nums = []
>>> 
>>> while len(nums) < n:
	
KeyboardInterrupt
>>> 
>>> num = 0
>>> 
>>> num, nums = 0, []
>>> 
>>> while len(nums) < n:
	num += 1
	if prime_factors(num): nums += [num]
KeyboardInterrupt
>>> 
>>> prime_factors(1)
[]
>>> prime_factors(2)
[2]
>>> 
>>> mmin.dstatial(lambda x: int(prime_factors(x)), '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
Traceback (most recent call last):
  File "<pyshell#782>", line 1, in <module>
    mmin.dstatial(lambda x: int(prime_factors(x)), '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
  File "C:\ProgramData\Anaconda3\lib\mymodule\__init__.py", line 286, in dstatial
    the_new_list.append(the_function(tla))
  File "<pyshell#782>", line 1, in <lambda>
    mmin.dstatial(lambda x: int(prime_factors(x)), '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
  File "<pyshell#759>", line 4, in prime_factors
    while index**2 <= num:
TypeError: '<=' not supported between instances of 'int' and 'str'
>>> 
>>> mmin.dstatial(lambda x: prime_factors(int(x)), '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
[[], [2], [3], [2, 2], [5], [2, 3], [2, 2, 2], [3, 3], [2, 5], [2, 2, 3]]
>>> 
>>> 

>>> mmin.dstatial(lambda x: sorted(set(prime_factors(int(x)))), '1, 2, 3, 4, 5, 6, 8, 9, 10, 12'.split(', '))
[[], [2], [3], [2], [5], [2, 3], [2], [3], [2, 5], [2, 3]]

>>> 

>>> mma.covto_or
<function compare_one_value_to_others_or at 0x00000250D65EA0D0>
>>> 

>>> 

>>> data = [0, 2, 3, 5]; lendata, digits = len(data), 3
>>> 
>>> 

>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums

	
Traceback (most recent call last):
  File "<pyshell#797>", line 1, in <module>
    for i in range(cp, lendata**digits):
NameError: name 'cp' is not defined
>>> 
>>> cp = 0
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums

	
[0, 0, 0]
[0, 0, 1]
[0, 0, 2]
[0, 0, 3]
[0, 1, 0]
[0, 1, 1]
[0, 1, 2]
[0, 1, 3]
[0, 2, 0]
[0, 2, 1]
[0, 2, 2]
[0, 2, 3]
[0, 3, 0]
[0, 3, 1]
[0, 3, 2]
[0, 3, 3]
[1, 0, 0]
[1, 0, 1]
[1, 0, 2]
[1, 0, 3]
[1, 1, 0]
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 2, 0]
[1, 2, 1]
[1, 2, 2]
[1, 2, 3]
[1, 3, 0]
[1, 3, 1]
[1, 3, 2]
[1, 3, 3]
[2, 0, 0]
[2, 0, 1]
[2, 0, 2]
[2, 0, 3]
[2, 1, 0]
[2, 1, 1]
[2, 1, 2]
[2, 1, 3]
[2, 2, 0]
[2, 2, 1]
[2, 2, 2]
[2, 2, 3]
[2, 3, 0]
[2, 3, 1]
[2, 3, 2]
[2, 3, 3]
[3, 0, 0]
[3, 0, 1]
[3, 0, 2]
[3, 0, 3]
[3, 1, 0]
[3, 1, 1]
[3, 1, 2]
[3, 1, 3]
[3, 2, 0]
[3, 2, 1]
[3, 2, 2]
[3, 2, 3]
[3, 3, 0]
[3, 3, 1]
[3, 3, 2]
[3, 3, 3]
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums.remove(0)
	nums

	
[0, 0]
[0, 1]
[0, 2]
[0, 3]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[2, 0]
[2, 1]
[2, 2]
[2, 3]
[3, 0]
[3, 1]
[3, 2]
[3, 3]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[1, 1]
Traceback (most recent call last):
  File "<pyshell#806>", line 3, in <module>
    nums.remove(0)
ValueError: list.remove(x): x not in list
>>> 
>>> help(nums.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> 

>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums.remove(nums.find(0))
	nums

	
Traceback (most recent call last):
  File "<pyshell#811>", line 3, in <module>
    nums.remove(nums.find(0))
AttributeError: 'list' object has no attribute 'find'
>>> 
>>> cp
0
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums.remove(nums.index(0))
	nums

	
[0, 0]
[0, 1]
[0, 2]
[0, 3]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[2, 0]
[2, 1]
[2, 2]
[2, 3]
[3, 0]
[3, 1]
[3, 2]
[3, 3]
[0, 0]
[0, 1]
[0, 2]
[0, 3]
Traceback (most recent call last):
  File "<pyshell#816>", line 3, in <module>
    nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 

>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(nums.index(0))
	nums

	
[0, 0]
[0, 1]
[0, 2]
[0, 3]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[2, 0]
[2, 1]
[2, 2]
[2, 3]
[3, 0]
[3, 1]
[3, 2]
[3, 3]
[0, 0]
[0, 1]
[0, 2]
[0, 3]
Traceback (most recent call last):
  File "<pyshell#819>", line 3, in <module>
    if 0 in nums: nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> nums
[1, 1, 0]
>>> 
>>> nums.index(0)
2
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(nums.index(0))
	sorted(set(nums))

	
[0]
[0, 1]
[0, 2]
[0, 3]
[0, 1]
[1]
[1, 2]
[1, 3]
[0, 2]
[1, 2]
[2]
[2, 3]
[0, 3]
[1, 3]
[2, 3]
[3]
[0]
[0, 1]
[0, 2]
[0, 3]
Traceback (most recent call last):
  File "<pyshell#826>", line 3, in <module>
    if 0 in nums: nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> 

>>> 

>>> cp
0
>>> 
>>> 

>>> nums.index(0)
2
>>> 
>>> nums
[1, 1, 0]
>>> 
>>> nums.remove(nums.index(0))
Traceback (most recent call last):
  File "<pyshell#837>", line 1, in <module>
    nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> nums.remove(2)
Traceback (most recent call last):
  File "<pyshell#839>", line 1, in <module>
    nums.remove(2)
ValueError: list.remove(x): x not in list
>>> 
>>> nums.index(0)
2
>>> 
>>> nums
[1, 1, 0]
>>> data = mmin.dstatial(str, [0, 2, 3, 5]); lendata, digits = len(data), 3
>>> 

>>> 

>>> for i in range(cp, lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(nums.index(0))
	sorted(set(nums))

	
[0]
[0, 1]
[0, 2]
[0, 3]
[0, 1]
[1]
[1, 2]
[1, 3]
[0, 2]
[1, 2]
[2]
[2, 3]
[0, 3]
[1, 3]
[2, 3]
[3]
[0]
[0, 1]
[0, 2]
[0, 3]
Traceback (most recent call last):
  File "<pyshell#848>", line 3, in <module>
    if 0 in nums: nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> data = [0, 2, 3, 5]; lendata, digits = len(data), 3
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(nums.index(0))
	sorted(set(nums))

	
[0]
[0, 2]
[0, 3]
[0, 5]
[0, 2]
[2]
[2, 3]
[2, 5]
[0, 3]
[2, 3]
[3]
[3, 5]
[0, 5]
[2, 5]
[3, 5]
[5]
Traceback (most recent call last):
  File "<pyshell#853>", line 3, in <module>
    if 0 in nums: nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(nums.index(0))
	sorted(set(nums))

	
[0]
[0, 2]
[0, 3]
[0, 5]
[0, 2]
[2]
[2, 3]
[2, 5]
[0, 3]
[2, 3]
[3]
[3, 5]
[0, 5]
[2, 5]
[3, 5]
[5]
Traceback (most recent call last):
  File "<pyshell#856>", line 3, in <module>
    if 0 in nums: nums.remove(nums.index(0))
ValueError: list.remove(x): x not in list
>>> 
>>> nums
[2, 0, 0]
>>> 0 in nums
True
>>> 
>>> nums.index(0)
1
>>> nums.remove(1)
Traceback (most recent call last):
  File "<pyshell#862>", line 1, in <module>
    nums.remove(1)
ValueError: list.remove(x): x not in list
>>> nums.remove(0)
>>> nums
[2, 0]
>>> 
>>> nums.remove(1)
Traceback (most recent call last):
  File "<pyshell#866>", line 1, in <module>
    nums.remove(1)
ValueError: list.remove(x): x not in list
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
	if 0 in nums: nums.remove(0)
	sorted(set(nums))

	
[0]
[0, 2]
[0, 3]
[0, 5]
[0, 2]
[2]
[2, 3]
[2, 5]
[0, 3]
[2, 3]
[3]
[3, 5]
[0, 5]
[2, 5]
[3, 5]
[5]
[0, 2]
[2]
[2, 3]
[2, 5]
[2]
[2]
[2, 3]
[2, 5]
[2, 3]
[2, 3]
[2, 3]
[2, 3, 5]
[2, 5]
[2, 5]
[2, 3, 5]
[2, 5]
[0, 3]
[2, 3]
[3]
[3, 5]
[2, 3]
[2, 3]
[2, 3]
[2, 3, 5]
[3]
[2, 3]
[3]
[3, 5]
[3, 5]
[2, 3, 5]
[3, 5]
[3, 5]
[0, 5]
[2, 5]
[3, 5]
[5]
[2, 5]
[2, 5]
[2, 3, 5]
[2, 5]
[3, 5]
[2, 3, 5]
[3, 5]
[3, 5]
[5]
[2, 5]
[3, 5]
[5]
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
	while 0 in nums: nums.remove(0)
	sorted(set(nums))

	
[]
[2]
[3]
[5]
[2]
[2]
[2, 3]
[2, 5]
[3]
[2, 3]
[3]
[3, 5]
[5]
[2, 5]
[3, 5]
[5]
[2]
[2]
[2, 3]
[2, 5]
[2]
[2]
[2, 3]
[2, 5]
[2, 3]
[2, 3]
[2, 3]
[2, 3, 5]
[2, 5]
[2, 5]
[2, 3, 5]
[2, 5]
[3]
[2, 3]
[3]
[3, 5]
[2, 3]
[2, 3]
[2, 3]
[2, 3, 5]
[3]
[2, 3]
[3]
[3, 5]
[3, 5]
[2, 3, 5]
[3, 5]
[3, 5]
[5]
[2, 5]
[3, 5]
[5]
[2, 5]
[2, 5]
[2, 3, 5]
[2, 5]
[3, 5]
[2, 3, 5]
[3, 5]
[3, 5]
[5]
[2, 5]
[3, 5]
[5]
>>> 

>>> numslist = []
>>> 
>>> for i in range(cp, lendata**digits):
	nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
	while 0 in nums: nums.remove(0)
	result = sorted(set(nums))
	if result not in numslist: numslist += [result]

	
>>> 
>>> numslist
[[], [2], [3], [5], [2, 3], [2, 5], [3, 5], [2, 3, 5]]
>>> 
>>> 

>>> while len(nums) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: nums += [num]
KeyboardInterrupt
>>> nums
[5, 5, 5]

>>> numswanted =[]
>>> while len(nums) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
Traceback (most recent call last):
  File "<pyshell#885>", line 1, in <module>
    while len(nums) < n:
NameError: name 'n' is not defined
>>> 
>>> n = 10
>>> 
>>> numswanted
[]
>>> 
>>> numswanted = []
>>> 
>>> while len(nums) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
Traceback (most recent call last):
  File "<pyshell#894>", line 1, in <module>
    while len(nums) < n:
KeyboardInterrupt
>>> 

>>> numswanted
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960, 972, 1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440, 1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000, 2025, 2048, 2160, 2187, 2250, 2304, 2400, 2430, 2500, 2560, 2592, 2700, 2880, 2916, 3000, 3072, 3125, 3200, 3240, 3375, 3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096, 4320, 4374, 4500, 4608, 4800, 4860, 5000, 5120, 5184, 5400, 5625, 5760, 5832, 6000, 6075, 6144, 6250, 6400, 6480, 6561, 6750, 6912, 7200, 7290, 7500, 7680, 7776, 8000, 8100, 8192, 8640, 8748, 9000, 9216, 9375, 9600, 9720, 10000, 10125, 10240, 10368, 10800, 10935, 11250, 11520, 11664, 12000, 12150, 12288, 12500, 12800, 12960, 13122, 13500, 13824, 14400, 14580, 15000, 15360, 15552, 15625, 16000, 16200, 16384, 16875, 17280, 17496, 18000, 18225, 18432, 18750, 19200, 19440, 19683, 20000, 20250, 20480, 20736, 21600, 21870, 22500, 23040, 23328, 24000, 24300, 24576, 25000, 25600, 25920, 26244, 27000, 27648, 28125, 28800, 29160, 30000, 30375, 30720, 31104, 31250, 32000, 32400, 32768, 32805, 33750, 34560, 34992, 36000, 36450, 36864, 37500, 38400, 38880, 39366, 40000, 40500, 40960, 41472, 43200, 43740, 45000, 46080, 46656, 46875, 48000, 48600, 49152, 50000, 50625, 51200, 51840, 52488, 54000, 54675, 55296, 56250, 57600, 58320, 59049, 60000, 60750, 61440, 62208, 62500, 64000, 64800, 65536, 65610, 67500, 69120, 69984, 72000, 72900, 73728, 75000, 76800, 77760, 78125, 78732, 80000, 81000, 81920, 82944, 84375, 86400, 87480, 90000, 91125, 92160, 93312, 93750, 96000, 97200, 98304, 98415, 100000, 101250, 102400, 103680, 104976, 108000, 109350, 110592, 112500, 115200, 116640, 118098, 120000, 121500, 122880, 124416, 125000, 128000, 129600, 131072, 131220, 135000, 138240, 139968, 140625, 144000]
>>> 
>>> 

>>> n = 10
>>> while len(numswanted) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]
KeyboardInterrupt
>>> 
>>> while len(numswanted) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
>>> numswanted
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960, 972, 1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440, 1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000, 2025, 2048, 2160, 2187, 2250, 2304, 2400, 2430, 2500, 2560, 2592, 2700, 2880, 2916, 3000, 3072, 3125, 3200, 3240, 3375, 3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096, 4320, 4374, 4500, 4608, 4800, 4860, 5000, 5120, 5184, 5400, 5625, 5760, 5832, 6000, 6075, 6144, 6250, 6400, 6480, 6561, 6750, 6912, 7200, 7290, 7500, 7680, 7776, 8000, 8100, 8192, 8640, 8748, 9000, 9216, 9375, 9600, 9720, 10000, 10125, 10240, 10368, 10800, 10935, 11250, 11520, 11664, 12000, 12150, 12288, 12500, 12800, 12960, 13122, 13500, 13824, 14400, 14580, 15000, 15360, 15552, 15625, 16000, 16200, 16384, 16875, 17280, 17496, 18000, 18225, 18432, 18750, 19200, 19440, 19683, 20000, 20250, 20480, 20736, 21600, 21870, 22500, 23040, 23328, 24000, 24300, 24576, 25000, 25600, 25920, 26244, 27000, 27648, 28125, 28800, 29160, 30000, 30375, 30720, 31104, 31250, 32000, 32400, 32768, 32805, 33750, 34560, 34992, 36000, 36450, 36864, 37500, 38400, 38880, 39366, 40000, 40500, 40960, 41472, 43200, 43740, 45000, 46080, 46656, 46875, 48000, 48600, 49152, 50000, 50625, 51200, 51840, 52488, 54000, 54675, 55296, 56250, 57600, 58320, 59049, 60000, 60750, 61440, 62208, 62500, 64000, 64800, 65536, 65610, 67500, 69120, 69984, 72000, 72900, 73728, 75000, 76800, 77760, 78125, 78732, 80000, 81000, 81920, 82944, 84375, 86400, 87480, 90000, 91125, 92160, 93312, 93750, 96000, 97200, 98304, 98415, 100000, 101250, 102400, 103680, 104976, 108000, 109350, 110592, 112500, 115200, 116640, 118098, 120000, 121500, 122880, 124416, 125000, 128000, 129600, 131072, 131220, 135000, 138240, 139968, 140625, 144000]
>>> 
>>> numswanted = []
>>> 
>>> numswanted, n = [], 10
>>> 
>>> while len(numswanted) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
>>> numswanted
[145800, 147456, 150000, 151875, 153600, 155520, 156250, 157464, 160000, 162000]
>>> 
>>> numswanted, n, num = [], 10, 0
>>> 
>>> while len(numswanted) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
>>> numswanted
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
>>> 

>>> numslist
[[], [2], [3], [5], [2, 3], [2, 5], [3, 5], [2, 3, 5]]
>>> 
>>> ppc.copy(str(numslist))
>>> 
>>> numswanted, n, num = [], 218, 0
>>> 
>>> while len(numswanted) < n:
	num += 1
	if sorted(set(prime_factors(num))) in numslist: numswanted += [num]

	
>>> numswanted
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960, 972, 1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440, 1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000, 2025, 2048, 2160, 2187, 2250, 2304, 2400, 2430, 2500, 2560, 2592, 2700, 2880, 2916, 3000, 3072, 3125, 3200, 3240, 3375, 3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096, 4320, 4374, 4500, 4608, 4800, 4860, 5000, 5120, 5184, 5400, 5625, 5760, 5832, 6000, 6075, 6144, 6250, 6400, 6480, 6561, 6750, 6912, 7200, 7290, 7500, 7680, 7776, 8000, 8100, 8192, 8640, 8748, 9000, 9216, 9375, 9600, 9720, 10000, 10125, 10240, 10368, 10800, 10935, 11250, 11520, 11664, 12000, 12150, 12288, 12500, 12800, 12960, 13122, 13500, 13824, 14400, 14580, 15000, 15360, 15552, 15625, 16000, 16200, 16384, 16875, 17280, 17496, 18000, 18225, 18432, 18750, 19200, 19440, 19683, 20000, 20250, 20480, 20736, 21600, 21870, 22500]
>>> 
>>> class Solution:
	def nthUglyNumber(self, n: int) -> int:
		numswanted, num, numslist = [], 0, [[], [2], [3], [5], [2, 3], [2, 5], [3, 5], [2, 3, 5]]
		
		while len(numswanted) < n:
			num += 1
			if sorted(set(prime_factors(num))) in numslist: numswanted += [num]
			
		return numswanted[-1]

	
>>> Solution().nthUglyNumber(n)
22500
>>> 

>>> Solution().nthUglyNumber(216)
21600
>>> 

>>> 
