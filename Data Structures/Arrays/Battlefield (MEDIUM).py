"""
Problem Statement - https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/battlefield-13/
"""


def min_swap(string, size_of_string):
	"""
	Calculate the minimum swap required to bring all the Knights together(K)
	Implemented By sliding window method.
	:param string: The string to be checked
	:param size_of_string: The Size of the string passed
	:return: None, print( the min no of swap)
	"""
	no_of_k = string.count('K')
	no_of_ones = []
	count = 0
	# Special check for cycle formation, that is after n, 0 comes..
	for i in range(size_of_string + no_of_k):
		if i > size_of_string - 1:
			i = i - size_of_string
			print(i)
		if string[i] == "K":
			count = count + 1
		no_of_ones.append(count)
	max = 0
	for i in range(0, size_of_string + no_of_k):
		temp = no_of_ones[i] - no_of_ones[i - no_of_k]
		if temp > max:
			max = temp
	print(no_of_k - max)


no_of_test_cases = int(input())
for i in range(no_of_test_cases):
	size_of_string = int(input())
	string = input()
	min_swap(string, size_of_string)
