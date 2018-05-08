"""
Problem Statement: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/
practice-problems/algorithm/submatrix-updates-1/
"""

no_of_rows, no_of_columns, no_of_operations = map(int, input().split())
array = []
for i in range(no_of_rows):
	temp = list(map(int, input().split()))
	array.append(temp)

for i in range(no_of_operations):
	row, column, size, to_add = map(int, input().split())
	if row + size > no_of_rows + 1:
		row_limit = no_of_rows
	else:
		row_limit = row + size

	if column + size > no_of_columns + 1:
		col_limit = no_of_rows
	else:
		col_limit = column + size
	for row in range(row - 1, row_limit - 1):
		for col in range(column - 1, col_limit - 1):
			array[row][col] = array[row][col] + to_add

for row in range(no_of_rows):
	for col in range(no_of_columns):
		print(array[row][col], end =" ")
	print("")
