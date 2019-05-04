"""
Problem Statement
https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/the-exam/
"""


def get_min(no_of_items, limit, no_of_visits):
	_min = 1
	while _min < no_of_items:
		if 2**(no_of_items - _min):
			pass
	return 0


def the_exam(no_of_items, limit, no_of_visits):
	magic_number = 0
	while no_of_visits > 0:
		magic_number = magic_number + get_min(no_of_items, limit, no_of_visits)
		no_of_visits -= 1
	return magic_number


if __name__ == "__main__":
	no_of_test_cases = int(input())
	for i in range(no_of_test_cases):
		items, max_limit, visits = map(int, input().split())
		print(the_exam(items, max_limit, visits))
