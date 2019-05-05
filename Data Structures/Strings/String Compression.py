"""
String compression - 1.6 in Cracking the coding interview.
"""


def string_compression(_string):
    """
    Given a string aaabbbccd -> a3b3c2d1, return the same string if no change
    :param _string: The string to compress,
    :return: String, The compressed string
    """
    last_char = None
    last_index = -1
    last_char_count = 0
    info_dict = {}

    for index, _char in enumerate(_string):
        if last_char and last_char != _char:
            info_dict.update({last_index: last_char_count})
            last_char_count = 0
            last_char = None
            last_index = -1
        last_char_count += 1
        if last_char_count == 1:
            last_char = _char
            last_index = index
    # TO handle the last char
    info_dict.update({last_index: last_char_count})
    if all([True if x == 1 else False for x in info_dict.values()]):
        return _string
    new_string = ""
    for item, values in info_dict.items():
        new_string = new_string + _string[item] + f"{values}"
        # _string = _string[:item + 1] + f"{values}" + _string[item + values:]
    return new_string


if __name__ == "__main__":
    assert string_compression("aabcccccaaa") == "a2b1c5a3"
    assert string_compression("aabcda") == "a2b1c1d1a1"
    assert string_compression("abcd") == "abcd"
