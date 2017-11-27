
"""
����: ���� guess.txt ���������� ����� ��� ���������� 

(�������� �� http://www.biographyonline.net/people/famous-100.html ����� ����� �����)


�������� ���� "������ �� ����"

3 ������ ���������:
1) ������������ ����� ������ 1-10
2) ����� 1-50
3) ����� 1-100

- �� ������������ ���� �������� ������� ����
- ��������� ����� �������� � Google �� ����������
- �������� ~30-50 ������ ������ �� ��������� �� ����� �����������
- ������� �������� �������� � �������� �� ������������ ��� ����������
  (����� ������� �� ����������� ������ ��������� ����)
- ����� ������ ������� ��������� ��� ���

�.�. ���������� ������ ��������� �����, �.�. ������ ������ � ������� �������� ��������� � ���-�������.

�.�. ��� ������ �������� ���������� ����������� ������� ���������������� ������ � Google
�.�. ����� ������������ � Google image search API
https://ajax.googleapis.com/ajax/services/search/images? ��� ��. ��������
�� � ����� ������ ����� ������������� ������������ ����������� �� ���-�� ��������
�.�. ���������� ���������� �� ������ ���������� ���-�� ����������� (����������)
�������� ��� ������ ������� �������� �����������.
�.�. ���� �� ������ ����������� ����� N �������� (����������� API)


�.�. ���������� "��������������" ��������� ������ (�������� ������ ������ ����, 
������������ ������ ������ 1-30 ��������� � �.�.)
��� ����������� ���� ��� ��������� �������� �� ������������� �����

p.s. ������ ����� �������� �� xms@npp.itb.spb.ru
"""


import codecs
import random
import re
import sys


names = dict()
keys = dict()
difficulty = dict({1: 10, 2: 50, 3: 100})


def to_filename(filename):
    if filename is not None and filename != "":
        return filename
    return None


def read_data(filename):
    return codecs.open(filename, 'r').read()


def get_file_names(args):
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    valid_files = list()
    for filename in args:
        if to_filename(filename) is None:
            print('* Invalid filename - [%s]' % filename)
            continue
        valid_files.append(filename)
    return valid_files


def build_name_dict(file_data):
    names_dict = dict()

    i = 1
    for newline in re.compile('\n').split(file_data):
        names_dict.update({i: newline})
        i += 1

    return names_dict


def extract_pic_link_from_page(page_data, limit):
    matches = list(re.finditer("<div jsname=\"ik8THc\" class=\".+\">.+</div>", page_data))

    match = matches[random.randint(0, limit)]
    if match > limit:
        match = matches[random.randint(0, len(matches))]

    link = re.match("\"ou\":\".+\"", match.group())
    if link is None:
        return None

    link = link.string.split(":")
    if link is None:
        return None

    return link[1:-1]


def setup():
    files = get_file_names(["words"])
    for file in files:
        names_dict = build_name_dict(read_data(file))
        if names_dict is not None:
            i = len(names)
            for num, name in names_dict:
                i += 1
                names.update({i: name})


def main():
    setup()


if __name__ == '__main__':
    main()
