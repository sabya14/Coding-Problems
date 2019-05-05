"""
Problem Statement - 1.4 from the book of Cracking the coding interview - 6th edition
"""


def palindrome_checker(_string):
    """
    Check if a string is palindrome
    :param _string: The string to check
    :return: Boolean (True, False) if its palindrome or not
    """
    if len(_string) == 0:
        return False
    elif len(_string) == 1:
        return True
    else:
        char_dict = {}
        # Keep check of the count of char in string, when there is even number of count, the value will be false
        for _char in _string:
            if _char in char_dict:
                char_dict[_char] = not char_dict[_char]
            else:
                char_dict[_char] = True
        n = len(_string)
        # In a even length string, all char should be in even number
        if n % 2 == 0:
            a = [not x for x in char_dict.values()]
            return all([not x for x in char_dict.values()])
        else:
            # In a odd length string, all char should be in even number, only one should be single
            single_occurrence = [x for x in char_dict.values() if x is True]
            if len(single_occurrence) == 1:
                return True
            else:
                return False


if __name__ == "__main__":
    assert palindrome_checker("abba") is True
    assert palindrome_checker("abbc") is False
    assert palindrome_checker("daabbaad") is True
    assert palindrome_checker("aabcaa") is False
    assert palindrome_checker("aabaa") is True
    assert palindrome_checker("aabac") is False
    assert palindrome_checker("aabbdedbbaa") is True
