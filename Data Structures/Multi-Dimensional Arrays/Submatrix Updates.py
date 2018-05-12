"""
Problem Statement: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/
practice-problems/algorithm/submatrix-updates-1/
"""

no_of_rows, no_of_columns, no_of_operations = map(int, input().split())
alist = []
blist = [(no_of_columns+1)*[0] for i in range(no_of_rows+1)]

for i in range(no_of_rows):
	alist.append(list(map(int, input().split())))
	blist.append([0] * no_of_rows)

for i in range(no_of_operations):
	r, c, s, d = [int(i) for i in input().split()]
	for i in range(r - 1, r - 1 + s):
		blist[i][c - 1] += d
		blist[i][c - 1 + s] -= d

for row in range(no_of_rows + 1):
	for col in range(1, no_of_columns + 1):
		blist[row][col] = blist[row][col] + blist[row][col - 1]

for row in range(no_of_rows):	
	for col in range(no_of_columns):
		alist[row][col] = alist[row][col] + blist[row][col]

for row in alist:
	print(*row)
