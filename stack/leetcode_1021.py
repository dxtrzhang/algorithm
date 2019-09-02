# -*- coding: utf8 -*-

"""
https://leetcode.com/problems/remove-outermost-parentheses/
"""


def remove_outer_parentheses(string: str) -> str:
    result = []
    cnt = 0
    for ch in string:
        if ch == '(':
            cnt += 1
            if cnt > 1:
                result.append(ch)
        else:
            cnt -= 1
            if cnt >= 1:
                result.append(ch)
    return ''.join(result)


if __name__ == '__main__':
    a = remove_outer_parentheses('(()())(())(()(()))')
    print(a)
