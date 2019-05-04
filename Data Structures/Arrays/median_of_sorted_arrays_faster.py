"""
Problem Statement - https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
import math


def maximum(a, b):
    return a if a > b else b


def minimum(a, b):
    return a if a < b else b


def find_sorted_arrays(list_a, list_b) -> float:
    """
    Make a third list, which contains element in sorted order, then find median
    in log(n+m)
    :param list_a:
    :param list_b:
    :return:
    """
    if len(list_b) < len(list_a):
        list_a, list_b = list_b, list_a
    n = len(list_a)
    m = len(list_b)
    min_index = 0
    max_index = n
    global result, part_a_index, part_b_index
    while min_index <= max_index:
        part_a_index = int((min_index + max_index) / 2)
        part_b_index = int(((n + m + 1) / 2) - part_a_index)
        print(part_a_index, part_b_index)
        """
        We check if the element after the split position in list a, is greater than element at
        the split position in list b, if so it signifies that all element before split position in list
        b is less than or equal to that of all elements after split position in list a
        """
        if (part_a_index < n and part_b_index > 0) and list_b[part_b_index - 1] > list_a[part_a_index]:
            min_index = min_index + 1
        elif (part_a_index > 0 and part_b_index < m) and list_b[part_b_index] < list_a[part_a_index - 1]:
            max_index = max_index - 1
        else:
            if part_a_index == 0:
                result = list_b[part_b_index - 1]
            elif part_b_index == 0:
                result = list_a[part_a_index - 1]
            else:
                print(list_a[:part_a_index], list_a[part_a_index:])
                print(list_b[:part_b_index], list_b[part_b_index:])
                result = maximum(list_a[part_a_index - 1], list_b[part_b_index - 1])
            break
    if (n + m) % 2 == 1:
        print('1', result)
        return result
    if part_a_index == n:
        print('2')
        return (result + list_b[part_b_index]) / 2
    if part_b_index == m:
        print('3', (result + list_a[part_a_index]) / 2)
        return (result + list_a[part_a_index]) / 2
    print(result)
    return (result + minimum(list_a[part_a_index], list_b[part_b_index])) / 2


if __name__ == "__main__":
    assert find_sorted_arrays([1], [1]) == 1
    assert find_sorted_arrays([-7, -2, 0, 3, 4], [1, 5, 9]) == 2.0
    assert find_sorted_arrays([-10, 2, 9, 71, 82], [-7, -1, 3, 4, 5, 6, 7, 11, 17]) == 5.5
    assert find_sorted_arrays([100, 200, 300, 400, 500], [-7]) == 250.0
    assert find_sorted_arrays([1, 3], [2]) == 2
    assert find_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_sorted_arrays([], [1, 2, 3]) == 2
    assert find_sorted_arrays([2, 3, 4, 5, 6, 7], [1]) == 4
