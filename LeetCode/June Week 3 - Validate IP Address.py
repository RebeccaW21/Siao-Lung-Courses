from _functools import *

def addf(addend1,addend2): return addend1+addend2

def sum(list):
	if list != []: return reduce(addf,list)
	if list == []: return int()

def atau(nilai1,nilai2): return nilai1 or nilai2
def ataumul(daftar): return(reduce(atau,daftar))
    
def compare_one_value_to_others_or(the_value,*compared_value):
	statements = []

	for cv in compared_value:
		statements.append(the_value == cv)

	return ataumul(statements)
	
covto_or = compare_one_value_to_others_or

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


class Solution:
    def validIPAddress(self, IP: str) -> str:
        IPv4 = IP.split('.')
        IPv6 = IP.split(':')
        
        if len(IPv4) == 4:
            try:
                list(map(int, IPv4))
                if sum(list(map(lambda x: x not in IP, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~—– \t\n\r'))) < 89: return 'Neither'
                elif sum(list(map(lambda x: eval(x) < 256 and x != '00', IPv4))) > 3:
                    return 'IPv4'
                else: return 'Neither'
                
            except (SyntaxError, ValueError): return 'Neither'
            
        elif len(IPv6) == 8:
            try: list(map(lambda x: eval('0x'+x), IPv6))
            except SyntaxError: return 'Neither'
            
            if sum(list(map(lambda x: 0 < len(x) < 5, IPv6))) == 8: return 'IPv6'
            elif sum(list(map(lambda x: daofal('0', x) == '' and x != '0', IPv6))) > 0: return 'Neither'
            return 'Neither'
            
        else: return 'Neither'