no_of_test_cases = int(input())
size = int(input())
for i in range(no_of_test_cases):
	alist = list(map(int, input().split()))
	values = [1]
	indexes = [alist[0]]

	for index, element in enumerate(alist[1:]):
		# print('index: ', index, 'element: ', element, alist[index], element > alist[index] )
		val = 0
		if element >= alist[index]:
			pos = index
			for pos, elements in enumerate(indexes):
				if elements <= element:
					val = val + 1
				# # indexes.pop()
				# pos = pos - 1
				# if pos < 0:
				# 	break
			indexes.append(element)
			values.append(val + 1)
		else:
			values.append(1)
			indexes.append(element)

	print(*values)