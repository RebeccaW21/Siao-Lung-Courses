Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\PolyResearchModules.pyw 
Traceback (most recent call last):
  File "D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\PolyResearchModules.pyw", line 21, in <module>
    from sympy import *
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\__init__.py", line 70, in <module>
    from .geometry import *
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\geometry\__init__.py", line 13, in <module>
    from sympy.geometry.point import Point, Point2D, Point3D
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\geometry\point.py", line 41, in <module>
    from .entity import GeometryEntity
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\geometry\entity.py", line 34, in <module>
    from sympy.multipledispatch import dispatch
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\multipledispatch\__init__.py", line 1, in <module>
    from .core import dispatch
  File "C:\ProgramData\Anaconda3\lib\site-packages\sympy\multipledispatch\core.py", line 3, in <module>
    from .dispatcher import Dispatcher, MethodDispatcher, ambiguity_warn
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 963, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 906, in _find_spec
  File "<frozen importlib._bootstrap_external>", line 1280, in find_spec
  File "<frozen importlib._bootstrap_external>", line 1252, in _get_spec
  File "<frozen importlib._bootstrap_external>", line 1394, in find_spec
  File "<frozen importlib._bootstrap_external>", line 95, in _path_isfile
  File "<frozen importlib._bootstrap_external>", line 87, in _path_is_mode_type
  File "<frozen importlib._bootstrap_external>", line 81, in _path_stat
KeyboardInterrupt
>>> 
>>> ef
<module 'mymodule.editFiles' from 'C:\\ProgramData\\Anaconda3\\lib\\mymodule\\editFiles.py'>
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0
		
		for i in range(finding_cp_1col(logtitle), lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]

			
>>> 
>>> Solution().uniquePaths
<bound method Solution.uniquePaths of <__main__.Solution object at 0x000001330BD8B9B0>>
>>> 
>>> Solution().uniquePaths(3,2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Solution().uniquePaths(3,2)
  File "<pyshell#5>", line 7, in uniquePaths
    for i in range(finding_cp_1col(logtitle), lendata**digits):
NameError: name 'finding_cp_1col' is not defined
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]

			
>>> 
>>> Solution().uniquePaths(3,2)
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]

		
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]
			
		return count

	
>>> 
>>> Solution().uniquePaths(3,2)
0
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]

		return count

	
>>> 
>>> Solution().uniquePaths(3,2)
3
>>> 
>>> Solution().uniquePaths(7, 3)
28
>>> 
>>> Solution().uniquePaths(23, 12)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Solution().uniquePaths(23, 12)
  File "<pyshell#25>", line 9, in uniquePaths
    count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]
KeyboardInterrupt
>>> 
>>> 2**(23+12-2)
8589934592
>>> 
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			count += [0, 1][nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1]
			print(nums)

		return count

	
>>> Solution().uniquePaths(23, 12)
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'down', 'down']Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Solution().uniquePaths(23, 12)
  File "<pyshell#37>", line 10, in uniquePaths
    print(nums)
KeyboardInterrupt
>>> 
>>> Solution().uniquePaths(7, 3)
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'right', 'down', 'down', 'down']
['right', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'down', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right']
['right', 'right', 'right', 'right', 'down', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'down', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'down', 'down', 'down', 'down']
['right', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down']
['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right']
['right', 'right', 'right', 'down', 'right', 'right', 'down', 'down']
['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right']
['right', 'right', 'right', 'down', 'right', 'down', 'right', 'down']
['right', 'right', 'right', 'down', 'right', 'down', 'down', 'right']
['right', 'right', 'right', 'down', 'right', 'down', 'down', 'down']
['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right']
['right', 'right', 'right', 'down', 'down', 'right', 'right', 'down']
['right', 'right', 'right', 'down', 'down', 'right', 'down', 'right']
['right', 'right', 'right', 'down', 'down', 'right', 'down', 'down']
['right', 'right', 'right', 'down', 'down', 'down', 'right', 'right']
['right', 'right', 'right', 'down', 'down', 'down', 'right', 'down']
['right', 'right', 'right', 'down', 'down', 'down', 'down', 'right']
['right', 'right', 'right', 'down', 'down', 'down', 'down', 'down']
['right', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down']
['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right']
['right', 'right', 'down', 'right', 'right', 'right', 'down', 'down']
['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right']
['right', 'right', 'down', 'right', 'right', 'down', 'right', 'down']
['right', 'right', 'down', 'right', 'right', 'down', 'down', 'right']
['right', 'right', 'down', 'right', 'right', 'down', 'down', 'down']
['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right']
['right', 'right', 'down', 'right', 'down', 'right', 'right', 'down']
['right', 'right', 'down', 'right', 'down', 'right', 'down', 'right']
['right', 'right', 'down', 'right', 'down', 'right', 'down', 'down']
['right', 'right', 'down', 'right', 'down', 'down', 'right', 'right']
['right', 'right', 'down', 'right', 'down', 'down', 'right', 'down']
['right', 'right', 'down', 'right', 'down', 'down', 'down', 'right']
['right', 'right', 'down', 'right', 'down', 'down', 'down', 'down']
['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right']
['right', 'right', 'down', 'down', 'right', 'right', 'right', 'down']
['right', 'right', 'down', 'down', 'right', 'right', 'down', 'right']
['right', 'right', 'down', 'down', 'right', 'right', 'down', 'down']
['right', 'right', 'down', 'down', 'right', 'down', 'right', 'right']
['right', 'right', 'down', 'down', 'right', 'down', 'right', 'down']
['right', 'right', 'down', 'down', 'right', 'down', 'down', 'right']
['right', 'right', 'down', 'down', 'right', 'down', 'down', 'down']
['right', 'right', 'down', 'down', 'down', 'right', 'right', 'right']
['right', 'right', 'down', 'down', 'down', 'right', 'right', 'down']
['right', 'right', 'down', 'down', 'down', 'right', 'down', 'right']
['right', 'right', 'down', 'down', 'down', 'right', 'down', 'down']
['right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
['right', 'right', 'down', 'down', 'down', 'down', 'right', 'down']
['right', 'right', 'down', 'down', 'down', 'down', 'down', 'right']
['right', 'right', 'down', 'down', 'down', 'down', 'down', 'down']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'down']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'down']
['right', 'down', 'right', 'right', 'right', 'down', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'down', 'down']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'down']
['right', 'down', 'right', 'right', 'down', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'down', 'down']
['right', 'down', 'right', 'right', 'down', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'down', 'right', 'down']
['right', 'down', 'right', 'right', 'down', 'down', 'down', 'right']
['right', 'down', 'right', 'right', 'down', 'down', 'down', 'down']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'down']
['right', 'down', 'right', 'down', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'down', 'down']
['right', 'down', 'right', 'down', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'down', 'right', 'down']
['right', 'down', 'right', 'down', 'right', 'down', 'down', 'right']
['right', 'down', 'right', 'down', 'right', 'down', 'down', 'down']
['right', 'down', 'right', 'down', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'down', 'right', 'right', 'down']
['right', 'down', 'right', 'down', 'down', 'right', 'down', 'right']
['right', 'down', 'right', 'down', 'down', 'right', 'down', 'down']
['right', 'down', 'right', 'down', 'down', 'down', 'right', 'right']
['right', 'down', 'right', 'down', 'down', 'down', 'right', 'down']
['right', 'down', 'right', 'down', 'down', 'down', 'down', 'right']
['right', 'down', 'right', 'down', 'down', 'down', 'down', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'down', 'down']
['right', 'down', 'down', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'down', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'down', 'down', 'right']
['right', 'down', 'down', 'right', 'right', 'down', 'down', 'down']
['right', 'down', 'down', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'down', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'down', 'right', 'down', 'right']
['right', 'down', 'down', 'right', 'down', 'right', 'down', 'down']
['right', 'down', 'down', 'right', 'down', 'down', 'right', 'right']
['right', 'down', 'down', 'right', 'down', 'down', 'right', 'down']
['right', 'down', 'down', 'right', 'down', 'down', 'down', 'right']
['right', 'down', 'down', 'right', 'down', 'down', 'down', 'down']
['right', 'down', 'down', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'down', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'down', 'right', 'right', 'down', 'right']
['right', 'down', 'down', 'down', 'right', 'right', 'down', 'down']
['right', 'down', 'down', 'down', 'right', 'down', 'right', 'right']
['right', 'down', 'down', 'down', 'right', 'down', 'right', 'down']
['right', 'down', 'down', 'down', 'right', 'down', 'down', 'right']
['right', 'down', 'down', 'down', 'right', 'down', 'down', 'down']
['right', 'down', 'down', 'down', 'down', 'right', 'right', 'right']
['right', 'down', 'down', 'down', 'down', 'right', 'right', 'down']
['right', 'down', 'down', 'down', 'down', 'right', 'down', 'right']
['right', 'down', 'down', 'down', 'down', 'right', 'down', 'down']
['right', 'down', 'down', 'down', 'down', 'down', 'right', 'right']
['right', 'down', 'down', 'down', 'down', 'down', 'right', 'down']
['right', 'down', 'down', 'down', 'down', 'down', 'down', 'right']
['right', 'down', 'down', 'down', 'down', 'down', 'down', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'down']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'down', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'down', 'down']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'down', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'down', 'down']
['down', 'right', 'right', 'right', 'down', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'down', 'right', 'down']
['down', 'right', 'right', 'right', 'down', 'down', 'down', 'right']
['down', 'right', 'right', 'right', 'down', 'down', 'down', 'down']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'down', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'down', 'down']
['down', 'right', 'right', 'down', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'down', 'right', 'down']
['down', 'right', 'right', 'down', 'right', 'down', 'down', 'right']
['down', 'right', 'right', 'down', 'right', 'down', 'down', 'down']
['down', 'right', 'right', 'down', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'down', 'right', 'right', 'down']
['down', 'right', 'right', 'down', 'down', 'right', 'down', 'right']
['down', 'right', 'right', 'down', 'down', 'right', 'down', 'down']
['down', 'right', 'right', 'down', 'down', 'down', 'right', 'right']
['down', 'right', 'right', 'down', 'down', 'down', 'right', 'down']
['down', 'right', 'right', 'down', 'down', 'down', 'down', 'right']
['down', 'right', 'right', 'down', 'down', 'down', 'down', 'down']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'down', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'down', 'down']
['down', 'right', 'down', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'down', 'right', 'down']
['down', 'right', 'down', 'right', 'right', 'down', 'down', 'right']
['down', 'right', 'down', 'right', 'right', 'down', 'down', 'down']
['down', 'right', 'down', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'down', 'right', 'right', 'down']
['down', 'right', 'down', 'right', 'down', 'right', 'down', 'right']
['down', 'right', 'down', 'right', 'down', 'right', 'down', 'down']
['down', 'right', 'down', 'right', 'down', 'down', 'right', 'right']
['down', 'right', 'down', 'right', 'down', 'down', 'right', 'down']
['down', 'right', 'down', 'right', 'down', 'down', 'down', 'right']
['down', 'right', 'down', 'right', 'down', 'down', 'down', 'down']
['down', 'right', 'down', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'down', 'right', 'right', 'right', 'down']
['down', 'right', 'down', 'down', 'right', 'right', 'down', 'right']
['down', 'right', 'down', 'down', 'right', 'right', 'down', 'down']
['down', 'right', 'down', 'down', 'right', 'down', 'right', 'right']
['down', 'right', 'down', 'down', 'right', 'down', 'right', 'down']
['down', 'right', 'down', 'down', 'right', 'down', 'down', 'right']
['down', 'right', 'down', 'down', 'right', 'down', 'down', 'down']
['down', 'right', 'down', 'down', 'down', 'right', 'right', 'right']
['down', 'right', 'down', 'down', 'down', 'right', 'right', 'down']
['down', 'right', 'down', 'down', 'down', 'right', 'down', 'right']
['down', 'right', 'down', 'down', 'down', 'right', 'down', 'down']
['down', 'right', 'down', 'down', 'down', 'down', 'right', 'right']
['down', 'right', 'down', 'down', 'down', 'down', 'right', 'down']
['down', 'right', 'down', 'down', 'down', 'down', 'down', 'right']
['down', 'right', 'down', 'down', 'down', 'down', 'down', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'down', 'down']
['down', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'down', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'down', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'down', 'down', 'down']
['down', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'down', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'down', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'down', 'right', 'down', 'down']
['down', 'down', 'right', 'right', 'down', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'down', 'down', 'right', 'down']
['down', 'down', 'right', 'right', 'down', 'down', 'down', 'right']
['down', 'down', 'right', 'right', 'down', 'down', 'down', 'down']
['down', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'down', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'down', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'down', 'right', 'right', 'down', 'down']
['down', 'down', 'right', 'down', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'down', 'right', 'down', 'right', 'down']
['down', 'down', 'right', 'down', 'right', 'down', 'down', 'right']
['down', 'down', 'right', 'down', 'right', 'down', 'down', 'down']
['down', 'down', 'right', 'down', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'down', 'down', 'right', 'right', 'down']
['down', 'down', 'right', 'down', 'down', 'right', 'down', 'right']
['down', 'down', 'right', 'down', 'down', 'right', 'down', 'down']
['down', 'down', 'right', 'down', 'down', 'down', 'right', 'right']
['down', 'down', 'right', 'down', 'down', 'down', 'right', 'down']
['down', 'down', 'right', 'down', 'down', 'down', 'down', 'right']
['down', 'down', 'right', 'down', 'down', 'down', 'down', 'down']
['down', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'down', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'down', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'down', 'right', 'right', 'right', 'down', 'down']
['down', 'down', 'down', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'down', 'right', 'right', 'down', 'right', 'down']
['down', 'down', 'down', 'right', 'right', 'down', 'down', 'right']
['down', 'down', 'down', 'right', 'right', 'down', 'down', 'down']
['down', 'down', 'down', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'down', 'right', 'down', 'right', 'right', 'down']
['down', 'down', 'down', 'right', 'down', 'right', 'down', 'right']
['down', 'down', 'down', 'right', 'down', 'right', 'down', 'down']
['down', 'down', 'down', 'right', 'down', 'down', 'right', 'right']
['down', 'down', 'down', 'right', 'down', 'down', 'right', 'down']
['down', 'down', 'down', 'right', 'down', 'down', 'down', 'right']
['down', 'down', 'down', 'right', 'down', 'down', 'down', 'down']
['down', 'down', 'down', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'down', 'down', 'right', 'right', 'right', 'down']
['down', 'down', 'down', 'down', 'right', 'right', 'down', 'right']
['down', 'down', 'down', 'down', 'right', 'right', 'down', 'down']
['down', 'down', 'down', 'down', 'right', 'down', 'right', 'right']
['down', 'down', 'down', 'down', 'right', 'down', 'right', 'down']
['down', 'down', 'down', 'down', 'right', 'down', 'down', 'right']
['down', 'down', 'down', 'down', 'right', 'down', 'down', 'down']
['down', 'down', 'down', 'down', 'down', 'right', 'right', 'right']
['down', 'down', 'down', 'down', 'down', 'right', 'right', 'down']
['down', 'down', 'down', 'down', 'down', 'right', 'down', 'right']
['down', 'down', 'down', 'down', 'down', 'right', 'down', 'down']
['down', 'down', 'down', 'down', 'down', 'down', 'right', 'right']
['down', 'down', 'down', 'down', 'down', 'down', 'right', 'down']
['down', 'down', 'down', 'down', 'down', 'down', 'down', 'right']
['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down']
28
>>> 
KeyboardInterrupt
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			print(['', str(nums)+'\n'][det], sep='', end='')

		return count

	
>>> Solution().uniquePaths(7, 3)
['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']
['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down']
['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right']
['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down']
['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right']
['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right']
['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down']
['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right']
['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right']
['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right']
['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down']
['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right']
['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right']
['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right']
['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
28
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			print(['', '\n'.join(nums)+'\n'][det], sep='', end='')

		return count

	
>>> 
>>> Solution().uniquePaths(7, 3)
right
right
right
right
right
right
down
down
right
right
right
right
right
down
right
down
right
right
right
right
right
down
down
right
right
right
right
right
down
right
right
down
right
right
right
right
down
right
down
right
right
right
right
right
down
down
right
right
right
right
right
down
right
right
right
down
right
right
right
down
right
right
down
right
right
right
right
down
right
down
right
right
right
right
right
down
down
right
right
right
right
right
down
right
right
right
right
down
right
right
down
right
right
right
down
right
right
right
down
right
right
down
right
right
right
right
down
right
down
right
right
right
right
right
down
down
right
right
right
right
right
down
right
right
right
right
right
down
right
down
right
right
right
right
down
right
right
down
right
right
right
down
right
right
right
down
right
right
down
right
right
right
right
down
right
down
right
right
right
right
right
down
down
right
right
right
right
right
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Solution().uniquePaths(7, 3)
  File "<pyshell#47>", line 11, in uniquePaths
    print(['', '\n'.join(nums)+'\n'][det], sep='', end='')
KeyboardInterrupt
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			print(['', '\t'.join(nums)+'\n'][det], sep='', end='')

		return count

	
>>> Solution().uniquePaths(7, 3)
right	right	right	right	right	right	down	down
right	right	right	right	right	down	right	down
right	right	right	right	right	down	down	right
right	right	right	right	down	right	right	down
right	right	right	right	down	right	down	right
right	right	right	right	down	down	right	right
right	right	right	down	right	right	right	down
right	right	right	down	right	right	down	right
right	right	right	down	right	down	right	right
right	right	right	down	down	right	right	right
right	right	down	right	right	right	right	down
right	right	down	right	right	right	down	right
right	right	down	right	right	down	right	right
right	right	down	right	down	right	right	right
right	right	down	down	right	right	right	right
right	down	right	right	right	right	right	down
right	down	right	right	right	right	down	right
right	down	right	right	right	down	right	right
right	down	right	right	down	right	right	right
right	down	right	down	right	right	right	right
right	down	down	right	right	right	right	right
down	right	right	right	right	right	right	down
down	right	right	right	right	right	down	right
down	right	right	right	right	down	right	right
down	right	right	right	down	right	right	right
down	right	right	down	right	right	right	right
down	right	down	right	right	right	right	right
down	down	right	right	right	right	right	right
28
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			print(['', '\t'.join(nums)+', \n'][det], sep='', end='')

		return count

	
>>> Solution().uniquePaths(7, 3)
right	right	right	right	right	right	down	down, 
right	right	right	right	right	down	right	down, 
right	right	right	right	right	down	down	right, 
right	right	right	right	down	right	right	down, 
right	right	right	right	down	right	down	right, 
right	right	right	right	down	down	right	right, 
right	right	right	down	right	right	right	down, 
right	right	right	down	right	right	down	right, 
right	right	right	down	right	down	right	right, 
right	right	right	down	down	right	right	right, 
right	right	down	right	right	right	right	down, 
right	right	down	right	right	right	down	right, 
right	right	down	right	right	down	right	right, 
right	right	down	right	down	right	right	right, 
right	right	down	down	right	right	right	right, 
right	down	right	right	right	right	right	down, 
right	down	right	right	right	right	down	right, 
right	down	right	right	right	down	right	right, 
right	down	right	right	down	right	right	right, 
right	down	right	down	right	right	right	right, 
right	down	down	right	right	right	right	right, 
down	right	right	right	right	right	right	down, 
down	right	right	right	right	right	down	right, 
down	right	right	right	right	down	right	right, 
down	right	right	right	down	right	right	right, 
down	right	right	down	right	right	right	right, 
down	right	down	right	right	right	right	right, 
down	down	right	right	right	right	right	right, 
28
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count = 0

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			print(['', '"'+'\t'.join(nums)+'", \n'][det], sep='', end='')

		return count

	
>>> 
>>> Solution().uniquePaths(7, 3)
"right	right	right	right	right	right	down	down", 
"right	right	right	right	right	down	right	down", 
"right	right	right	right	right	down	down	right", 
"right	right	right	right	down	right	right	down", 
"right	right	right	right	down	right	down	right", 
"right	right	right	right	down	down	right	right", 
"right	right	right	down	right	right	right	down", 
"right	right	right	down	right	right	down	right", 
"right	right	right	down	right	down	right	right", 
"right	right	right	down	down	right	right	right", 
"right	right	down	right	right	right	right	down", 
"right	right	down	right	right	right	down	right", 
"right	right	down	right	right	down	right	right", 
"right	right	down	right	down	right	right	right", 
"right	right	down	down	right	right	right	right", 
"right	down	right	right	right	right	right	down", 
"right	down	right	right	right	right	down	right", 
"right	down	right	right	right	down	right	right", 
"right	down	right	right	down	right	right	right", 
"right	down	right	down	right	right	right	right", 
"right	down	down	right	right	right	right	right", 
"down	right	right	right	right	right	right	down", 
"down	right	right	right	right	right	down	right", 
"down	right	right	right	right	down	right	right", 
"down	right	right	right	down	right	right	right", 
"down	right	right	down	right	right	right	right", 
"down	right	down	right	right	right	right	right", 
"down	down	right	right	right	right	right	right", 
28
>>> 
>>> sorted(["right	right	right	right	right	right	down	down",
"right	right	right	right	right	down	right	down",
"right	right	right	right	right	down	down	right",
"right	right	right	right	down	right	right	down",
"right	right	right	right	down	right	down	right",
"right	right	right	right	down	down	right	right",
"right	right	right	down	right	right	right	down",
"right	right	right	down	right	right	down	right",
"right	right	right	down	right	down	right	right",
"right	right	right	down	down	right	right	right",
"right	right	down	right	right	right	right	down",
"right	right	down	right	right	right	down	right",
"right	right	down	right	right	down	right	right",
"right	right	down	right	down	right	right	right",
"right	right	down	down	right	right	right	right",
"right	down	right	right	right	right	right	down",
"right	down	right	right	right	right	down	right",
"right	down	right	right	right	down	right	right",
"right	down	right	right	down	right	right	right",
"right	down	right	down	right	right	right	right",
"right	down	down	right	right	right	right	right",
"down	right	right	right	right	right	right	down",
"down	right	right	right	right	right	down	right",
"down	right	right	right	right	down	right	right",
"down	right	right	right	down	right	right	right",
"down	right	right	down	right	right	right	right",
"down	right	down	right	right	right	right	right",
"down	down	right	right	right	right	right	right"])
['down\tdown\tright\tright\tright\tright\tright\tright', 'down\tright\tdown\tright\tright\tright\tright\tright', 'down\tright\tright\tdown\tright\tright\tright\tright', 'down\tright\tright\tright\tdown\tright\tright\tright', 'down\tright\tright\tright\tright\tdown\tright\tright', 'down\tright\tright\tright\tright\tright\tdown\tright', 'down\tright\tright\tright\tright\tright\tright\tdown', 'right\tdown\tdown\tright\tright\tright\tright\tright', 'right\tdown\tright\tdown\tright\tright\tright\tright', 'right\tdown\tright\tright\tdown\tright\tright\tright', 'right\tdown\tright\tright\tright\tdown\tright\tright', 'right\tdown\tright\tright\tright\tright\tdown\tright', 'right\tdown\tright\tright\tright\tright\tright\tdown', 'right\tright\tdown\tdown\tright\tright\tright\tright', 'right\tright\tdown\tright\tdown\tright\tright\tright', 'right\tright\tdown\tright\tright\tdown\tright\tright', 'right\tright\tdown\tright\tright\tright\tdown\tright', 'right\tright\tdown\tright\tright\tright\tright\tdown', 'right\tright\tright\tdown\tdown\tright\tright\tright', 'right\tright\tright\tdown\tright\tdown\tright\tright', 'right\tright\tright\tdown\tright\tright\tdown\tright', 'right\tright\tright\tdown\tright\tright\tright\tdown', 'right\tright\tright\tright\tdown\tdown\tright\tright', 'right\tright\tright\tright\tdown\tright\tdown\tright', 'right\tright\tright\tright\tdown\tright\tright\tdown', 'right\tright\tright\tright\tright\tdown\tdown\tright', 'right\tright\tright\tright\tright\tdown\tright\tdown', 'right\tright\tright\tright\tright\tright\tdown\tdown']
>>> 
>>> '\n'.join(sorted(["right	right	right	right	right	right	down	down",
"right	right	right	right	right	down	right	down",
"right	right	right	right	right	down	down	right",
"right	right	right	right	down	right	right	down",
"right	right	right	right	down	right	down	right",
"right	right	right	right	down	down	right	right",
"right	right	right	down	right	right	right	down",
"right	right	right	down	right	right	down	right",
"right	right	right	down	right	down	right	right",
"right	right	right	down	down	right	right	right",
"right	right	down	right	right	right	right	down",
"right	right	down	right	right	right	down	right",
"right	right	down	right	right	down	right	right",
"right	right	down	right	down	right	right	right",
"right	right	down	down	right	right	right	right",
"right	down	right	right	right	right	right	down",
"right	down	right	right	right	right	down	right",
"right	down	right	right	right	down	right	right",
"right	down	right	right	down	right	right	right",
"right	down	right	down	right	right	right	right",
"right	down	down	right	right	right	right	right",
"down	right	right	right	right	right	right	down",
"down	right	right	right	right	right	down	right",
"down	right	right	right	right	down	right	right",
"down	right	right	right	down	right	right	right",
"down	right	right	down	right	right	right	right",
"down	right	down	right	right	right	right	right",
"down	down	right	right	right	right	right	right"]))
'down\tdown\tright\tright\tright\tright\tright\tright\ndown\tright\tdown\tright\tright\tright\tright\tright\ndown\tright\tright\tdown\tright\tright\tright\tright\ndown\tright\tright\tright\tdown\tright\tright\tright\ndown\tright\tright\tright\tright\tdown\tright\tright\ndown\tright\tright\tright\tright\tright\tdown\tright\ndown\tright\tright\tright\tright\tright\tright\tdown\nright\tdown\tdown\tright\tright\tright\tright\tright\nright\tdown\tright\tdown\tright\tright\tright\tright\nright\tdown\tright\tright\tdown\tright\tright\tright\nright\tdown\tright\tright\tright\tdown\tright\tright\nright\tdown\tright\tright\tright\tright\tdown\tright\nright\tdown\tright\tright\tright\tright\tright\tdown\nright\tright\tdown\tdown\tright\tright\tright\tright\nright\tright\tdown\tright\tdown\tright\tright\tright\nright\tright\tdown\tright\tright\tdown\tright\tright\nright\tright\tdown\tright\tright\tright\tdown\tright\nright\tright\tdown\tright\tright\tright\tright\tdown\nright\tright\tright\tdown\tdown\tright\tright\tright\nright\tright\tright\tdown\tright\tdown\tright\tright\nright\tright\tright\tdown\tright\tright\tdown\tright\nright\tright\tright\tdown\tright\tright\tright\tdown\nright\tright\tright\tright\tdown\tdown\tright\tright\nright\tright\tright\tright\tdown\tright\tdown\tright\nright\tright\tright\tright\tdown\tright\tright\tdown\nright\tright\tright\tright\tright\tdown\tdown\tright\nright\tright\tright\tright\tright\tdown\tright\tdown\nright\tright\tright\tright\tright\tright\tdown\tdown'

>>> print('\n'.join(sorted(["right	right	right	right	right	right	down	down",
"right	right	right	right	right	down	right	down",
"right	right	right	right	right	down	down	right",
"right	right	right	right	down	right	right	down",
"right	right	right	right	down	right	down	right",
"right	right	right	right	down	down	right	right",
"right	right	right	down	right	right	right	down",
"right	right	right	down	right	right	down	right",
"right	right	right	down	right	down	right	right",
"right	right	right	down	down	right	right	right",
"right	right	down	right	right	right	right	down",
"right	right	down	right	right	right	down	right",
"right	right	down	right	right	down	right	right",
"right	right	down	right	down	right	right	right",
"right	right	down	down	right	right	right	right",
"right	down	right	right	right	right	right	down",
"right	down	right	right	right	right	down	right",
"right	down	right	right	right	down	right	right",
"right	down	right	right	down	right	right	right",
"right	down	right	down	right	right	right	right",
"right	down	down	right	right	right	right	right",
"down	right	right	right	right	right	right	down",
"down	right	right	right	right	right	down	right",
"down	right	right	right	right	down	right	right",
"down	right	right	right	down	right	right	right",
"down	right	right	down	right	right	right	right",
"down	right	down	right	right	right	right	right",
"down	down	right	right	right	right	right	right"])))
down	down	right	right	right	right	right	right
down	right	down	right	right	right	right	right
down	right	right	down	right	right	right	right
down	right	right	right	down	right	right	right
down	right	right	right	right	down	right	right
down	right	right	right	right	right	down	right
down	right	right	right	right	right	right	down
right	down	down	right	right	right	right	right
right	down	right	down	right	right	right	right
right	down	right	right	down	right	right	right
right	down	right	right	right	down	right	right
right	down	right	right	right	right	down	right
right	down	right	right	right	right	right	down
right	right	down	down	right	right	right	right
right	right	down	right	down	right	right	right
right	right	down	right	right	down	right	right
right	right	down	right	right	right	down	right
right	right	down	right	right	right	right	down
right	right	right	down	down	right	right	right
right	right	right	down	right	down	right	right
right	right	right	down	right	right	down	right
right	right	right	down	right	right	right	down
right	right	right	right	down	down	right	right
right	right	right	right	down	right	down	right
right	right	right	right	down	right	right	down
right	right	right	right	right	down	down	right
right	right	right	right	right	down	right	down
right	right	right	right	right	right	down	down
>>> 
>>> down	down	right	right	right	right	right	right'.split()
SyntaxError: invalid syntax
>>> 
>>> 'down	down	right	right	right	right	right	right'.split()
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> list1 = 'down	down	right	right	right	right	right	right'.split()
>>> list2 = list1[:]
>>> 
>>> list1
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> list2
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> len(list1)
8
>>> 
>>> 7+3-2
8
>>> 
>>> i
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    i
NameError: name 'i' is not defined

>>> 
>>> lendata, digits = 10, 6;\
data = range(lendata)
>>> 
>>> lendata, digits = 7+3-2, 7+3-2;\
data = range(lendata)
>>> 
>>> for i in range(finding_cp_1col(logtitle), lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    for i in range(finding_cp_1col(logtitle), lendata**digits):
NameError: name 'finding_cp_1col' is not defined
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums

	
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 2]
[0, 0, 0, 0, 0, 0, 0, 3]
[0, 0, 0, 0, 0, 0, 0, 4]
[0, 0, 0, 0, 0, 0, 0, 5]
[0, 0, 0, 0, 0, 0, 0, 6]
[0, 0, 0, 0, 0, 0, 0, 7]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 1, 2]
[0, 0, 0, 0, 0, 0, 1, 3]
[0, 0, 0, 0, 0, 0, 1, 4]
[0, 0, 0, 0, 0, 0, 1, 5]
[0, 0, 0, 0, 0, 0, 1, 6]
[0, 0, 0, 0, 0, 0, 1, 7]
[0, 0, 0, 0, 0, 0, 2, 0]
[0, 0, 0, 0, 0, 0, 2, 1]
[0, 0, 0, 0, 0, 0, 2, 2]
[0, 0, 0, 0, 0, 0, 2, 3]
[0, 0, 0, 0, 0, 0, 2, 4]
[0, 0, 0, 0, 0, 0, 2, 5]
[0, 0, 0, 0, 0, 0, 2, 6]
[0, 0, 0, 0, 0, 0, 2, 7]
[0, 0, 0, 0, 0, 0, 3, 0]
[0, 0, 0, 0, 0, 0, 3, 1]
[0, 0, 0, 0, 0, 0, 3, 2]
[0, 0, 0, 0, 0, 0, 3, 3]
[0, 0, 0, 0, 0, 0, 3, 4]
[0, 0, 0, 0, 0, 0, 3, 5]
[0, 0, 0, 0, 0, 0, 3, 6]
[0, 0, 0, 0, 0, 0, 3, 7]
[0, 0, 0, 0, 0, 0, 4, 0]
[0, 0, 0, 0, 0, 0, 4, 1]
[0, 0, 0, 0, 0, 0, 4, 2]
[0, 0, 0, 0, 0, 0, 4, 3]
[0, 0, 0, 0, 0, 0, 4, 4]
[0, 0, 0, 0, 0, 0, 4, 5]
[0, 0, 0, 0, 0, 0, 4, 6]
[0, 0, 0, 0, 0, 0, 4, 7]
[0, 0, 0, 0, 0, 0, 5, 0]
[0, 0, 0, 0, 0, 0, 5, 1]
[0, 0, 0, 0, 0, 0, 5, 2]
[0, 0, 0, 0, 0, 0, 5, 3]
[0, 0, 0, 0, 0, 0, 5, 4]
[0, 0, 0, 0, 0, 0, 5, 5]
[0, 0, 0, 0, 0, 0, 5, 6]
[0, 0, 0, 0, 0, 0, 5, 7]
[0, 0, 0, 0, 0, 0, 6, 0]
[0, 0, 0, 0, 0, 0, 6, 1]
[0, 0, 0, 0, 0, 0, 6, 2]
[0, 0, 0, 0, 0, 0, 6, 3]
[0, 0, 0, 0, 0, 0, 6, 4]
[0, 0, 0, 0, 0, 0, 6, 5]
[0, 0, 0, 0, 0, 0, 6, 6]
[0, 0, 0, 0, 0, 0, 6, 7]
[0, 0, 0, 0, 0, 0, 7, 0]
[0, 0, 0, 0, 0, 0, 7, 1]
[0, 0, 0, 0, 0, 0, 7, 2]
[0, 0, 0, 0, 0, 0, 7, 3]
[0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 0, 0, 0, 0, 7, 5]
[0, 0, 0, 0, 0, 0, 7, 6]
[0, 0, 0, 0, 0, 0, 7, 7]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 2]
[0, 0, 0, 0, 0, 1, 0, 3]
[0, 0, 0, 0, 0, 1, 0, 4]
[0, 0, 0, 0, 0, 1, 0, 5]
[0, 0, 0, 0, 0, 1, 0, 6]
[0, 0, 0, 0, 0, 1, 0, 7]
[0, 0, 0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 1, 1, 2]
[0, 0, 0, 0, 0, 1, 1, 3]
[0, 0, 0, 0, 0, 1, 1, 4]
[0, 0, 0, 0, 0, 1, 1, 5]
[0, 0, 0, 0, 0, 1, 1, 6]
[0, 0, 0, 0, 0, 1, 1, 7]
[0, 0, 0, 0, 0, 1, 2, 0]
[0, 0, 0, 0, 0, 1, 2, 1]
[0, 0, 0, 0, 0, 1, 2, 2]
[0, 0, 0, 0, 0, 1, 2, 3]
[0, 0, 0, 0, 0, 1, 2, 4]
[0, 0, 0, 0, 0, 1, 2, 5]
[0, 0, 0, 0, 0, 1, 2, 6]
[0, 0, 0, 0, 0, 1, 2, 7]
[0, 0, 0, 0, 0, 1, 3, 0]
Traceback (most recent call last):
  File "<pyshell#93>", line 3, in <module>
    nums
KeyboardInterrupt
>>> 
>>> lendata, digits = 7+3-2, 2;\
data = range(lendata)
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	nums

	
[0, 0]
[0, 1]
[0, 2]
[0, 3]
[0, 4]
[0, 5]
[0, 6]
[0, 7]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[1, 4]
[1, 5]
[1, 6]
[1, 7]
[2, 0]
[2, 1]
[2, 2]
[2, 3]
[2, 4]
[2, 5]
[2, 6]
[2, 7]
[3, 0]
[3, 1]
[3, 2]
[3, 3]
[3, 4]
[3, 5]
[3, 6]
[3, 7]
[4, 0]
[4, 1]
[4, 2]
[4, 3]
[4, 4]
[4, 5]
[4, 6]
[4, 7]
[5, 0]
[5, 1]
[5, 2]
[5, 3]
[5, 4]
[5, 5]
[5, 6]
[5, 7]
[6, 0]
[6, 1]
[6, 2]
[6, 3]
[6, 4]
[6, 5]
[6, 6]
[6, 7]
[7, 0]
[7, 1]
[7, 2]
[7, 3]
[7, 4]
[7, 5]
[7, 6]
[7, 7]
>>> 
>>> list1 = 'down	down	right	right	right	right	right	right'.split()
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)

	
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> coun
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    coun
NameError: name 'coun' is not defined
>>> count
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    count
NameError: name 'count' is not defined
>>> count = 0
>>> coun
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    coun
NameError: name 'coun' is not defined
>>> count
0

>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)
	count += 1

	
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> count
64
>>> 
>>> 
>>> 
>>> result
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> 
>>> result = []
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)
	result += [list2]

	
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> len(list2)
8
>>> 
>>> result
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']]
>>> 
>>> list(set(result))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    list(set(result))
TypeError: unhashable type: 'list'

>>> list(set(result))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    list(set(result))
TypeError: unhashable type: 'list'

>>> result = []
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)
	result += [tuple(list2)]

	
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> list(set(result))
[('down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'), ('down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'), ('down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'), ('right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'), ('down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'), ('right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'), ('right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'), ('down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'), ('right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'), ('down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'), ('right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'), ('down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'), ('right', 'down', 'down', 'right', 'right', 'right', 'right', 'right')]
>>> 
>>> len(set(result))
13
>>> 
>>> len((result))
64
>>> 
>>> result = []
>>> result = []
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)
	result += [list2]

	
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> len(mmin.make_unique(result))
13
>>> 
>>> np.array(mmin.make_unique(result))
array([['down', 'down', 'right', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'right',
        'down'],
       ['down', 'right', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'right',
        'down']], dtype='<U5')
>>> 
>>> np.array(mmin.make_unique(result))
array([['down', 'down', 'right', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'right',
        'down'],
       ['down', 'right', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'right',
        'down']], dtype='<U5')
>>> 
>>> mmin.make_unique(result)
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]
>>> 
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count, result = 0, []

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			result += [[], nums][det]
##			print(['', '\n'.join(nums)+'\n'][det], sep='', end='')

		return count

	
>>> Solution().uniquePaths(7, 3)
28
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count, result = 0, []

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			result += [[], nums][det]
##			print(['', '\n'.join(nums)+'\n'][det], sep='', end='')

		return result

	
>>> Solution().uniquePaths(7, 3)
['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		data = ['right', 'down']
		lendata, digits = len(data), m+n-2
		count, result = 0, []

		for i in range(lendata**digits):
			nums = [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
			det = nums.count(data[0]) == m-1 and nums.count(data[1]) == n-1
			count += [0, 1][det]
			result += [[], [nums]][det]
##			print(['', '\n'.join(nums)+'\n'][det], sep='', end='')

		return result

	
>>> Solution().uniquePaths(7, 3)
[['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']]
>>> 
>>> mmin.make_unique(result)
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]
>>> sorted(Solution().uniquePaths(7, 3))
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']]
>>> 
>>> 
>>> sorted(mmin.make_unique(result))
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']]

>>> sorted(Solution().uniquePaths(7, 3))
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']]
>>> [['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]==[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]
True
>>> 
>>> sorted(mmin.make_unique(result))==[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']]
True
>>> sorted(mmin.make_unique(result))==sorted(Solution().uniquePaths(7, 3))[:14]
False
>>> sorted(mmin.make_unique(result))==sorted(Solution().uniquePaths(7, 3))[:13]
True
>>> 
>>> result1 = sorted(mmin.make_unique(result))
>>> result1
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down']]
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	list2 = list1[:]
	list2[nums[0]], list2[nums[1]] = list2[nums[1]], list2[nums[0]]
	print(list2)
	result += [list2]
KeyboardInterrupt
>>> 
>>> ['right']*(7+3-2)
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	
KeyboardInterrupt
>>> 
>>> List
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    List
NameError: name 'List' is not defined
>>> 
>>> List = ['right']*(7+3-2)
>>> 
>>> List = ['right']*(digits)
>>> List
['right', 'right']
>>> 
>>> List = ['right']*(lendata)
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	List[nums[0]], List[nums[1]] = ['right
					
SyntaxError: EOL while scanning string literal
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	List[nums[0]], List[nums[1]] = ['down']*2
KeyboardInterrupt
>>> 
>>> result
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right']]
>>> 
>>> result = []
>>> List
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*2
	result += [sample]

	
>>> result

>>> 
>>> set(result)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    set(result)
TypeError: unhashable type: 'list'
>>> 
>>> mmin.make_unique(result)
[['down', 'right', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]
>>> 
>>> len(mmin.make_unique(result))
36
>>> mmin.make_unique(result)[0]
['down', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
>>> 
>>> np.array(mmin.make_unique(result))
array([['down', 'right', 'right', 'right', 'right', 'right', 'right',
        'right'],
       ['down', 'down', 'right', 'right', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['down', 'right', 'right', 'right', 'right', 'right', 'right',
        'down'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['right', 'down', 'right', 'right', 'right', 'right', 'right',
        'down'],
       ['right', 'right', 'down', 'right', 'right', 'right', 'right',
        'right'],
       ['right', 'right', 'down', 'down', 'right', 'right', 'right',
        'right'],
       ['right', 'right', 'down', 'right', 'down', 'right', 'right',
        'right'],
       ['right', 'right', 'down', 'right', 'right', 'down', 'right',
        'right'],
       ['right', 'right', 'down', 'right', 'right', 'right', 'down',
        'right'],
       ['right', 'right', 'down', 'right', 'right', 'right', 'right',
        'down'],
       ['right', 'right', 'right', 'down', 'right', 'right', 'right',
        'right'],
       ['right', 'right', 'right', 'down', 'down', 'right', 'right',
        'right'],
       ['right', 'right', 'right', 'down', 'right', 'down', 'right',
        'right'],
       ['right', 'right', 'right', 'down', 'right', 'right', 'down',
        'right'],
       ['right', 'right', 'right', 'down', 'right', 'right', 'right',
        'down'],
       ['right', 'right', 'right', 'right', 'down', 'right', 'right',
        'right'],
       ['right', 'right', 'right', 'right', 'down', 'down', 'right',
        'right'],
       ['right', 'right', 'right', 'right', 'down', 'right', 'down',
        'right'],
       ['right', 'right', 'right', 'right', 'down', 'right', 'right',
        'down'],
       ['right', 'right', 'right', 'right', 'right', 'down', 'right',
        'right'],
       ['right', 'right', 'right', 'right', 'right', 'down', 'down',
        'right'],
       ['right', 'right', 'right', 'right', 'right', 'down', 'right',
        'down'],
       ['right', 'right', 'right', 'right', 'right', 'right', 'down',
        'right'],
       ['right', 'right', 'right', 'right', 'right', 'right', 'down',
        'down'],
       ['right', 'right', 'right', 'right', 'right', 'right', 'right',
        'down']], dtype='<U5')
>>> mmin.make_unique(result)
[['down', 'right', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'down']]
>>> 
>>> str(mmin.make_unique(result)).replace("', '", '')
"[['downrightrightrightrightrightrightright'], ['downdownrightrightrightrightrightright'], ['downrightdownrightrightrightrightright'], ['downrightrightdownrightrightrightright'], ['downrightrightrightdownrightrightright'], ['downrightrightrightrightdownrightright'], ['downrightrightrightrightrightdownright'], ['downrightrightrightrightrightrightdown'], ['rightdownrightrightrightrightrightright'], ['rightdowndownrightrightrightrightright'], ['rightdownrightdownrightrightrightright'], ['rightdownrightrightdownrightrightright'], ['rightdownrightrightrightdownrightright'], ['rightdownrightrightrightrightdownright'], ['rightdownrightrightrightrightrightdown'], ['rightrightdownrightrightrightrightright'], ['rightrightdowndownrightrightrightright'], ['rightrightdownrightdownrightrightright'], ['rightrightdownrightrightdownrightright'], ['rightrightdownrightrightrightdownright'], ['rightrightdownrightrightrightrightdown'], ['rightrightrightdownrightrightrightright'], ['rightrightrightdowndownrightrightright'], ['rightrightrightdownrightdownrightright'], ['rightrightrightdownrightrightdownright'], ['rightrightrightdownrightrightrightdown'], ['rightrightrightrightdownrightrightright'], ['rightrightrightrightdowndownrightright'], ['rightrightrightrightdownrightdownright'], ['rightrightrightrightdownrightrightdown'], ['rightrightrightrightrightdownrightright'], ['rightrightrightrightrightdowndownright'], ['rightrightrightrightrightdownrightdown'], ['rightrightrightrightrightrightdownright'], ['rightrightrightrightrightrightdowndown'], ['rightrightrightrightrightrightrightdown']]"
>>> 
>>> str(mmin.make_unique(result)).replace("', '", '')
KeyboardInterrupt
>>> 
>>> [r for r in mmin.make_unique(result) if r.count('down') == 3-1]
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']]
>>> 
>>> len([r for r in mmin.make_unique(result) if r.count('down') == 3-1])
28
>>> 
>>> List = ['right']*(lendata)
>>> for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*2
	result += [sample]

	
>>> [r for r in mmin.make_unique(result) if r.count('down') == 3-1]
[['down', 'down', 'right', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'down', 'right', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'down', 'right', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'down', 'right', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'down', 'right', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'down', 'right'], ['down', 'right', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'down', 'down', 'right', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'down', 'right', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'down', 'right', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'down', 'right', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'down', 'right'], ['right', 'down', 'right', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'down', 'down', 'right', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'down', 'right', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'down', 'right', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'down', 'right'], ['right', 'right', 'down', 'right', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'down', 'down', 'right', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'down', 'right', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'down', 'right'], ['right', 'right', 'right', 'down', 'right', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'down', 'down', 'right', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'down', 'right'], ['right', 'right', 'right', 'right', 'down', 'right', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'right'], ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'down'], ['right', 'right', 'right', 'right', 'right', 'right', 'down', 'down']]
>>> 
>>> len([r for r in (result) if r.count('down') == 3-1])
112
>>> 
>>> len(result)
128
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		lendata, digits = m+n-2, 2
		List, result = ['right']*(lendata), []
		
		data = range(lendata)
		
		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			sample = List[:]
			sample[nums[0]], sample[nums[1]] = ['down']*2
			result += [sample]
			
		return len([r for r in make_unique(result) if r.count('down') == n-1])

	
>>> Solution().uniquePaths(23, 12)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    Solution().uniquePaths(23, 12)
  File "<pyshell#239>", line 14, in uniquePaths
    return len([r for r in make_unique(result) if r.count('down') == n-1])
NameError: name 'make_unique' is not defined
>>> 
>>> class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		lendata, digits = m+n-2, 2
		List, result = ['right']*(lendata), []

		data = range(lendata)

		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			sample = List[:]
			sample[nums[0]], sample[nums[1]] = ['down']*2
			result += [sample]

		return len([r for r in mmin.make_unique(result) if r.count('down') == n-1])

	
>>> Solution().uniquePaths(23, 12)
0
>>> 
>>> Solution().uniquePaths(23, 12)
0
>>> 
>>> Solution().uniquePaths(7, 3)
28
>>> Solution().uniquePaths(7, 30)
0
>>> 
>>> Solution().uniquePaths(7, 4)
0
>>> 
>>> Solution().uniquePaths(7, 2)
7
>>> Solution().uniquePaths(7, 1)
0
>>> 
>>> Solution().uniquePaths(7, 0)
0
>>> Solution().uniquePaths(1, 2)
1
>>> 
>>> Solution().uniquePaths(3, 7)
0
>>> 
>>> Solution().uniquePaths(30, 7)
0
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, 2
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*2
	result += [sample]

return len([r for r in mmin.make_unique(result) if r.count('down') == n-1])
''')
Traceback (most recent call last):
  File "<pyshell#263>", line 16, in <module>
    ''')
  File "<string>", line 15
SyntaxError: 'return' outside function
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, 2
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*2
	result += [sample]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
0
>>> 
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, 2
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*2
	result += [sample]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
0
>>> 
>>> [r for r in mmin.make_unique(result) if r.count('down') == n-1]
[]
>>> [r for r in mmin.make_unique(result)]

>>> len([r for r in mmin.make_unique(result)])
630
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, 2
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = List[:]
	sample[nums[0]], sample[nums[1]] = ['down']*(n-1)
	result += [sample]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
Traceback (most recent call last):
  File "<pyshell#273>", line 16, in <module>
    ''')
  File "<string>", line 12, in <module>
ValueError: too many values to unpack (expected 2)
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[tuple(nums)] = ['down']*(n-1)
	result += [sample.tolist()]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
Traceback (most recent call last):
  File "<pyshell#275>", line 16, in <module>
    ''')
  File "<string>", line 12, in <module>
IndexError: too many indices for array
>>> 
>>> nums
[0, 0, 0, 0, 0, 0]
>>> 
>>> sample[tuple(nums)]
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    sample[tuple(nums)]
IndexError: too many indices for array
>>> 
>>> sample
array(['right', 'right', 'right', 'right', 'right', 'right', 'right',
       'right', 'right', 'right', 'right', 'right', 'right', 'right',
       'right', 'right', 'right', 'right', 'right', 'right', 'right',
       'right', 'right', 'right', 'right', 'right', 'right', 'right',
       'right', 'right', 'right', 'right', 'right', 'right', 'right'],
      dtype='<U5')
>>> sample[(nums)]
array(['right', 'right', 'right', 'right', 'right', 'right'], dtype='<U5')
>>> 
>>> List
['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
>>> len(list)
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    len(list)
TypeError: object of type 'type' has no len()
>>> len(List)
35
>>> 
>>> n
7
>>> n-1
6
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	result += [sample.tolist()]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
Traceback (most recent call last):
  File "<pyshell#290>", line 16, in <module>
    ''')
  File "<string>", line 12, in <module>
KeyboardInterrupt

>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	result += [[], [sample.tolist()]][r.count('down') == n-1]

print(len(mmin.make_unique(result))
''')
Traceback (most recent call last):
  File "<pyshell#291>", line 16, in <module>
    ''')
  File "<string>", line 15
    print(len(mmin.make_unique(result))
                                      ^

SyntaxError: unexpected EOF while parsing
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	result += [[], [sample.tolist()]][r.count('down') == n-1]

print(len(mmin.make_unique(result)))
''')
Traceback (most recent call last):
  File "<pyshell#293>", line 16, in <module>
    ''')
  File "<string>", line 13, in <module>
NameError: name 'r' is not defined
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	result += [[], [sample.tolist()]][r.count('down') == n-1]

print(len(mmin.make_unique(result)))
''')
KeyboardInterrupt
>>> 
>>> np.array()
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    np.array()
TypeError: array() missing required argument 'object' (pos 1)
>>> np.array(2)
array(2)
>>> np.array(2).count
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    np.array(2).count
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> np.array([2]).count
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    np.array([2]).count
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	samplelst = sample.tolist()
	result += [[], [samplelst]][samplelst.count('down') == n-1]

print(len(mmin.make_unique(result)))


''')
KeyboardInterrupt
>>> 
>>> 
>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	samplelst = sample.tolist()
	result += [[], [samplelst]][samplelst.count('down') == n-1]

print(len(mmin.make_unique(result)))


''')
Traceback (most recent call last):
  File "<pyshell#303>", line 19, in <module>
    ''')
  File "<string>", line 12, in <module>
KeyboardInterrupt

>>> 
>>> lendata, digits = 100, 2; data = range(lendata)
>>> [[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)]

>>> 
>>> np.array([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])
array([[ 0,  0],
       [ 0,  1],
       [ 0,  2],
       ...,
       [99, 97],
       [99, 98],
       [99, 99]])
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
>>> 

>>> lendata, digits = 100, 2; data = range(lendata)
>>> 
 RESTART: D:\SL\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Reading and Writing Zipped Docs\Polynomul Research\PolyResearchModules.pyw 
>>> 
>>> 

>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200]
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200]
NameError: name 'lendata' is not defined
>>> 
>>> lendata, digits = 100, 2; data = range(lendata)
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200]
'[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19], [0, 20], [0, 21], [0, 22], [0'
>>> len(str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200])
200
>>> len(str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)]))
98000
>>> 
>>> 

>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200].replace(']], [', ']\n').replace(', [', '\t[')
'[[0, 0]\t[0, 1]\t[0, 2]\t[0, 3]\t[0, 4]\t[0, 5]\t[0, 6]\t[0, 7]\t[0, 8]\t[0, 9]\t[0, 10]\t[0, 11]\t[0, 12]\t[0, 13]\t[0, 14]\t[0, 15]\t[0, 16]\t[0, 17]\t[0, 18]\t[0, 19]\t[0, 20]\t[0, 21]\t[0, 22]\t[0'
>>> 
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[2:200].replace(']], [', ']\n').replace(', [', '\t[')
'0, 0]\t[0, 1]\t[0, 2]\t[0, 3]\t[0, 4]\t[0, 5]\t[0, 6]\t[0, 7]\t[0, 8]\t[0, 9]\t[0, 10]\t[0, 11]\t[0, 12]\t[0, 13]\t[0, 14]\t[0, 15]\t[0, 16]\t[0, 17]\t[0, 18]\t[0, 19]\t[0, 20]\t[0, 21]\t[0, 22]\t[0'
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[1:200].replace(']], [', ']\n').replace(', [', '\t[')
'[0, 0]\t[0, 1]\t[0, 2]\t[0, 3]\t[0, 4]\t[0, 5]\t[0, 6]\t[0, 7]\t[0, 8]\t[0, 9]\t[0, 10]\t[0, 11]\t[0, 12]\t[0, 13]\t[0, 14]\t[0, 15]\t[0, 16]\t[0, 17]\t[0, 18]\t[0, 19]\t[0, 20]\t[0, 21]\t[0, 22]\t[0'
>>> 
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[1:200].replace(']], [', ']\n').replace(', [', '\t[')
KeyboardInterrupt
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200].replace('[','').replace(']','')
'0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0, 21, 0, 22, 0'
>>> 
>>> str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)])[:200].replace('[','').replace(']','').replace(', ','\n')
'0\n0\n0\n1\n0\n2\n0\n3\n0\n4\n0\n5\n0\n6\n0\n7\n0\n8\n0\n9\n0\n10\n0\n11\n0\n12\n0\n13\n0\n14\n0\n15\n0\n16\n0\n17\n0\n18\n0\n19\n0\n20\n0\n21\n0\n22\n0'
>>> 
>>> ppc.copy(str([[(i//lendata**d)%lendata for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 99, 2; data = range(lendata)
>>> ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> lendata, digits = 89, 2; data = range(lendata)
>>> ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 79, 2; data = range(lendata); ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 50, 2; data = range(lendata); ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 30, 2; data = range(lendata); ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> lendata, digits = 25, 2; data = range(lendata); ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 15, 2; data = range(lendata); ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> 12*23
276
>>> ppc.copy(str([[i, d] for d in range(13) for i in range(24)]).replace('[','').replace(']','').replace(', ','\n'))
>>> ppc.copy(str([[i, d] for d in range(1,13+1) for i in range(1, 24+1)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> {(1, 1):1,
		(1, 2):1,
		(1, 3):1,
		(1, 4):1,
		(1, 5):1,
		(1, 6):1,
		(1, 7):1,
		(1, 8):1,
		(1, 9):1,
		(1, 10):1,
		(1, 11):1,
		(1, 12):1,
		(1, 13):1,
		(1, 14):1,
		(1, 15):1,
		(2, 1):1,
		(2, 2):2,
		(2, 3):3,
		(2, 4):4,
		(2, 5):5,
		(2, 6):6,
		(2, 7):7,
		(2, 8):8,
		(2, 9):9,
		(2, 10):10,
		(2, 11):11,
		(2, 12):12,
		(2, 13):13,
		(2, 14):14,
		(2, 15):15,
		(3, 1):1,
		(3, 2):3,
		(3, 3):6,
		(3, 4):10,
		(3, 5):15,
		(3, 6):21,
		(3, 7):28,
		(3, 8):36,
		(3, 9):45,
		(3, 10):55,
		(3, 11):66,
		(3, 12):78,
		(3, 13):91,
		(3, 14):105,
		(3, 15):120,
		(4, 1):1,
		(4, 2):4,
		(4, 3):10,
		(4, 4):20,
		(4, 5):35,
		(4, 6):56,
		(4, 7):84,
		(4, 8):120,
		(4, 9):165,
		(4, 10):220,
		(4, 11):286,
		(4, 12):364,
		(4, 13):455,
		(4, 14):560,
		(4, 15):680,
		(5, 1):1,
		(5, 2):5,
		(5, 3):15,
		(5, 4):35,
		(5, 5):70,
		(5, 6):126,
		(5, 7):210,
		(5, 8):330,
		(5, 9):495,
		(5, 10):715,
		(5, 11):1001,
		(5, 12):1365,
		(5, 13):1820,
		(5, 14):2380,
		(5, 15):3060,
		(6, 1):1,
		(6, 2):6,
		(6, 3):21,
		(6, 4):56,
		(6, 5):126,
		(6, 6):252,
		(6, 7):462,
		(6, 8):792,
		(6, 9):1287,
		(6, 10):2002,
		(6, 11):3003,
		(6, 12):4368,
		(6, 13):6188,
		(6, 14):8568,
		(6, 15):11628,
		(7, 1):1,
		(7, 2):7,
		(7, 3):28,
		(7, 4):84,
		(7, 5):210,
		(7, 6):462,
		(7, 7):924,
		(7, 8):1716,
		(7, 9):3003,
		(7, 10):5005,
		(7, 11):8008,
		(7, 12):12376,
		(7, 13):18564,
		(7, 14):27132,
		(7, 15):38760,
		(8, 1):1,
		(8, 2):8,
		(8, 3):36,
		(8, 4):120,
		(8, 5):330,
		(8, 6):792,
		(8, 7):1716,
		(8, 8):3432,
		(8, 9):6435,
		(8, 10):11440,
		(8, 11):19448,
		(8, 12):31824,
		(8, 13):50388,
		(8, 14):77520,
		(8, 15):116280,
		(9, 1):1,
		(9, 2):9,
		(9, 3):45,
		(9, 4):165,
		(9, 5):495,
		(9, 6):1287,
		(9, 7):3003,
		(9, 8):6435,
		(9, 9):12870,
		(9, 10):24310,
		(9, 11):43758,
		(9, 12):75582,
		(9, 13):125970,
		(9, 14):203490,
		(9, 15):319770,
		(10, 1):1,
		(10, 2):10,
		(10, 3):55,
		(10, 4):220,
		(10, 5):715,
		(10, 6):2002,
		(10, 7):5005,
		(10, 8):11440,
		(10, 9):24310,
		(10, 10):48620,
		(10, 11):92378,
		(10, 12):167960,
		(10, 13):293930,
		(10, 14):497420,
		(10, 15):817190,
		(11, 1):1,
		(11, 2):11,
		(11, 3):66,
		(11, 4):286,
		(11, 5):1001,
		(11, 6):3003,
		(11, 7):8008,
		(11, 8):19448,
		(11, 9):43758,
		(11, 10):92378,
		(11, 11):184756,
		(11, 12):352716,
		(11, 13):646646,
		(11, 14):1144066,
		(11, 15):1961256,
		(12, 1):1,
		(12, 2):12,
		(12, 3):78,
		(12, 4):364,
		(12, 5):1365,
		(12, 6):4368,
		(12, 7):12376,
		(12, 8):31824,
		(12, 9):75582,
		(12, 10):167960,
		(12, 11):352716,
		(12, 12):705432,
		(12, 13):1352078,
		(12, 14):2496144,
		(12, 15):4457400,
		(13, 1):1,
		(13, 2):13,
		(13, 3):91,
		(13, 4):455,
		(13, 5):1820,
		(13, 6):6188,
		(13, 7):18564,
		(13, 8):50388,
		(13, 9):125970,
		(13, 10):293930,
		(13, 11):646646,
		(13, 12):1352078,
		(13, 13):2704156,
		(13, 14):5200300,
		(13, 15):9657700,
		(14, 1):1,
		(14, 2):14,
		(14, 3):105,
		(14, 4):560,
		(14, 5):2380,
		(14, 6):8568,
		(14, 7):27132,
		(14, 8):77520,
		(14, 9):203490,
		(14, 10):497420,
		(14, 11):1144066,
		(14, 12):2496144,
		(14, 13):5200300,
		(14, 14):10400600,
		(14, 15):20058300,
		(15, 1):1,
		(15, 2):15,
		(15, 3):120,
		(15, 4):680,
		(15, 5):3060,
		(15, 6):11628,
		(15, 7):38760,
		(15, 8):116280,
		(15, 9):319770,
		(15, 10):817190,
		(15, 11):1961256,
		(15, 12):4457400,
		(15, 13):9657700,
		(15, 14):20058300,
		(15, 15):40116600,
		(16, 1):1,
		(17, 1):1,
		(18, 1):1,
		(19, 1):1,
		(20, 1):1,
		(21, 1):1,
		(22, 1):1,
		(23, 1):1,
		(24, 1):1,
		(16, 2):16,
		(17, 2):17,
		(18, 2):18,
		(19, 2):19,
		(20, 2):20,
		(21, 2):21,
		(22, 2):22,
		(23, 2):23,
		(24, 2):24,
		(16, 3):136,
		(17, 3):153,
		(18, 3):171,
		(19, 3):190,
		(20, 3):210,
		(21, 3):231,
		(22, 3):253,
		(23, 3):276,
		(24, 3):300,
		(16, 4):816,
		(17, 4):969,
		(18, 4):1140,
		(19, 4):1330,
		(20, 4):1540,
		(21, 4):1771,
		(22, 4):2024,
		(23, 4):2300,
		(24, 4):2600,
		(16, 5):3876,
		(17, 5):4845,
		(18, 5):5985,
		(19, 5):7315,
		(20, 5):8855,
		(21, 5):10626,
		(22, 5):12650,
		(23, 5):14950,
		(24, 5):17550,
		(16, 6):15504,
		(17, 6):20349,
		(18, 6):26334,
		(19, 6):33649,
		(20, 6):42504,
		(21, 6):53130,
		(22, 6):65780,
		(23, 6):80730,
		(24, 6):98280,
		(16, 7):54264,
		(17, 7):74613,
		(18, 7):100947,
		(19, 7):134596,
		(20, 7):177100,
		(21, 7):230230,
		(22, 7):296010,
		(23, 7):376740,
		(24, 7):475020,
		(16, 8):170544,
		(17, 8):245157,
		(18, 8):346104,
		(19, 8):480700,
		(20, 8):657800,
		(21, 8):888030,
		(22, 8):1184040,
		(23, 8):1560780,
		(24, 8):2035800,
		(16, 9):490314,
		(17, 9):735471,
		(18, 9):1081575,
		(19, 9):1562275,
		(20, 9):2220075,
		(21, 9):3108105,
		(22, 9):4292145,
		(23, 9):5852925,
		(24, 9):7888725,
		(16, 10):1307504,
		(17, 10):2042975,
		(18, 10):3124550,
		(19, 10):4686825,
		(20, 10):6906900,
		(21, 10):10015005,
		(22, 10):14307150,
		(23, 10):20160075,
		(24, 10):28048800,
		(16, 11):3268760,
		(17, 11):5311735,
		(18, 11):8436285,
		(19, 11):13123110,
		(20, 11):20030010,
		(21, 11):30045015,
		(22, 11):44352165,
		(23, 11):64512240,
		(24, 11):92561040,
		(16, 12):7726160,
		(17, 12):13037895,
		(18, 12):21474180,
		(19, 12):34597290,
		(20, 12):54627300,
		(21, 12):84672315,
		(22, 12):129024480,
		(23, 12):193536720,
		(24, 12):286097760,
		(16, 13):17383860,
		(17, 13):30421755,
		(18, 13):51895935,
		(19, 13):86493225,
		(20, 13):141120525,
		(21, 13):225792840,
		(22, 13):354817320,
		(23, 13):548354040,
		(24, 13):834451800,
		} [(m, n)]
Traceback (most recent call last):
  File "<pyshell#353>", line 343, in <module>
    } [(m, n)]
NameError: name 'm' is not defined
>>> 
>>> {(1, 1):1,
		(1, 2):1,
		(1, 3):1,
		(1, 4):1,
		(1, 5):1,
		(1, 6):1,
		(1, 7):1,
		(1, 8):1,
		(1, 9):1,
		(1, 10):1,
		(1, 11):1,
		(1, 12):1,
		(1, 13):1,
		(1, 14):1,
		(1, 15):1,
		(2, 1):1,
		(2, 2):2,
		(2, 3):3,
		(2, 4):4,
		(2, 5):5,
		(2, 6):6,
		(2, 7):7,
		(2, 8):8,
		(2, 9):9,
		(2, 10):10,
		(2, 11):11,
		(2, 12):12,
		(2, 13):13,
		(2, 14):14,
		(2, 15):15,
		(3, 1):1,
		(3, 2):3,
		(3, 3):6,
		(3, 4):10,
		(3, 5):15,
		(3, 6):21,
		(3, 7):28,
		(3, 8):36,
		(3, 9):45,
		(3, 10):55,
		(3, 11):66,
		(3, 12):78,
		(3, 13):91,
		(3, 14):105,
		(3, 15):120,
		(4, 1):1,
		(4, 2):4,
		(4, 3):10,
		(4, 4):20,
		(4, 5):35,
		(4, 6):56,
		(4, 7):84,
		(4, 8):120,
		(4, 9):165,
		(4, 10):220,
		(4, 11):286,
		(4, 12):364,
		(4, 13):455,
		(4, 14):560,
		(4, 15):680,
		(5, 1):1,
		(5, 2):5,
		(5, 3):15,
		(5, 4):35,
		(5, 5):70,
		(5, 6):126,
		(5, 7):210,
		(5, 8):330,
		(5, 9):495,
		(5, 10):715,
		(5, 11):1001,
		(5, 12):1365,
		(5, 13):1820,
		(5, 14):2380,
		(5, 15):3060,
		(6, 1):1,
		(6, 2):6,
		(6, 3):21,
		(6, 4):56,
		(6, 5):126,
		(6, 6):252,
		(6, 7):462,
		(6, 8):792,
		(6, 9):1287,
		(6, 10):2002,
		(6, 11):3003,
		(6, 12):4368,
		(6, 13):6188,
		(6, 14):8568,
		(6, 15):11628,
		(7, 1):1,
		(7, 2):7,
		(7, 3):28,
		(7, 4):84,
		(7, 5):210,
		(7, 6):462,
		(7, 7):924,
		(7, 8):1716,
		(7, 9):3003,
		(7, 10):5005,
		(7, 11):8008,
		(7, 12):12376,
		(7, 13):18564,
		(7, 14):27132,
		(7, 15):38760,
		(8, 1):1,
		(8, 2):8,
		(8, 3):36,
		(8, 4):120,
		(8, 5):330,
		(8, 6):792,
		(8, 7):1716,
		(8, 8):3432,
		(8, 9):6435,
		(8, 10):11440,
		(8, 11):19448,
		(8, 12):31824,
		(8, 13):50388,
		(8, 14):77520,
		(8, 15):116280,
		(9, 1):1,
		(9, 2):9,
		(9, 3):45,
		(9, 4):165,
		(9, 5):495,
		(9, 6):1287,
		(9, 7):3003,
		(9, 8):6435,
		(9, 9):12870,
		(9, 10):24310,
		(9, 11):43758,
		(9, 12):75582,
		(9, 13):125970,
		(9, 14):203490,
		(9, 15):319770,
		(10, 1):1,
		(10, 2):10,
		(10, 3):55,
		(10, 4):220,
		(10, 5):715,
		(10, 6):2002,
		(10, 7):5005,
		(10, 8):11440,
		(10, 9):24310,
		(10, 10):48620,
		(10, 11):92378,
		(10, 12):167960,
		(10, 13):293930,
		(10, 14):497420,
		(10, 15):817190,
		(11, 1):1,
		(11, 2):11,
		(11, 3):66,
		(11, 4):286,
		(11, 5):1001,
		(11, 6):3003,
		(11, 7):8008,
		(11, 8):19448,
		(11, 9):43758,
		(11, 10):92378,
		(11, 11):184756,
		(11, 12):352716,
		(11, 13):646646,
		(11, 14):1144066,
		(11, 15):1961256,
		(12, 1):1,
		(12, 2):12,
		(12, 3):78,
		(12, 4):364,
		(12, 5):1365,
		(12, 6):4368,
		(12, 7):12376,
		(12, 8):31824,
		(12, 9):75582,
		(12, 10):167960,
		(12, 11):352716,
		(12, 12):705432,
		(12, 13):1352078,
		(12, 14):2496144,
		(12, 15):4457400,
		(13, 1):1,
		(13, 2):13,
		(13, 3):91,
		(13, 4):455,
		(13, 5):1820,
		(13, 6):6188,
		(13, 7):18564,
		(13, 8):50388,
		(13, 9):125970,
		(13, 10):293930,
		(13, 11):646646,
		(13, 12):1352078,
		(13, 13):2704156,
		(13, 14):5200300,
		(13, 15):9657700,
		(14, 1):1,
		(14, 2):14,
		(14, 3):105,
		(14, 4):560,
		(14, 5):2380,
		(14, 6):8568,
		(14, 7):27132,
		(14, 8):77520,
		(14, 9):203490,
		(14, 10):497420,
		(14, 11):1144066,
		(14, 12):2496144,
		(14, 13):5200300,
		(14, 14):10400600,
		(14, 15):20058300,
		(15, 1):1,
		(15, 2):15,
		(15, 3):120,
		(15, 4):680,
		(15, 5):3060,
		(15, 6):11628,
		(15, 7):38760,
		(15, 8):116280,
		(15, 9):319770,
		(15, 10):817190,
		(15, 11):1961256,
		(15, 12):4457400,
		(15, 13):9657700,
		(15, 14):20058300,
		(15, 15):40116600,
		(16, 1):1,
		(17, 1):1,
		(18, 1):1,
		(19, 1):1,
		(20, 1):1,
		(21, 1):1,
		(22, 1):1,
		(23, 1):1,
		(24, 1):1,
		(16, 2):16,
		(17, 2):17,
		(18, 2):18,
		(19, 2):19,
		(20, 2):20,
		(21, 2):21,
		(22, 2):22,
		(23, 2):23,
		(24, 2):24,
		(16, 3):136,
		(17, 3):153,
		(18, 3):171,
		(19, 3):190,
		(20, 3):210,
		(21, 3):231,
		(22, 3):253,
		(23, 3):276,
		(24, 3):300,
		(16, 4):816,
		(17, 4):969,
		(18, 4):1140,
		(19, 4):1330,
		(20, 4):1540,
		(21, 4):1771,
		(22, 4):2024,
		(23, 4):2300,
		(24, 4):2600,
		(16, 5):3876,
		(17, 5):4845,
		(18, 5):5985,
		(19, 5):7315,
		(20, 5):8855,
		(21, 5):10626,
		(22, 5):12650,
		(23, 5):14950,
		(24, 5):17550,
		(16, 6):15504,
		(17, 6):20349,
		(18, 6):26334,
		(19, 6):33649,
		(20, 6):42504,
		(21, 6):53130,
		(22, 6):65780,
		(23, 6):80730,
		(24, 6):98280,
		(16, 7):54264,
		(17, 7):74613,
		(18, 7):100947,
		(19, 7):134596,
		(20, 7):177100,
		(21, 7):230230,
		(22, 7):296010,
		(23, 7):376740,
		(24, 7):475020,
		(16, 8):170544,
		(17, 8):245157,
		(18, 8):346104,
		(19, 8):480700,
		(20, 8):657800,
		(21, 8):888030,
		(22, 8):1184040,
		(23, 8):1560780,
		(24, 8):2035800,
		(16, 9):490314,
		(17, 9):735471,
		(18, 9):1081575,
		(19, 9):1562275,
		(20, 9):2220075,
		(21, 9):3108105,
		(22, 9):4292145,
		(23, 9):5852925,
		(24, 9):7888725,
		(16, 10):1307504,
		(17, 10):2042975,
		(18, 10):3124550,
		(19, 10):4686825,
		(20, 10):6906900,
		(21, 10):10015005,
		(22, 10):14307150,
		(23, 10):20160075,
		(24, 10):28048800,
		(16, 11):3268760,
		(17, 11):5311735,
		(18, 11):8436285,
		(19, 11):13123110,
		(20, 11):20030010,
		(21, 11):30045015,
		(22, 11):44352165,
		(23, 11):64512240,
		(24, 11):92561040,
		(16, 12):7726160,
		(17, 12):13037895,
		(18, 12):21474180,
		(19, 12):34597290,
		(20, 12):54627300,
		(21, 12):84672315,
		(22, 12):129024480,
		(23, 12):193536720,
		(24, 12):286097760,
		(16, 13):17383860,
		(17, 13):30421755,
		(18, 13):51895935,
		(19, 13):86493225,
		(20, 13):141120525,
		(21, 13):225792840,
		(22, 13):354817320,
		(23, 13):548354040,
		(24, 13):834451800,
		} [(7, 30)]
Traceback (most recent call last):
  File "<pyshell#355>", line 343, in <module>
    } [(7, 30)]
KeyError: (7, 30)
>>> 
>>> (25, 9)[::-1]
(9, 25)
>>> 13*23
299
>>> 53*4
212
>>> 51*9
459
>>> 50*15
750
>>> 30*15
450
>>> ppc.copy(str([[i, d] for d in range(1,30+1) for i in range(1, 10+1)]).replace('[','').replace(']','').replace(', ','\n'))
>>> ppc.copy(str([[i, d] for d in range(1,30+1) for i in range(1, 10+1)]+[[d, i] for d in range(1,30+1) for i in range(1, 10+1)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> 

>>> ppc.copy(str([[i, d] for d in range(1,50+1) for i in range(1, 10+1)]+[[d, i] for d in range(1,50+1) for i in range(1, 10+1)]).replace('[','').replace(']','').replace(', ','\n'))
>>> ppc.copy(str([[i, d] for d in range(1,50+1) for i in range(1, 10)]+[[d, i] for d in range(1,50+1) for i in range(1, 10+1)]).replace('[','').replace(']','').replace(', ','\n'))
>>> ppc.copy(str([[i, d] for d in range(1,50+1) for i in range(1, 10)]+[[d, i] for d in range(1,50+1) for i in range(1, 10)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> ppc.copy(str([[i, d] for d in range(51, 52) for i in range(1, 10)]+[[d, i] for d in range(51, 52) for i in range(1, 10)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 

>>> ppc.copy(str([[i, d] for d in range(51, 52) for i in range(1, 10)]+[[d, i] for d in range(51, 52) for i in range(1, 10)]).replace('[','').replace(']','').replace(', ','\n'))
>>> 

>>> mma.m.factorial(7)
5040
>>> mma.m.factorial(7)/mma.m.factorial(7-3)
210.0
>>> mma.m.factorial(7)/mma.m.factorial(7-3)/mma.m.factorial(3)
35.0
>>> mma.m.factorial(7+3-1)/mma.m.factorial(7-1)/mma.m.factorial(3)
84.0
>>> n, r = 2, m+n-2
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    n, r = 2, m+n-2
NameError: name 'm' is not defined
>>> 
>>> m, n = 7, 3
>>> 
>>> n, r = 2, m+n-2
>>> 
>>> n
2
>>> r
8
>>> 
>>> mma.m.factorial(n)/mma.m.factorial(n-r)
Traceback (most recent call last):
  File "<pyshell#388>", line 1, in <module>
    mma.m.factorial(n)/mma.m.factorial(n-r)
ValueError: factorial() not defined for negative values
>>> 
>>> mma.m.factorial(n)/mma.m.factorial(n-r)/mma.m.factorial(r)
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    mma.m.factorial(n)/mma.m.factorial(n-r)/mma.m.factorial(r)
ValueError: factorial() not defined for negative values
>>> 
>>> 

>>> exec('''

m, n = 30, 7
lendata, digits = m+n-2, n-1
List, result = ['right']*(lendata), []

data = range(lendata)

for i in range(lendata**digits):
	nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
	sample = np.array(List[:])
	sample[(nums)] = ['down']*(n-1)
	result += [sample.tolist()]

print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))
''')
Traceback (most recent call last):
  File "<pyshell#393>", line 16, in <module>
    ''')
  File "<string>", line 12, in <module>
KeyboardInterrupt
>>> del result
>>> 
>>> 59**5
714924299
>>> 11**18
5559917313492231481
>>> 11*18
198
>>> 59*5
295
>>> lendata, digits = 99, 2; data = range(lendata) ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits) if np.product([(i//lendata**d)%lendata+1 for d in range(digits)[::-1]]) < 301]).replace('[','').replace(']','').replace(', ','\n'))
SyntaxError: invalid syntax
>>> 
>>> lendata, digits = 99, 2; data = range(lendata);ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits) if np.product([(i//lendata**d)%lendata+1 for d in range(digits)[::-1]]) < 301]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
>>> lendata, digits = 990, 2; data = range(lendata);ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits) if np.product([(i//lendata**d)%lendata+1 for d in range(digits)[::-1]]) < 301]).replace('[','').replace(']','').replace(', ','\n'))
>>> lendata, digits = 100, 2; data = range(lendata);ppc.copy(str([[(i//lendata**d)%lendata+1 for d in range(digits)[::-1]] for i in range(lendata**digits) if np.product([(i//lendata**d)%lendata+1 for d in range(digits)[::-1]]) < 301]).replace('[','').replace(']','').replace(', ','\n'))
>>> 
