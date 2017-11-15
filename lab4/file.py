
"""
��������� �� ����� (��� - �������� ��������� ������)
��� ����� (����������� ������)

������� "�������" ������� ������� ���������� ������ ����� �� �����
�� ������ ���� ����, ������� ������� �� ��� (��� ��������).

������ ���� ����� ���� � ����� ������� � �������� ����������.
�������� "and" ['best", "then", "after", "then", ...]

������� , ��� ������ ������ ������������ ���� ������ � �����.

� ������� "��������" ������� ������������� ����� �����
������� �� ��������.
�.�. ���������� ����� - ���������� ����� ����� ���� ���������
� ������� ���������.

� �������� ����� ����� ������������ ����� ��������� ��� ����.�����. ��� ��������� �����
(��� ������ ����.�����. - ����)

����:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import codecs
import sys


def to_filename(filename):
    if filename is not None and filename != "":
        return filename
    return None


def read_data(filename):
    return codecs.open(filename, 'r').read()


def get_files(args):
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


def mem_dict(filename):
    work_dict = dict()
    return


def main():
    files = get_files(sys.argv[1:])


if __name__ == '__main__':
    main()
