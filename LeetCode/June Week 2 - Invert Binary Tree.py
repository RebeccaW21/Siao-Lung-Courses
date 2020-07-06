from _functools import *

def addf(addend1,addend2): return addend1+addend2

def sum(list):
	if list != []: return reduce(addf,list)
	if list == []: return int()

def atau(nilai1,nilai2): return nilai1 or nilai2
def ataumul(daftar): return(reduce(atau, daftar))

def dstatial(the_function,the_list):
	#"Do something to all things in a list"
	
	the_new_list = []
	
	for tla in the_list:
		# if str(type(tla)) == "<class 'list'>": dstatial(the_function,the_list)			
		# else:
		the_new_list.append(the_function(tla))
		
	return the_new_list

def compare_one_value_to_others_or(the_value,*compared_value):
	statements = []

	for cv in compared_value:
		statements.append(the_value == cv)

	return ataumul(statements)
	
covto_or = compare_one_value_to_others_or

def group(list,number,extra_length=10):
	if number != 0:
		grouped_list = []
		
		try: len_list = len(list)
		except TypeError as errordesc:
			if repr(errordesc) == 'TypeError("object of type \'int\' has no len()")':
				len_list = number+1
		
		for a in range(0, len_list, int(number)):
			if type(list) == type(0): grouped_list.append('')
			else: grouped_list.append(list[a:a+number])
		
		if grouped_list == []: grouped_list.append('')
		
		return grouped_list
		
	else: pass #group([0]*extra_length,extra_length//2)

def daofal(the_object,the_list):
	#daofal "del an object from a list [in/from the front only]"
	
	sttl = str(type(the_list))
	
	if covto_or(sttl,
					"<class 'str'>",
					"<class 'list'>",
					"<class 'numpy.ndarray'>"):
		the_list = list(the_list)
	
	if sttl == "<class 'int'>":
		the_list = list(str(the_list))
		
	for a in range(len(the_list)):
		b = the_list[0]
		#print('b =',b)
		
		if b == the_object: del the_list[0]#; print('b is still the_object, which is',the_object)
		if b != the_object: break
		
	#print('\n')
	if sttl == "<class 'str'>":
		the_list1 = sum(the_list)
		if the_list1 == 0: return ''
		
		return the_list1
		
	if sttl == "<class 'int'>":
		the_list1 = sum(the_list)
		the_list2 = int(the_list1)
		
		return the_list2
		
	if sttl == "<class 'list'>":
		the_list1 = list(the_list)
	
		return the_list1
		
	if sttl == "<class 'numpy.ndarray'>":
		the_list1 = np.array(the_list)
	
		return the_list1

def countlistlvl(List):
    count = 0
    
    for i in List[::-1]:
        if i == ']': count += 1
        else: break
    
    return count
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        print(root)
        result = [int(r) for r in sum([r for r in str(root) if r in '0123456789,']).split(',') if r != '']
        
        rootstr = str(root).replace('TreeNode{val: ','[').replace('}',']').replace('left: ','').replace('right: ','').replace(', None','')
        rootlist = eval(rootstr)#[::-1]
        
        result = [[] for i in range(countlistlvl(rootstr))]
        print(rootlist)
        #print([rootlist[0]]+rootlist[1:][::-1])
        #print(result)
        
        '''resultindex = 0
        for r in rootlist: #print(r)
            if r.__class__ == int: result[resultindex] += [r]
            else:
                resultindex += 1
                result[resultindex] = r + result[resultindex]'''
        
        print(result)
        
        #print([result[0]]+dstatial(lambda x: x[::-1], group(result[1:], 2)))