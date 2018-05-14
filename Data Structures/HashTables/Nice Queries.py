"""
Problem Statement = https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/
practice-problems/algorithm/mandee-and-his-girlfriend-9a96aabd/
"""
size, no_of_queries = map(int, input().split())
hash = [0] * (size + 1)
diff = 0
for i in range(no_of_queries):
	type, index = map(int, input().split())
	if type == 2:
		if index > diff:
			print(-1)
			continue
		else:
			while diff >= index:
				if hash[diff] == diff:
					print(diff)
					break
				diff = hash[diff]
	else:
		if index > diff:
			diff = index
		hash[index] = diff
