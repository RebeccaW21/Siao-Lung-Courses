import numpy as np

def make_unique(the_list):
	the_unique_list = []

	for tlc in the_list:
		if tlc not in the_unique_list: the_unique_list.append(tlc)
	return the_unique_list

class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		lendata, digits = m+n-2, n-1
		List, result = ['right']*(lendata), []

		data = range(lendata)

		for i in range(lendata**digits):
			nums = [(i//lendata**d)%lendata for d in range(digits)[::-1]]
			sample = np.array(List[:])
			sample[(nums)] = ['down']*(n-1)
			result += [sample.tolist()]

		print(len([r for r in mmin.make_unique(result) if r.count('down') == n-1]))