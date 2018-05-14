"""
Problem Statement = https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/
practice-problems/algorithm/mandee-and-his-girlfriend-9a96aabd/
"""
size, no_of_queries = map(int, input().split())
hash = {}
highest = 0
for i in range(no_of_queries):
	type, index = map(int, input().split())
	if type == 2:
		if index > highest:
			print(-1)
			continue
		while 1:
			if index > size:
				print(-1)
				break
			try:
				if hash[index]:
					print(index)
					break
			except KeyError as e:
				index = index + 1
				continue
	else:
		if index > highest:
			highest = index
		hash.update({index: highest})
