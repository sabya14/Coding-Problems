"""
Problem Statement :  https://www.hackerearth.com/practice/data-structures/hash-tables/
basics-of-hash-tables/practice-problems/algorithm/exists/
"""
from collections import deque
from sys import argv, stdin


def hash_insert(element, hash_table, size):
	index = element % size
	if hash_table[index] is not None:
		hash_table[index].append(element)
	else:
		hash_table[index] = [element]


def hash_search(element, hash_table, size):
	index = element % size
	if hash_table[index] is not None:
		if float(element) in hash_table[index]:
			print("Yes")
			return
		else:
			print("No")
	else:
		print("No")


input_file = open(argv[1]) if len(argv) - 1 > 0 else stdin
inputs = deque()
elements = list(map(int, input_file.read().split()))
inputs.extend(elements)
no_of_test_cases = inputs.popleft()
for _ in range(no_of_test_cases):
	size_of_array = inputs.popleft()
	hash_table = dict.fromkeys(list(range(0, 5*size_of_array)))
	array = []
	for i in range(size_of_array):
		array.append(inputs.popleft())
	for element in array:
		hash_insert(element, hash_table, 5*size_of_array)
	no_of_queries = inputs.popleft()
	search_queries_list = []
	for i in range(no_of_queries):
		search_queries_list.append(inputs.popleft())
	for element in search_queries_list:
		hash_search(element, hash_table, 5*size_of_array)



