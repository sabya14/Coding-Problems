"""
Problem Statement - https://www.hackerearth.com/practice/data-structures/arrays/
multi-dimensional/practice-problems/algorithm/saul-goodmans-problem-statement/
"""


def find_result(alist, blist):
	print(alist.count(0) + blist.count(0))
	

no_of_test_cases = int(input())
for cases in range (no_of_test_cases):
	no_of_true_cells = int(input())
	alist, blist = [], []
	for cells in range (no_of_true_cells):
		x, y = map(int, input().split())
		alist.append(x-y)
		blist.append(y-x)
	# print(alist)	
	find_result(alist, blist)