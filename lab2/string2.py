"""1.
Вх: строка. Если длина > 3, добавить в конец "ing",
если в конце нет уже "ing", иначе добавить "ly".
def v(s):

return


2.
Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
на 'good'.
Пример: So 'This music is not so bad!' -> This music is good!
"""

import re


def change_ending(s):
    if len(s) < 4:
        return s
    if s[len(s) - 3:] == "ing":
        return s + "ly"
    return s + "ing"


def change_bad(s):
    not_match = re.search('not', s)
    if not_match is None:
        return s

    bad_match = re.search('bad', s[not_match.start():])
    if bad_match is None:
        return s

    return s[:not_match.start()] + "good" + s[not_match.start() + bad_match.end():]


def main():
    print(change_bad("1 - bob you are not so bad man!"))
    print(change_bad("2 - mama bad one"))
    print(change_bad("3 - tim you are not mine"))
    print(change_ending("4 - tring"))
    print(change_ending("5 - tiig"))


if __name__ == '__main__':
    main()
