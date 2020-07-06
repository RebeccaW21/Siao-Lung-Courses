Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from PolyResearchModules import *
>>> ['''5 5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 4 4 
5 4 3 3 3 3 3 3 3 4 
5 4 3 2 2 2 2 2 3 4 
5 4 3 2 1 1 1 2 3 4 
5 4 3 2 1 0 1 2 3 4 
5 4 3 2 1 1 1 2 3 4 
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4 
5 4 4 4 4 4 4 4 4 4''']
['5 5 5 5 5 5 5 5 5 5 \n5 4 4 4 4 4 4 4 4 4 \n5 4 3 3 3 3 3 3 3 4 \n5 4 3 2 2 2 2 2 3 4 \n5 4 3 2 1 1 1 2 3 4 \n5 4 3 2 1 0 1 2 3 4 \n5 4 3 2 1 1 1 2 3 4 \n5 4 3 2 2 2 2 2 3 4\n5 4 3 3 3 3 3 3 3 4 \n5 4 4 4 4 4 4 4 4 4']

>>> [isi.split(' ') for isi in '''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4'''.split('\n')]
[['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'], ['5', '4', '4', '4', '4', '4', '4', '4', '4', '4'], ['5', '4', '3', '3', '3', '3', '3', '3', '3', '4'], ['5', '4', '3', '2', '2', '2', '2', '2', '3', '4'], ['5', '4', '3', '2', '1', '1', '1', '2', '3', '4'], ['5', '4', '3', '2', '1', '0', '1', '2', '3', '4'], ['5', '4', '3', '2', '1', '1', '1', '2', '3', '4'], ['5', '4', '3', '2', '2', '2', '2', '2', '3', '4'], ['5', '4', '3', '3', '3', '3', '3', '3', '3', '4'], ['5', '4', '4', '4', '4', '4', '4', '4', '4', '4']]

>>> 
>>> ere = np.array([isi.split(' ') for isi in '''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4'''.split('\n')])
>>> 
>>> ere
array([['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
       ['5', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
       ['5', '4', '3', '3', '3', '3', '3', '3', '3', '4'],
       ['5', '4', '3', '2', '2', '2', '2', '2', '3', '4'],
       ['5', '4', '3', '2', '1', '1', '1', '2', '3', '4'],
       ['5', '4', '3', '2', '1', '0', '1', '2', '3', '4'],
       ['5', '4', '3', '2', '1', '1', '1', '2', '3', '4'],
       ['5', '4', '3', '2', '2', '2', '2', '2', '3', '4'],
       ['5', '4', '3', '3', '3', '3', '3', '3', '3', '4'],
       ['5', '4', '4', '4', '4', '4', '4', '4', '4', '4']], dtype='<U1')
>>> 
>>> 
>>> ere = np.array([isi.split(' ') for isi in '''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4'''.split('\n')], dtype=np.int64)
>>> 
>>> ere
array([[5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4]], dtype=int64)
>>> 
>>> 
>>> ere-5
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 0, -1, -2, -2, -2, -2, -2, -2, -2, -1],
       [ 0, -1, -2, -3, -3, -3, -3, -3, -2, -1],
       [ 0, -1, -2, -3, -4, -4, -4, -3, -2, -1],
       [ 0, -1, -2, -3, -4, -5, -4, -3, -2, -1],
       [ 0, -1, -2, -3, -4, -4, -4, -3, -2, -1],
       [ 0, -1, -2, -3, -3, -3, -3, -3, -2, -1],
       [ 0, -1, -2, -2, -2, -2, -2, -2, -2, -1],
       [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]], dtype=int64)
>>> 
>>> ere[0]
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=int64)
>>> 
>>> np.copy(ere[0])
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=int64)

>>> isi
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    isi
NameError: name 'isi' is not defined

>>> isi = np.copy(ere[0])
>>> isi
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=int64)
>>> 
>>> isi[10]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    isi[10]
IndexError: index 10 is out of bounds for axis 0 with size 10
>>> 
>>> r, c, ci, cj = 10, 10, 5, 5
>>> 
>>> isi
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=int64)
>>> 
>>> row0 = np.copy(ere[0])
>>> 
>>> row0 = [ci]*c
>>> row
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    row
NameError: name 'row' is not defined
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

>>> row0[r]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    row0[r]
IndexError: list index out of range

>>> row1 = row0[:]
>>> row1
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> row1
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> row1[1:r]
[5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1[1:r-1]
[5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> row1[1:r-1] = [ci]*c-2
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    row1[1:r-1] = [ci]*c-2
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> 
>>> row1[1:r-1] = [ci]*(c-2)
>>> row1
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> row0 = [ci]*c
>>> row1 = row0[:]
>>> row1[1:r-1] = [ci-1]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 5]
>>> 
>>> row0 = [ci]*c
>>> row1 = row0[:]
>>> row1[1:r] = [ci-1]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4]
>>> 
>>> row0 = [ci]*c
>>> row1 = row0[:]
>>> row1[1:r] = [ci-1]*(c-`)
SyntaxError: invalid syntax
>>> 
>>> row0 = [ci]*c
>>> row1 = row0[:]
>>> row1[1:r] = [ci-1]*(c-1)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> 
>>> row2 = row1[:]
>>> row2[2:r] = [ci-2]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> row2
[5, 4, 3, 3, 3, 3, 3, 3, 3, 3]
>>> 
>>> row2 = row1[:]
>>> row2[1:r] = [ci-2]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> row2
[5, 3, 3, 3, 3, 3, 3, 3, 3]
>>> 
>>> row2 = row1[:]
>>> row2[1:r-1] = [ci-2]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> row2
[5, 3, 3, 3, 3, 3, 3, 3, 3, 4]
>>> 
>>> row2 = row1[:]
>>> row2[2:r-1] = [ci-2]*(c-2)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> row2
[5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4]
>>> 
>>> row2 = row1[:]
>>> row2[2:r-1] = [ci-2]*(c-3)
>>> 
>>> row0
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> row1
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> row2
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
>>> 
>>> row0 = [ci]*c
>>> 
>>> row = [ci]*c
>>> 
>>> for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row

	
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> cj
5
>>> 
>>> for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row

	
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row

	
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> row = [ci]*c
>>> row
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row
	
KeyboardInterrupt
>>> 
>>> exec('''

print(row)
for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> exec('''

print(row)
for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	row

''')
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> 
>>> exec('''

row = [ci]*c
print(row)
for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> 
>>> for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)

	
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> for i in range(r//2):
	row[i-1:r+i] = [ci+1+i]*(c+1+2*i)
	print(row)

	
[5, 4, 3, 2, 1, 0, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
>>> 
>>> row
[7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
>>> 
>>> for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)

	
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 3, 3, 3, 3, 3, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 2, 2, 2, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 1, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
>>> 
>>> exec('''

row = [ci]*c
print(row)
for i in range(r):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> for i in range(r):
	row[i-1:r+i] = [ci+1+i]*(c-1-2*i)
	print(row)

	
[5, 4, 3, 2, 1, 0, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6]
[7, 8, 8, 8, 8, 8, 6, 6]
[7, 8, 9, 9, 9]
[7, 8, 9, 10]
[7, 8, 9, 10]
[7, 8, 9, 10]
[7, 8, 9, 10]
[7, 8, 9, 10]
[7, 8, 9, 10]
>>> 
>>> exec('''

row = [ci]*c
print(row)
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row]

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> 
>>> result
[[5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]]
>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> result
[[5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]]

>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for r in result[::-1]: r

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for r in result[::-1]: print(r)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "<pyshell#167>", line 14, in <module>
    ''')
  File "<string>", line 7, in <module>
TypeError: unsupported operand type(s) for //: 'list' and 'int'
>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[::-1]: print(r)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "<pyshell#169>", line 14, in <module>
    ''')
  File "<string>", line 7, in <module>
TypeError: unsupported operand type(s) for //: 'list' and 'int'
>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
Traceback (most recent call last):
  File "<pyshell#171>", line 14, in <module>
    ''')
  File "<string>", line 7, in <module>

TypeError: unsupported operand type(s) for //: 'list' and 'int'
>>> r, c, ci, cj = 10, 10, 5, 5
>>> 
>>> exec('''

row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = []
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[1::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[1::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]

[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

#for content in result[::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[:-1:-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]

[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

#for content in result[:-1:-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

>>> result
[[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]]
>>> 
>>> result[1::-1]
[[5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> result[:-1:-1]
[]
>>> 
>>> result[:-1]
[[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4]]
>>> 
>>> result[::-1]
[[5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> 
>>> result[::-1][1:]
[[5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> 
>>> result[-1::-1]
[[5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> 
>>> result[-2::-1]
[[5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(row)
	result += [row[:]]

for content in result[-2::-1]: print(content)

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
[5, 4, 3, 2, 1, 1, 1, 2, 3, 4]
[5, 4, 3, 2, 2, 2, 2, 2, 3, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 4]
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

>>> 
>>> content
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> str(content)
'[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]'
>>> 
>>> str(content)[1:-1]
'5, 5, 5, 5, 5, 5, 5, 5, 5, 5'
>>> str(content)[1:-1].replace(', ',' ')
'5 5 5 5 5 5 5 5 5 5'
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(row)

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' ')

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
Traceback (most recent call last):
  File "<pyshell#213>", line 15, in <module>
    ''')
  File "<string>", line 7
    result = [row[:]]
         ^
SyntaxError: invalid syntax
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> dir()
['Abs', 'AccumBounds', 'Add', 'Adjoint', 'AlgebraicField', 'AlgebraicNumber', 'And', 'AppliedPredicate', 'Array', 'AssumptionsContext', 'Atom', 'AtomicExpr', 'BasePolynomialError', 'Basic', 'BlockDiagMatrix', 'BlockMatrix', 'C', 'CC', 'CRootOf', 'Catalan', 'Chi', 'Ci', 'Circle', 'ClassRegistry', 'CoercionFailed', 'Complement', 'ComplexField', 'ComplexRegion', 'ComplexRootOf', 'Complexes', 'ComputationFailed', 'ConditionSet', 'Contains', 'CosineTransform', 'Curve', 'DeferredVector', 'DenseNDimArray', 'Derivative', 'Determinant', 'DiagonalMatrix', 'DiagonalOf', 'Dict', 'DiracDelta', 'Domain', 'DomainError', 'DotProduct', 'Dummy', 'E', 'E1', 'EPath', 'EX', 'Ei', 'Eijk', 'Ellipse', 'EmptySequence', 'EmptySet', 'Eq', 'Equality', 'Equivalent', 'EulerGamma', 'EvaluationFailed', 'ExactQuotientFailed', 'Expr', 'ExpressionDomain', 'ExtraneousFactors', 'FF', 'FF_gmpy', 'FF_python', 'FU', 'FallingFactorial', 'FiniteField', 'FiniteSet', 'FlagError', 'Float', 'FourierTransform', 'FractionField', 'Function', 'FunctionClass', 'FunctionMatrix', 'GF', 'GMPYFiniteField', 'GMPYIntegerRing', 'GMPYRationalField', 'Ge', 'GeneratorsError', 'GeneratorsNeeded', 'GeometryError', 'GoldenRatio', 'GramSchmidt', 'GreaterThan', 'GroebnerBasis', 'Gt', 'HadamardProduct', 'HankelTransform', 'Heaviside', 'HeuristicGCDFailed', 'HomomorphismFailed', 'I', 'ITE', 'Id', 'Identity', 'Idx', 'ImageSet', 'ImmutableDenseMatrix', 'ImmutableDenseNDimArray', 'ImmutableMatrix', 'ImmutableSparseMatrix', 'ImmutableSparseNDimArray', 'Implies', 'Indexed', 'IndexedBase', 'Integer', 'IntegerRing', 'Integers', 'Integral', 'Intersection', 'Interval', 'Inverse', 'InverseCosineTransform', 'InverseFourierTransform', 'InverseHankelTransform', 'InverseLaplaceTransform', 'InverseMellinTransform', 'InverseSineTransform', 'IsomorphismFailed', 'KroneckerDelta', 'KroneckerProduct', 'LC', 'LM', 'LT', 'Lambda', 'LambertW', 'LaplaceTransform', 'Le', 'LessThan', 'LeviCivita', 'Li', 'Limit', 'Line', 'Line2D', 'Line3D', 'Lt', 'MatAdd', 'MatMul', 'MatPow', 'Matrix', 'MatrixBase', 'MatrixExpr', 'MatrixSlice', 'MatrixSymbol', 'Max', 'MellinTransform', 'Min', 'Mod', 'Monomial', 'Mul', 'MultivariatePolynomialError', 'MutableDenseMatrix', 'MutableDenseNDimArray', 'MutableMatrix', 'MutableSparseMatrix', 'MutableSparseNDimArray', 'N', 'NDimArray', 'Nand', 'Naturals', 'Naturals0', 'Ne', 'NonSquareMatrixError', 'Nor', 'Not', 'NotAlgebraic', 'NotInvertible', 'NotReversible', 'Number', 'NumberSymbol', 'O', 'OmegaPower', 'OperationNotSupported', 'OptionError', 'Options', 'Or', 'Order', 'Ordinal', 'POSform', 'Parabola', 'Piecewise', 'Plane', 'Point', 'Point2D', 'Point3D', 'PoleError', 'PolificationFailed', 'Poly', 'Polygon', 'PolynomialDivisionFailed', 'PolynomialError', 'PolynomialRing', 'Pow', 'PrecisionExhausted', 'Predicate', 'Product', 'ProductSet', 'PurePoly', 'PythonFiniteField', 'PythonIntegerRing', 'PythonRationalField', 'Q', 'QQ', 'QQ_gmpy', 'QQ_python', 'Quaternion', 'RR', 'Range', 'Rational', 'RationalField', 'Ray', 'Ray2D', 'Ray3D', 'RealField', 'RealNumber', 'Reals', 'RefinementFailed', 'RegularPolygon', 'Rel', 'RisingFactorial', 'RootOf', 'RootSum', 'S', 'SOPform', 'SYMPY_DEBUG', 'Segment', 'Segment2D', 'Segment3D', 'SeqAdd', 'SeqFormula', 'SeqMul', 'SeqPer', 'Set', 'ShapeError', 'Shi', 'Si', 'Sieve', 'SineTransform', 'SingularityFunction', 'SparseMatrix', 'SparseNDimArray', 'StrPrinter', 'StrictGreaterThan', 'StrictLessThan', 'Subs', 'Sum', 'Symbol', 'SymmetricDifference', 'SympifyError', 'TableForm', 'Trace', 'Transpose', 'Triangle', 'TribonacciConstant', 'Tuple', 'Unequality', 'UnevaluatedExpr', 'UnificationFailed', 'Union', 'UnivariatePolynomialError', 'UniversalSet', 'Wild', 'WildFunction', 'Xor', 'Ynm', 'Ynm_c', 'ZZ', 'ZZ_gmpy', 'ZZ_python', 'ZeroMatrix', 'Znm', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'abundance', 'acos', 'acosh', 'acot', 'acoth', 'acsc', 'acsch', 'add', 'adjoint', 'airyai', 'airyaiprime', 'airybi', 'airybiprime', 'algebras', 'apart', 'apart_list', 'appellf1', 'apply_finite_diff', 'are_similar', 'arg', 'arity', 'array', 'as_finite_diff', 'asec', 'asech', 'asin', 'asinh', 'ask', 'ask_generated', 'assemble_partfrac_list', 'assoc_laguerre', 'assoc_legendre', 'assume', 'assuming', 'assumptions', 'atan', 'atan2', 'atanh', 'basic', 'bell', 'bernoulli', 'besseli', 'besselj', 'besselk', 'besselsimp', 'bessely', 'beta', 'binomial', 'binomial_coefficients', 'binomial_coefficients_list', 'bivariate', 'block_collapse', 'blockcut', 'bool_map', 'boolalg', 'bottom_up', 'bspline_basis', 'bspline_basis_set', 'c', 'cache', 'cacheit', 'calculus', 'cancel', 'capture', 'carmichael', 'cartes', 'casoratian', 'catalan', 'cbrt', 'ccode', 'ceiling', 'centroid', 'chebyshevt', 'chebyshevt_poly', 'chebyshevt_root', 'chebyshevu', 'chebyshevu_poly', 'chebyshevu_root', 'check_assumptions', 'checkodesol', 'checkpdesol', 'checksol', 'ci', 'cj', 'class_registry', 'classify_ode', 'classify_pde', 'closest_points', 'codegen', 'cofactors', 'collect', 'collect_const', 'combinatorial', 'combinatorics', 'combsimp', 'common', 'comp', 'compatibility', 'compose', 'composite', 'compositepi', 'concrete', 'conditionset', 'conjugate', 'construct_domain', 'containers', 'contains', 'content', 'continued_fraction', 'continued_fraction_convergents', 'continued_fraction_iterator', 'continued_fraction_periodic', 'continued_fraction_reduce', 'convex_hull', 'convolution', 'convolutions', 'core', 'coreerrors', 'cos', 'cosh', 'cosine_transform', 'cot', 'coth', 'count_ops', 'count_roots', 'covering_product', 'csc', 'csch', 'cse', 'cse_main', 'cse_opts', 'curve', 'cxxcode', 'cycle_length', 'cyclotomic_poly', 'decompogen', 'decompose', 'decorator', 'decorators', 'default_sort_key', 'deg', 'degree', 'degree_list', 'denom', 'dense', 'deprecated', 'derive_by_array', 'det', 'det_quick', 'deutils', 'diag', 'dict_merge', 'diff', 'difference_delta', 'differentiate_finite', 'digamma', 'diophantine', 'dirichlet_eta', 'discrete', 'discrete_log', 'discriminant', 'div', 'divisor_count', 'divisor_sigma', 'divisors', 'doctest', 'dotprint', 'dsolve', 'ef', 'egyptian_fraction', 'elementary', 'ellipse', 'elliptic_e', 'elliptic_f', 'elliptic_k', 'elliptic_pi', 'entity', 'enumerative', 'epath', 'epathtools', 'ere', 'erf', 'erf2', 'erf2inv', 'erfc', 'erfcinv', 'erfi', 'erfinv', 'euler', 'euler_equations', 'evalf', 'evaluate', 'exceptions', 'exp', 'exp_polar', 'expand', 'expand_complex', 'expand_func', 'expand_log', 'expand_mul', 'expand_multinomial', 'expand_power_base', 'expand_power_exp', 'expand_trig', 'expint', 'expr', 'expr_with_intlimits', 'expr_with_limits', 'expressions', 'exprtools', 'exptrigsimp', 'exquo', 'external', 'eye', 'factor', 'factor_', 'factor_list', 'factor_nc', 'factor_terms', 'factorial', 'factorial2', 'factorint', 'factorrat', 'facts', 'failing_assumptions', 'false', 'fancysets', 'farthest_points', 'fcode', 'ff', 'fft', 'fibonacci', 'field', 'field_isomorphism', 'filldedent', 'finite_diff_weights', 'flatten', 'floor', 'format_exc', 'fourier_series', 'fourier_transform', 'fps', 'frac', 'fraction', 'fresnelc', 'fresnels', 'fu', 'function', 'functions', 'fwht', 'gamma', 'gammasimp', 'gcd', 'gcd_list', 'gcd_terms', 'gcdex', 'gegenbauer', 'generate', 'genocchi', 'geometry', 'get_contraction_structure', 'get_indices', 'gff', 'gff_list', 'glsl_code', 'gosper', 'grevlex', 'grlex', 'groebner', 'ground_roots', 'group', 'gruntz', 'hadamard_product', 'half_gcdex', 'hankel1', 'hankel2', 'hankel_transform', 'harmonic', 'has_dups', 'has_variety', 'hermite', 'hermite_poly', 'hessian', 'hf', 'hn1', 'hn2', 'homogeneous_order', 'horner', 'hyper', 'hyperexpand', 'hypersimilar', 'hypersimp', 'i', 'idiff', 'ifft', 'ifwht', 'igcd', 'igrevlex', 'igrlex', 'ilcm', 'ilex', 'im', 'imageset', 'immutable', 'index_methods', 'indexed', 'inequalities', 'inference', 'init_printing', 'init_session', 'integer_log', 'integer_nthroot', 'integrals', 'integrate', 'interactive', 'interactive_traversal', 'interpolate', 'interpolating_poly', 'interpolating_spline', 'intersecting_product', 'intersection', 'intervals', 'intt', 'inv_quick', 'inverse_cosine_transform', 'inverse_fourier_transform', 'inverse_hankel_transform', 'inverse_laplace_transform', 'inverse_mellin_transform', 'inverse_mobius_transform', 'inverse_sine_transform', 'invert', 'is_abundant', 'is_amicable', 'is_convex', 'is_decreasing', 'is_deficient', 'is_increasing', 'is_mersenne_prime', 'is_monotonic', 'is_nthpow_residue', 'is_perfect', 'is_primitive_root', 'is_quad_residue', 'is_strictly_decreasing', 'is_strictly_increasing', 'is_zero_dimensional', 'isi', 'isolate', 'isprime', 'iterables', 'itermonomials', 'jacobi', 'jacobi_normalized', 'jacobi_poly', 'jacobi_symbol', 'jn', 'jn_zeros', 'jordan_cell', 'jscode', 'julia_code', 'kronecker_product', 'laguerre', 'laguerre_poly', 'lambdify', 'laplace_transform', 'latex', 'lcm', 'lcm_list', 'legendre', 'legendre_poly', 'legendre_symbol', 'lerchphi', 'lex', 'li', 'limit', 'limit_seq', 'line', 'line_integrate', 'linear_eq_to_matrix', 'linsolve', 'list2numpy', 'ln', 'log', 'logcombine', 'loggamma', 'logic', 'lowergamma', 'lucas', 'magic', 'manualintegrate', 'mathematica_code', 'mathieuc', 'mathieucprime', 'mathieus', 'mathieusprime', 'mathml', 'matrices', 'matrix2numpy', 'matrix_multiply_elementwise', 'matrix_symbols', 'meijerg', 'meijerint', 'mellin_transform', 'memoization', 'memoize_property', 'mersenne_prime_exponent', 'minimal_polynomial', 'minpoly', 'misc', 'mma', 'mmin', 'mobius', 'mobius_transform', 'mod', 'mod_inverse', 'monic', 'mul', 'multidimensional', 'multinomial', 'multinomial_coefficients', 'multipledispatch', 'multiplicity', 'myos', 'n_order', 'nan', 'nextprime', 'nfloat', 'nonlinsolve', 'not_empty_in', 'np', 'npartitions', 'nroots', 'nsimplify', 'nsolve', 'nth_power_roots_poly', 'ntheory', 'nthroot_mod', 'ntt', 'numbered_symbols', 'numbers', 'numer', 'octave_code', 'ode', 'ode_order', 'ones', 'oo', 'operations', 'ord0', 'ordered', 'ordinals', 'os', 'pager_print', 'parabola', 'parallel_poly_from_expr', 'parsing', 'partition', 'partitions_', 'pde', 'pde_separate', 'pde_separate_add', 'pde_separate_mul', 'pdiv', 'pdsolve', 'perfect_power', 'periodic_argument', 'periodicity', 'permutedims', 'pexquo', 'pi', 'piecewise_fold', 'plane', 'plot', 'plot_backends', 'plot_implicit', 'plotting', 'point', 'polar_lift', 'polarify', 'pollard_pm1', 'pollard_rho', 'poly', 'poly_from_expr', 'polygamma', 'polygon', 'polylog', 'polys', 'polysys', 'posify', 'postfixes', 'postorder_traversal', 'powdenest', 'power', 'powsimp', 'pprint', 'pprint_try_use_unicode', 'pprint_use_unicode', 'pquo', 'prefixes', 'prem', 'preorder_traversal', 'pretty', 'pretty_print', 'preview', 'prevprime', 'prime', 'primefactors', 'primenu', 'primeomega', 'primepi', 'primerange', 'primetest', 'primitive', 'primitive_element', 'primitive_root', 'primorial', 'principal_branch', 'print_ccode', 'print_fcode', 'print_glsl', 'print_gtk', 'print_jscode', 'print_latex', 'print_mathml', 'print_python', 'print_rcode', 'print_tree', 'printing', 'prod', 'product', 'products', 'public', 'pycode', 'python', 'quadratic_residues', 'quo', 'r', 'rad', 'radsimp', 'randMatrix', 'random_poly', 'randprime', 'randtest', 'rational_interpolate', 'ratsimp', 'ratsimpmodprime', 'rcode', 'rcollect', 're', 'real_root', 'real_roots', 'recurr', 'reduce_abs_inequalities', 'reduce_abs_inequality', 'reduce_inequalities', 'reduced', 'reduced_totient', 'refine', 'refine_root', 'register_handler', 'relational', 'release', 'rem', 'remove_handler', 'reshape', 'residue', 'residue_ntheory', 'result', 'resultant', 'rf', 'ring', 'root', 'rootof', 'roots', 'rot_axis1', 'rot_axis2', 'rot_axis3', 'rotations', 'row', 'row0', 'row1', 'row2', 'rq', 'rsolve', 'rsolve_hyper', 'rsolve_poly', 'rsolve_ratio', 'rules', 'runtests', 'rust_code', 'satisfiable', 'sec', 'sech', 'separatevars', 'sequence', 'series', 'seterr', 'sets', 'sfield', 'sieve', 'sift', 'sign', 'signsimp', 'simplify', 'simplify_logic', 'sin', 'sinc', 'sine_transform', 'singleton', 'singularities', 'singularityfunctions', 'singularityintegrate', 'sinh', 'solve', 'solve_linear', 'solve_linear_system', 'solve_linear_system_LU', 'solve_poly_inequality', 'solve_poly_system', 'solve_rational_inequalities', 'solve_triangulated', 'solve_undetermined_coeffs', 'solve_univariate_inequality', 'solvers', 'solveset', 'source', 'sparse', 'special', 'sqf', 'sqf_list', 'sqf_norm', 'sqf_part', 'sqrt', 'sqrt_mod', 'sqrt_mod_iter', 'sqrtdenest', 'srepr', 'sring', 'sstr', 'sstrrepr', 'stieltjes', 'strategies', 'sturm', 'subfactorial', 'subresultants', 'subsets', 'substitution', 'summation', 'summations', 'swinnerton_dyer_poly', 'symarray', 'symbol', 'symbols', 'symmetric_poly', 'symmetrize', 'sympify', 'sys', 'take', 'tan', 'tanh', 'tensor', 'tensorcontraction', 'tensorproduct', 'terms_gcd', 'test', 'textplot', 'threaded', 'time', 'timed', 'timeutils', 'to_cnf', 'to_dnf', 'to_nnf', 'to_number_field', 'together', 'topological_sort', 'total_degree', 'totient', 'trace', 'trailing', 'transforms', 'transpose', 'traversaltools', 'tribonacci', 'trigamma', 'trigonometry', 'trigsimp', 'true', 'trunc', 'unbranched_argument', 'unflatten', 'unpolarify', 'uppergamma', 'use', 'util', 'utilities', 'var', 'variations', 'vectorize', 'vfield', 'viete', 'vring', 'wronskian', 'x', 'xfield', 'xring', 'xthreaded', 'yn', 'zeros', 'zeta', 'zoo']
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-3::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5

5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-3::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-3::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4

5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:1:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4

>>> 
>>> exec('''

r, c, ci, cj = 10, 10, 5, 5
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> 10 10 5 5
SyntaxError: invalid syntax
>>> 
>>> input()
10 10 5 5
'10 10 5 5'
>>> 
>>> r, c, ci, cj = 
KeyboardInterrupt
>>> 
>>> text
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    text
NameError: name 'text' is not defined

>>> text = input()
10 10 5 5
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> text = input()
10 10 5 5
>>> 
>>> text
'10 10 5 5'
>>> text.split()
['10', '10', '5', '5']
>>> 
>>> list(map(int, text.split()))
[10, 10, 5, 5]
>>> 
>>> r, c, ci, cj = list(map(int, input().split()))
10 10 5 5
>>> r
10
c
>>> 
>>> c
10
>>> ci
5
>>> cj
5
>>> 
>>> r, c, ci, cj = list(map(int, input().split()))
745 42 11 41
>>> 
>>> exec('''

r, c, ci, cj = list(map(int, input().split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
745 42 11 41
11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11
11 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
11 10 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
11 10 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
11 10 9 8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
11 10 9 8 7 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
11 10 9 8 7 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
11 10 9 8 7 6 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
11 10 9 8 7 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
11 10 9 8 7 6 5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
11 10 9 8 7 6 5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
11 10 9 8 7 6 5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
11 10 9 8 7 6 5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -6 -6 -6 -6 -6 -6 -6 -6
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -7 -7 -7 -7 -7 -7
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -8 -8 -8 -8
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -9 -9
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
Traceback (most recent call last):
  File "<pyshell#254>", line 15, in <module>
    ''')
  File "<string>", line 10, in <module>
KeyboardInterrupt
>>> exec('''

r, c, cj, ci = list(map(int, input().split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
745 42 11 41
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> exec('''

r, c, cj, ci = list(map(int, input().split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
745 42 11 41
41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41
41 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40
41 40 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39
41 40 39 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38
41 40 39 38 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37
41 40 39 38 37 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36
41 40 39 38 37 36 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35
41 40 39 38 37 36 35 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34
41 40 39 38 37 36 35 34 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33
41 40 39 38 37 36 35 34 33 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32
41 40 39 38 37 36 35 34 33 32 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31
41 40 39 38 37 36 35 34 33 32 31 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
41 40 39 38 37 36 35 34 33 32 31 30 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29
41 40 39 38 37 36 35 34 33 32 31 30 29 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 27 27 27 27 27 27 27 27 27 27 27 27 27 27
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 26 26 26 26 26 26 26 26 26 26 26 26
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 25 25 25 25 25 25 25 25 25 25
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 24 24 24 24 24 24 24 24
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 23 23 23 23 23 23
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 22 22 22 22
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 21 21
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
Traceback (most recent call last):
  File "<pyshell#257>", line 15, in <module>
    ''')
  File "<string>", line 10, in <module>
KeyboardInterrupt
>>> exec('''

text = '745 42 11 41'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41
41 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40
41 40 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39
41 40 39 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38 38
41 40 39 38 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37
41 40 39 38 37 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36
41 40 39 38 37 36 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35
41 40 39 38 37 36 35 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34 34
41 40 39 38 37 36 35 34 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33 33
41 40 39 38 37 36 35 34 33 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32
41 40 39 38 37 36 35 34 33 32 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31
41 40 39 38 37 36 35 34 33 32 31 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30

41 40 39 38 37 36 35 34 33 32 31 30 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29 29
41 40 39 38 37 36 35 34 33 32 31 30 29 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 27 27 27 27 27 27 27 27 27 27 27 27 27 27
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 26 26 26 26 26 26 26 26 26 26 26 26
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 25 25 25 25 25 25 25 25 25 25
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 24 24 24 24 24 24 24 24
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 23 23 23 23 23 23
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 22 22 22 22
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 21 21
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20Traceback (most recent call last):
  File "<pyshell#258>", line 16, in <module>
    ''')
  File "<string>", line 11, in <module>
KeyboardInterrupt
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 11 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 3 3 3 4 4 5
5 4 3 2 2 2 2 2 2 3 3 4 4 5
5 4 3 2 1 1 1 1 2 2 3 3 4 4 5
5 4 3 2 1 0 0 1 1 2 2 3 3 4 4 5
5 4 3 2 1 1 1 1 2 2 3 3 4 4 5
5 4 3 2 2 2 2 2 2 3 3 4 4 5
5 4 3 3 3 3 3 3 3 3 4 4 5
5 4 4 4 4 4 4 4 4 4 4 5
>>> 
>>> exec('''

text = '10 11 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-2-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 3 3 4 5
5 4 3 2 2 2 2 2 3 4 5
5 4 3 2 1 1 1 2 3 4 5
5 4 3 2 1 0 1 2 3 4 5
5 4 3 2 1 1 1 2 3 4 5
5 4 3 2 2 2 2 2 3 4 5
5 4 3 3 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 4 4 5
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-2-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3
5 4 3 2 2 2 2
5 4 3 2 1 1
5 4 3 2 1
5 4 3 2 1 1
5 4 3 2 2 2 2
5 4 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4

>>> exec('''

text = '10 11 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 3 3 4 5
5 4 3 2 2 2 2 2 3 4 5
5 4 3 2 1 1 1 2 3 4 5

5 4 3 2 1 0 1 2 3 4 5
5 4 3 2 1 1 1 2 3 4 5
5 4 3 2 2 2 2 2 3 4 5
5 4 3 3 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 4 4 5
>>> 
>>> exec('''

text = '10 12 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5 5
5 4 3 3 3 3 3 3 3 4 5 5
5 4 3 2 2 2 2 2 3 4 5 5
5 4 3 2 1 1 1 2 3 4 5 5
5 4 3 2 1 0 1 2 3 4 5 5

5 4 3 2 1 1 1 2 3 4 5 5
5 4 3 2 2 2 2 2 3 4 5 5
5 4 3 3 3 3 3 3 3 4 5 5
5 4 4 4 4 4 4 4 4 4 5 5
>>> 
>>> exec('''

text = '10 13 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5 5 5
5 4 3 3 3 3 3 3 3 4 5 5 5
5 4 3 2 2 2 2 2 3 4 5 5 5
5 4 3 2 1 1 1 2 3 4 5 5 5
5 4 3 2 1 0 1 2 3 4 5 5 5
5 4 3 2 1 1 1 2 3 4 5 5 5
5 4 3 2 2 2 2 2 3 4 5 5 5
5 4 3 3 3 3 3 3 3 4 5 5 5
5 4 4 4 4 4 4 4 4 4 5 5 5

>>> 
'
>>> 
>>> exec('''

text = '10 20 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*c
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5
5 4 3 3 3 3 3 3 3 4 5 5 5 5 5 5 5 5 5 5
5 4 3 2 2 2 2 2 3 4 5 5 5 5 5 5 5 5 5 5
5 4 3 2 1 1 1 2 3 4 5 5 5 5 5 5 5 5 5 5
5 4 3 2 1 0 1 2 3 4 5 5 5 5 5 5 5 5 5 5
5 4 3 2 1 1 1 2 3 4 5 5 5 5 5 5 5 5 5 5

5 4 3 2 2 2 2 2 3 4 5 5 5 5 5 5 5 5 5 5
5 4 3 3 3 3 3 3 3 4 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5
>>> 
>>> row
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> row
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

>>> exec('''

text = '10 20 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4

5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 20 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, ci+c//2))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14
>>> 
>>> exec('''

text = '10 200 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, ci+c//2))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104

5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104
>>> 
>>> list(range(ci, ci+c//2))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]
>>> 
>>> ci+c//2
105
>>> ci
5
>>> list(range(ci, c-ci))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194]
>>> exec('''

text = '10 200 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194

5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194
>>> exec('''

text = '10 20 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14

5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2
5 4 3 2 1 1 1
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 1 1
5 4 3 2 2 2 2 2
5 4 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-2*i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4 4
5 4 3 2 2 2 2 2 3 3 3 4 4
5 4 3 2 1 1 1 2 2 2 2 3 3 3 4 4
5 4 3 2 1 0 1 1 2 2 2 2 3 3 3 4 4
5 4 3 2 1 1 1 2 2 2 2 3 3 3 4 4
5 4 3 2 2 2 2 2 3 3 3 4 4
5 4 3 3 3 3 3 3 3 4 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-2*i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2
5 4 3 2 1 1 1
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 1 1
5 4 3 2 2 2 2 2
5 4 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 0 -1 -1 -1 -1
5 4 3 2 1 0 -1 -2 -2 -2
5 4 3 2 1 0 -1 -2 -3 -3
5 4 3 2 1 0 -1 -2 -3 -4
5 4 3 2 1 0 -1 -2 -3 -4
5 4 3 2 1 0 -1 -2 -3 -4
5 4 3 2 1 0 -1 -2 -3 -3
5 4 3 2 1 0 -1 -2 -2 -2
5 4 3 2 1 0 -1 -1 -1 -1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(9-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(18-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3
5 4 3 2 1 0 -1 -2 -3 -4 -4
5 4 3 2 1 0 -1 -2 -3 -4
5 4 3 2 1 0 -1 -2 -3 -4 -4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -5 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(r//2):
	row[i+1:r-i] = [ci-1-i]*(c-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2
5 4 3 2 1 1 1
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 0
5 4 3 2 1 1 1
5 4 3 2 2 2 2 2
5 4 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj//2):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj*2):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -5 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4

5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(ci-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4
5 4 3 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3 3
5 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(cj-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4
5 4 3 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3 3
5 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [cj-1-i]*(ci-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4
5 4 3 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3
5 4 3 3
5 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj*2):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -5 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -4 -4 -4 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -3 -3 -3 -3 -3 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -2 -2 -2 -2 -2 -2 -2 -1 0 1 2 3 4
5 4 3 2 1 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> row
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
>>> len(row)
20
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:r]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:c]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4
5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4
5 4 3 2 1 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2:0:-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

for content in result[-2::-1]: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = [row[:]]
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))

result += result[-2::-1]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1] + [row[:]]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 2 1 0 1 2 3 4
>>> 
>>> result
[[5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]]
>>> 
>>> np.array(result)
array([[5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]])
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> result
[[5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], [5, 4, 3, 2, 1, 1, 1, 2, 3, 4], [5, 4, 3, 2, 2, 2, 2, 2, 3, 4], [5, 4, 3, 3, 3, 3, 3, 3, 3, 4], [5, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
>>> 
>>> np.array(result)
array([[5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]])
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1] + [row0]
# for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4

>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(str(row)[1:-1].replace(', ',' '))
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print([i]*c)
	
''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
[11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
[12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
[13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
[14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' ')))

''')
Traceback (most recent call last):
  File "<pyshell#376>", line 22, in <module>
    ''')
  File "<string>", line 20
    print(str([i]*c)[1:-1].replace(', ',' ')))
                                             ^
SyntaxError: invalid syntax
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:r-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	print(row)

''')
5 5 5 5 5 5 5 5 5 5
[5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[5, 4, 3, 3, 3, 3, 3, 3, 3, 3]
[5, 4, 3, 2, 2, 2, 2, 2, 2, 2]
[5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
[5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	r-i

''')
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	print(r-i)

''')
5 5 5 5 5 5 5 5 5 5
20
19
18
17
16
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(r-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 3
5 4 3 2 2 2 2 2 2 2
5 4 3 2 1 1 1 1 1 1
5 4 3 2 1 0 0 0 0 0
5 4 3 2 1 1 1 1 1 1
5 4 3 2 2 2 2 2 2 2
5 4 3 3 3 3 3 3 3 3
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	print(c-i)

''')
5 5 5 5 5 5 5 5 5 5
10
9
8
7
6

>>> 
>>> [ci-1-i]*(r-1-2*i)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	print([ci-1-i]*(r-1-2*i))

''')
5 5 5 5 5 5 5 5 5 5
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14
>>> 
>>> '''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14''' == '''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14'''
False
>>> 
>>> isi
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=int64)
>>> 
>>> isi1
Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    isi1
NameError: name 'isi1' is not defined
>>> 
>>> for isi1 in zip('''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14'''.split('\n'),'''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14'''.split('\n'))
SyntaxError: invalid syntax
>>> 
>>> for isi1 in zip('''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14'''.split('\n'),'''5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14'''.split('\n')):
	if isi1[0] != isi1[1]: print(isi1)

	
('5 5 5 5 5 5 5 5 5 5', '6 6 6 6 6 6 6 6 6 6')
('6 6 6 6 6 6 6 6 6 6', '7 7 7 7 7 7 7 7 7 7')
('7 7 7 7 7 7 7 7 7 7', '8 8 8 8 8 8 8 8 8 8')
('8 8 8 8 8 8 8 8 8 8', '9 9 9 9 9 9 9 9 9 9')
('9 9 9 9 9 9 9 9 9 9', '10 10 10 10 10 10 10 10 10 10')
('10 10 10 10 10 10 10 10 10 10', '11 11 11 11 11 11 11 11 11 11')
('11 11 11 11 11 11 11 11 11 11', '12 12 12 12 12 12 12 12 12 12')
('12 12 12 12 12 12 12 12 12 12', '13 13 13 13 13 13 13 13 13 13')
('13 13 13 13 13 13 13 13 13 13', '14 14 14 14 14 14 14 14 14 14')
>>> 
>>> exec('''

text = '20 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj+1,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
11 11 11 11 11 11 11 11 11 11
12 12 12 12 12 12 12 12 12 12
13 13 13 13 13 13 13 13 13 13
14 14 14 14 14 14 14 14 14 14
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj+1,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 6'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
6 6 6 6 6 6 6 6 6 6
6 5 5 5 5 5 5 5 5 5
6 5 4 4 4 4 4 4 4 5
6 5 4 3 3 3 3 3 4 5
6 5 4 3 2 2 2 3 4 5
6 5 4 3 2 1 2 3 4 5
6 5 4 3 2 2 2 3 4 5
6 5 4 3 3 3 3 3 4 5
6 5 4 4 4 4 4 4 4 5
6 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 6 5'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]*(cj*2)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 8'
r, c, cj, ci = list(map(int, text.split()))
row = [ci]+[ci]*(ci-cj)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
8 8 8 8
8 7 7 7 7 7 7 7 7 7
8 7 6 6 6 6 6 6 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 4 3 4 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 6 6 6 6 6 6 7
8 7 7 7 7 7 7 7 7 7
>>> 
>>> exec('''

text = '10 10 5 8'
r, c, cj, ci = list(map(int, text.split()))
row = list(range(cj+1, ci+1))[::-1]+[ci]*(ci-cj)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
8 7 6 8 8 8
8 7 7 7 7 7 7 7 7 7
8 7 6 6 6 6 6 6 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 4 3 4 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 6 6 6 6 6 6 7
8 7 7 7 7 7 7 7 7 7
>>> 
>>> exec('''

text = '10 10 5 8'
r, c, cj, ci = list(map(int, text.split()))
row = list(range(cj+1, ci+1))[::-1]+[cj]*(ci-cj)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
8 7 6 5 5 5
8 7 7 7 7 7 7 7 7 7
8 7 6 6 6 6 6 6 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 4 3 4 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 6 6 6 6 6 6 7
8 7 7 7 7 7 7 7 7 7
>>> 
>>> exec('''

text = '10 10 5 8'
r, c, cj, ci = list(map(int, text.split()))
row = list(range(cj+1, ci+1))[::-1]+[cj]*(c-ci+cj)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	row[i+1:c-i] = [ci-1-i]*(c-1-2*i)
	row = row[:c]
	result += [row[:]]

result += result[-2::-1] + [row0]
for content in result[:-1]: print(str(content)[1:-1].replace(', ',' '))

if r > 2*cj:
	for i in range(cj,r-cj):
		print(str([i]*c)[1:-1].replace(', ',' '))

''')
8 7 6 5 5 5 5 5 5 5
8 7 7 7 7 7 7 7 7 7
8 7 6 6 6 6 6 6 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 4 3 4 5 6 7
8 7 6 5 4 4 4 5 6 7
8 7 6 5 5 5 5 5 6 7
8 7 6 6 6 6 6 6 6 7
8 7 7 7 7 7 7 7 7 7
>>> 
>>> exec('''

text = '10 10 5 8'
r, c, cj, ci = list(map(int, text.split()))
row = list(range(cj+1, ci+1))[::-1]+[cj]*(c-ci+cj)+list(range(ci, c-ci))
row0 = row[:]
print(str(row)[1:-1].replace(', ',' '))

result = []
for i in range(cj):
	print([ci-1-i]*(c-1-2*i))

''')
8 7 6 5 5 5 5 5 5 5
[7, 7, 7, 7, 7, 7, 7, 7, 7]
[6, 6, 6, 6, 6, 6, 6]
[5, 5, 5, 5, 5]
[4, 4, 4]
[3]

>>> 
>>> list(range(5,9))
[5, 6, 7, 8]
>>> list(range(5,8+1))
[5, 6, 7, 8]
>>> 
>>> list(range(5,8+1))[::-1]
[8, 7, 6, 5]
>>> r, c, ci, cj = 10 10 5 8
SyntaxError: invalid syntax
>>> 
>>> r, c, ci, cj = list(map(int, '10 10 5 8'.split()))
>>> 
>>> r, c, ci, cj
(10, 10, 5, 8)
>>> 
>>> list(range(5,8+1))
[5, 6, 7, 8]
>>> list(range(5,8+1))[::-1]
[8, 7, 6, 5]
>>> 
>>> list(range(5,8+1))[::-1]+[5]*7+list(range(5,8+1))
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> '8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8'.split()
['8', '7', '6', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '7', '8']
>>> 
>>> len('8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8'.split())
17
>>> 
>>> len('5 5 5 5 5 5 5 5 5'.split())
9
>>> 
>>> list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1))
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:c]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5]
>>> len([8, 7, 6, 5, 5, 5, 5, 5, 5, 5])
10
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:c]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:18]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:16]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5,8+2))[::-1]+[5]*9+list(range(5,8+2)))[:17]
[9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7]
>>> 
>>> (list(range(5,8+2))[::-1]+[5]*7+list(range(5,8+2)))[:17]
[9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9]
>>> 
>>> (list(range(5,8+2))[::-1]+[5]*8+list(range(5,8+2)))[:17]
[9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5,8+2))[::-1]+[5]*7+list(range(5,8+2)))[:17]
[9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9]
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> (list(range(5-1,8+1))[::-1]+[5]*9+list(range(5-1,8+1)))[:17]
[8, 7, 6, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 6]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5-1,8+1))[::-1]+[5]*9+list(range(5-1,8+1)))[:17]
[8, 7, 6, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 6]

>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5-1,8+1))[::-1]+[4]*9-(2*1)+list(range(5-1,8+1)))[:17]
Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    (list(range(5-1,8+1))[::-1]+[4]*9-(2*1)+list(range(5-1,8+1)))[:17]
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))[:17]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5-1,8+1))[::-1]+[4]*(9-2*1)+list(range(5-1,8+1)))[:17]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5-1,8+1))[::-1]+[4]*(9-2*1)+list(range(5-1,8+1)))
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
>>> 
>>> (list(range(5,8+1))[::-1]+[5]*9+list(range(5,8+1)))
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> (list(range(5-1,8+1))[::-1]+[5-1]*(9-2*1)+list(range(5-1,8+1)))
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(10):
	(list(range(5-i,8+1))[::-1]+[5-i]*(9-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(10):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> '4, 4, 4, 4, 4, 4, 4, 4, 4'.count('4')
9
>>> '4 4 4 4 4 4 4 4 4'.count('4')
9
>>> '3 3 3 3 3 3 3'.count('3')
7
>>> '3, 3, 3, 3, 3, 3, 3'.count('4')
0
>>> '3, 3, 3, 3, 3, 3, 3'.count('3')
7
>>> for i in range(6):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> [5-i]*(10-1-2*i)
[]
>>> 
>>> list(range(5-i,8+1))
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> list(range(5-i,8+1))[::-1]
[8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> for i in range(5):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(-1, 5):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-1-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-1-2*i-1)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-3-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

>>> 
>>> for i in range(-1,5):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-2-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-1-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-3-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-1-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 3, 3, 3, 3, 3, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 2, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-1-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-1-i,8+1))[::-1]+[5-1-i]*(10-3-2*i)+list(range(5-1-i,8+1)))

	
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(-1, 5):
	(list(range(5-1-i,8+1))[:-1:-1]+[5-1-i]*(10-3-2*i)+list(range(5-1-i,8+1)))

	
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[1, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(6):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[:-1:-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[1, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[::-1]+[5-i]*(10-1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	list(range(5-i,8+1))[::-1]

	
[8, 7, 6, 5]
[8, 7, 6, 5, 4]
[8, 7, 6, 5, 4, 3]
[8, 7, 6, 5, 4, 3, 2]
[8, 7, 6, 5, 4, 3, 2, 1]
[8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> for i in range(6):
	list(range(5-i,8+1))

	
[5, 6, 7, 8]
[4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	list(range(5-i,8+1))[:-1:-1]

	
[]
[]
[]
[]
[]
[]
>>> 
>>> for i in range(6):
	list(range(5-i,8+1))[:1:-1]

	
[8, 7]
[8, 7, 6]
[8, 7, 6, 5]
[8, 7, 6, 5, 4]
[8, 7, 6, 5, 4, 3]
[8, 7, 6, 5, 4, 3, 2]
>>> for i in range(6):
	list(range(5-i,8+1))[:0:-1]

	
[8, 7, 6]
[8, 7, 6, 5]
[8, 7, 6, 5, 4]
[8, 7, 6, 5, 4, 3]
[8, 7, 6, 5, 4, 3, 2]
[8, 7, 6, 5, 4, 3, 2, 1]

>>> for i in range(6):
	list(range(5-i,8+1))

	
[5, 6, 7, 8]
[4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(6):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10+2-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(6):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10+1-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range(6):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(5+1):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(5+1):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> for i in range(-5-1):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))

	
>>> 
>>> for i in range(-5-1):
	(list(range(5+i,8+1))[:0:-1]+[5+i]*(10+2*i)+list(range(5+i,8+1)))

	
>>> [(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1))) for i in range(5+1)]
[[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8], [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
>>> 
>>> [(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1))) for i in range(5+1)][:0:-1]
[[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]]
>>> np.array([(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1))) for i in range(5+1)])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]])
>>> 
>>> 
>>> for i in range(5+1):
	(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))

[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> arr
Traceback (most recent call last):
  File "<pyshell#604>", line 1, in <module>
    arr
NameError: name 'arr' is not defined

>>> arr = [(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1))) for i in range(5+1)]
KeyboardInterrupt
>>> ere
array([[5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
       [5, 4, 3, 2, 1, 1, 1, 2, 3, 4],
       [5, 4, 3, 2, 2, 2, 2, 2, 3, 4],
       [5, 4, 3, 3, 3, 3, 3, 3, 3, 4],
       [5, 4, 4, 4, 4, 4, 4, 4, 4, 4]], dtype=int64)
>>> 
>>> ere = [(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1))) for i in range(5+1)]
>>> ere
[[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8], [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
>>> 
>>> 
>>> arr
Traceback (most recent call last):
  File "<pyshell#611>", line 1, in <module>
    arr
NameError: name 'arr' is not defined

>>> np.array(ere+ere[:0:-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]])
>>> 
>>> np.array(ere+ere[::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> 
>>> np.array(ere+ere[-1::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> np.array(ere+ere[1::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> np.array(ere+ere[5::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> np.array(ere+ere[5-1::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> 

>>> list(range(8, 20-8*2-1))
[]
>>> 
>>> 20-8*2-1
3
>>> 
>>> list(range(8, 820-8*2-1))
[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802]
>>> list(range(8, 8+20-8*2-1))
[8, 9, 10]
>>> 
>>> list(range(8, 8+20-8*2))
[8, 9, 10, 11]
>>> 
>>> list(range(8, 8+17-8*2))
[8]
>>> list(range(8+1, 8+20-8*2))
[9, 10, 11]
>>> 
>>> list(range(8+1, 8+17-8*2))
[]
>>> ere = [(list(range(5-i,8+1))[:0:-1]+[5-i]*(10-2*i)+list(range(5-i,8+1)))+list(range(8+1, 8+17-8*2)) for i in range(5+1)]
>>> ere
[[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8], [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
>>> 
>>> np.array(ere+ere[5-1::-1])
array([[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]])
>>> 
>>> e
Traceback (most recent call last):
  File "<pyshell#639>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> 
>>> for e in ere+ere[5-1::-1]:
	e

	
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

for e in ere+ere[5-1::-1]:
	print(e)

''')
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]

>>> 

>>> exec('''

text = '10 20 5 8'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(10-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+1)) for i in range(ci+1)]

for e in ere+ere[5-1::-1]:
	print(e)

''')
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
>>> 
>>> list(range(8+1, 8+17-8*2))
[]
>>> list(range(9+1, 9+17-9*2))
[]
>>> 
>>> list(range(8+1, 8+18-8*2))
[9]
>>> 
>>> list(range(8+1, 8+18-8*2))
[9]
>>> 
>>> exec('''

text = '10 20 5 8'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(10-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)) for i in range(ci+1)]

for e in ere+ere[5-1::-1]:
	print(e)

''')
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]
>>> 
>>> 

>>> exec('''

text = '10 20 5 8'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)) for i in range(ci+1)]

for e in ere+ere[ci-1::-1]:
	print(e)

''')
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
[8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]

>>> 
>>> exec('''

text = '10 20 5 80'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)) for i in range(ci+1)]

for e in ere+ere[ci-1::-1]:
	print(e)

''')
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
[80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
>>> 

>>> exec('''

text = '10 20 5 80'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)) for i in range(ci+1)]

for e in ere+ere[ci-1::-1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in ere+ere[ci-1::-1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in [ere+ere[ci-1::-1]][:-1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> 

>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in [ere+ere[ci-1::-1]][:1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
[5 5 5 5 5 5 5 5 5 5] [5 4 4 4 4 4 4 4 4 4] [5 4 3 3 3 3 3 3 3 4] [5 4 3 2 2 2 2 2 3 4] [5 4 3 2 1 1 1 2 3 4] [5 4 3 2 1 0 1 2 3 4] [5 4 3 2 1 1 1 2 3 4] [5 4 3 2 2 2 2 2 3 4] [5 4 3 3 3 3 3 3 3 4] [5 4 4 4 4 4 4 4 4 4] [5 5 5 5 5 5 5 5 5 5]
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e)[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 20 5 80'
r, c, ci, cj = list(map(int, text.split()))

ere = [(list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)) for i in range(ci+1)]

for e in ere+ere[ci-1::-1]:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61
>>> 
>>> exec('''

text = '10 10 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 4 4
5 4 3 3 3 3 3 3 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 1 0 1 2 3 4
5 4 3 2 1 1 1 2 3 4
5 4 3 2 2 2 2 2 3 4
5 4 3 3 3 3 3 3 3 4
5 4 4 4 4 4 4 4 4 4
>>> 
>>> exec('''

text = '10 10 5 20'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
20 19 18 17 16 15 14 13 12 11
>>> 
>>> exec('''

text = '10 20 5 5'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
5 5 5 5 5 5 5 5 5 5 5 6 7 8 9 10 11 12 13
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13
5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13
5 4 3 2 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13
5 4 3 2 2 2 2 2 3 4 5 6 7 8 9 10 11 12 13
5 4 3 3 3 3 3 3 3 4 5 6 7 8 9 10 11 12 13
5 4 4 4 4 4 4 4 4 4 5 6 7 8 9 10 11 12 13
>>> 
>>> exec('''

text = '745 42 11 41'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]

for e in (ere+ere[ci-1::-1])[:-1]:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 11 11 11 11 11 11 11 11 11 11 11
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 10 10 10 10 10 10 10 10 10 10
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 9 9 9 9 9 9 9 9 9
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 8 8 8 8 8 8 8 8
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 7 7 7 7 7 7 7
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 6 6 6 6 6 6
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 6 6 6 6 6 6
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 7 7 7 7 7 7 7
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 8 8 8 8 8 8 8 8
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 9 9 9 9 9 9 9 9 9
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 10 10 10 10 10 10 10 10 10 10
>>> 
>>> ere

>>> len(ere)
12
>>> exec('''

text = '745 42 11 41'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]
ere = (ere+ere[ci-1::-1])[:-1]


for e in ere:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
KeyboardInterrupt
>>> 
>>> exec('''

text = '745 42 11 41'
r, c, ci, cj = list(map(int, text.split()))

ere = [((list(range(ci-i,cj+1))[:0:-1]+[ci-i]*(r-2*i)+list(range(ci-i,cj+1)))+list(range(cj+1, cj+c-cj*2)))[:-1] for i in range(ci+1)]
ere = (ere+ere[ci-1::-1])[:-1]


for e in ere:
	print(str(e[:c])[1:-1].replace(', ',' '))

''')
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 11 11 11 11 11 11 11 11 11 11 11
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 10 10 10 10 10 10 10 10 10 10
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 9 9 9 9 9 9 9 9 9
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 8 8 8 8 8 8 8 8
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 7 7 7 7 7 7 7
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 6 6 6 6 6 6
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1

41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 1
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 2 2
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 3 3 3
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 4 4 4 4
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 5 5 5 5 5
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 6 6 6 6 6 6
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 7 7 7 7 7 7 7
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 8 8 8 8 8 8 8 8
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 9 9 9 9 9 9 9 9 9
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 10 10 10 10 10 10 10 10 10 10
>>> 
>>> ere[-1]
[41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
>>> 
>>> e[:c]
[41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> e[:c][-12:]
[11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> e[:c][-11:]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> 
>>> e[:c][-c:]
[41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> 
>>> c
42
>>> e[:c][-r:]
[41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> 
>>> e[:c][-ci:]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
>>> 
>>> lendata, digits = 100, 5;\
data = range(lendata)

>>> data
range(0, 100)
>>> 
>>> list(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> lendata, digits = 100, 5;\
data = np.arange(lendata)+1
>>> 
>>> list(data)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> 
>>> 

>>> lendata, digits = 9, 5;\
data = np.arange(lendata)+1
>>> 
>>> list(data)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> data
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> lendata, digits = 99, 5;\
data = np.arange(lendata)+1
>>> data
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
       52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
       69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
       86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>> 

>>> 

>>> exec(ef.read('Polynomul Build Executer.pyw'))
>>> exec(ef.read('Polynomul Build Executer.pyw'))
>>> exec(ef.read('Polynomul Build Executer1.pyw'))
>>> exec(ef.read('Polynomul Build Executer.pyw'))
>>> 
 RESTART: D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\Polynomul Exp - TK1 - Composer - Ver 1.pyw 
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\mymodule\editFiles.py", line 146, in add
    return str(open(address_link + filename, 'a').write(str(text_argument)+end))
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\Polynomul Exp - TK1 - Composer - Ver 1.pyw", line 64, in <module>
    if len(ef.read(logtitle)) < 1e5: ef.add(logtitle, i)
  File "C:\ProgramData\Anaconda3\lib\mymodule\editFiles.py", line 148, in add
    except KeyboardInterrupt: raise KeyboardInterrupt
KeyboardInterrupt
>>> 
 RESTART: D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\Polynomul Exp - TK1 - Composer - Ver 1.pyw 
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\mymodule\editFiles.py", line 146, in add
    return str(open(address_link + filename, 'a').write(str(text_argument)+end))
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\Polynomul Exp - TK1 - Composer - Ver 1.pyw", line 64, in <module>
    if len(ef.read(logtitle)) < 1e5: ef.add(logtitle, i)
  File "C:\ProgramData\Anaconda3\lib\mymodule\editFiles.py", line 148, in add
    except KeyboardInterrupt: raise KeyboardInterrupt
KeyboardInterrupt
>>> 
>>> mmin.group('0010100101',2)
['00', '10', '10', '01', '01']
>>> 

>>> mmin.group('0200200101',2)
['02', '00', '20', '01', '01']
>>> 
>>> mmin.group('1100611006',2)
['11', '00', '61', '10', '06']
>>> 

>>> 
>>> 
>>> [isi for isi in ef.read('PRTD1 - 6D - Version 2 - Longer.txt').split('\n') if '.' not in isi]
KeyboardInterrupt
>>> ppc
Traceback (most recent call last):
  File "<pyshell#734>", line 1, in <module>
    ppc
NameError: name 'ppc' is not defined

>>> import pyperclip as ppc;\
       ppc.copy('\n'.join([isi for isi in ef.read('PRTD1 - 6D - Version 2 - Longer.txt').split('\n') if '.' not in isi]))

>>> 

>>> ppc.copy('\n'.join([isi for isi in ef.read('PRTD1 - 6D - Version 2 - Longer.txt').split('\n') if '.' not in isi]).replace('[','').replace(']','').replace(', ','\t'))
>>> 672280+96040
768320
>>> 
