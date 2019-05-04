"""
Problem Statement - https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
import math


def sorted_list_median(_list):
    n = len(_list)
    if len(_list) == 1:
        return _list[0]
    if n % 2 == 0:
        return (_list[int(n/2) - 1] + _list[int(n/2)]) / 2
    else:
        return _list[int(n/2)]

  
def find_sorted_arrays(list_a, list_b) -> float:
    """
    Make a third list, which contains element in sorted order, then find median
    O(n+m)
    :param list_a:
    :param list_b:
    :return:
    """
    len_a, len_b = len(list_a), len(list_b)
    combined_list = []
    a = 0
    b = 0
    for i in range(len_a + len_b):
        if a > len_a - 1:
            combined_list = combined_list + list_b[b:]
            break
        if b > len_b - 1:
            combined_list = combined_list + list_a[a:]
            break
        if list_a[a] > list_b[b]:
            combined_list.append(list_b[b])
            b += 1

        else:
            combined_list.append(list_a[a])
            a += 1
    return  sorted_list_median(combined_list)


if __name__ == "__main__":
    assert find_sorted_arrays([-7, -2, 0, 3, 4], [1, 5, 9]) == 2.0
    assert find_sorted_arrays([-10, 2, 9, 71, 82], [-7, -1, 3, 4, 5, 6, 7, 11, 17]) == 5.5
    assert find_sorted_arrays([100, 200, 300, 400, 500], [-7]) == 250.0
    assert find_sorted_arrays([1, 3], [2]) == 2
    assert find_sorted_arrays([1, 2], [3, 4]) == 2.5
