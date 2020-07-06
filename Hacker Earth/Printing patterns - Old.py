'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
r, c, cj, ci = list(map(int, input().split()))
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