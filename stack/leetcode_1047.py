# -*- coding: utf8 -*-

"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


def remove_duplicates(string: str) -> str:
    result = []
    for ch in string:
        if result:
            if result[-1] == ch:
                result.pop()
                continue
        result.append(ch)
    return ''.join(result)


if __name__ == '__main__':
    remove_duplicates('abbaca')
