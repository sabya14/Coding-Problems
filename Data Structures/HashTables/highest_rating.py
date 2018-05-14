"""
Problem Statement: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/
practice-problems/algorithm/highest-rating-f8ead57a/
"""


def find_highest_rating(Q, arr, M, size):
	possibilities = []
	for i in range(1, Q + 1):
		possibilities.append(i * M)
	hash_set = [0] * (size + 1)
	for elements in arr:
		hash_set[elements] = hash_set[elements] + 1
		for value in possibilities:
			index = value + elements
			index_1 = -value + elements
			if index > 0 and index < size:
				hash_set[index] = hash_set[index] + 1
			if index_1 > 0 and index_1 < size:
				hash_set[index_1] = hash_set[index_1] + 1
	return max(hash_set)


M = int(input())
Q = int(input())
N = int(input())
arr = list(map(int, input().split()))
output = find_highest_rating(Q, arr, M, N)
print(output)
