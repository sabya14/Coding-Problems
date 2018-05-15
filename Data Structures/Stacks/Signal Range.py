no_of_test_cases = int(input())
for i in range(no_of_test_cases):
	size = int(input())
	alist = list(map(int, input().split()))
	result = [1]
	stack_min = [(alist[0], 0)]

	for index, element in enumerate(alist[1:]):
		val = 0
		if element >= alist[index]:
			index = len(stack_min)
			while stack_min[-1][0] <= element:
				val = val + result[stack_min[-1][1]]
				stack_min.pop()
				if len(stack_min) == 0:
					break
			result.append(val + 1)
			stack_min.append((element, index + 1))
		else:
			result.append(1)
			stack_min.append((element, index + 1))
	print(*result)