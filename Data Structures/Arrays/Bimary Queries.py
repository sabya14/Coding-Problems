"""
Problem Statement - https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/
"""


def is_ever_or_odd(number, left, right):
	"""
	:param number: The list of number
	:param left: The left index of the subarray to be considered
	:param right: The right index of the subarray to be considered
	:return: None
	"""
	# A binary no ending with 0 is even
	if number[right-1] == '0':
		print('EVEN')
	else:
		print('ODD')


def flip_bit(list, index):
	# flip the index passed
	list[index - 1] = "1" if not int(list[index - 1]) else "0"
	return list


length_of_int, no_of_test_cases = map(int, input().split())
int_list = list(map(str, input().split()))
for i in range(no_of_test_cases):
	# split the query into proper parameters
	query_list = list(map(int, input().split()))
	if query_list[0] == 1:
		int_list = flip_bit(int_list, query_list[1])
	if query_list[0] == 0:
		is_ever_or_odd(int_list, left=query_list[1], right=query_list[2])

