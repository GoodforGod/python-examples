"""
    Вход: nameYYYY.html,
    Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
"""

import codecs
import re
import sys


def extract_name(filename):
    file_data = codecs.open(filename, 'r').read()
    name_book = dict()
    for match in re.finditer("<tr align=\"[a-zA-Z]+\"><td>[0-9]+</td><td>[a-zA-Z]+</td><td>[a-zA-Z]+</td>", file_data):
        m_values = list()
        for tag in re.finditer('<td *[0-9a-zA-Z"=]*> *[0-9a-zA-Z]+ *</td>', match.group()):
            m_values.append(extract_value(tag.group()))
        if len(m_values) != 3:
            continue
        name_book.update({int(m_values[0]): [m_values[1], m_values[2]]})
    return name_book


def extract_value(tagged_value):
    return tagged_value[4:-5]


def is_file_valid(filename):
    if re.match('name[0-9]{4}\.html', filename):
        li = filename.split('.')
        return li[4:]
    return None


# напечатать ТОП-10 муж и жен имен из всех переданных файлов
# для каждого переданного аргументом имени файла, вывести имена   extract_name
def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    for filename in args:
        if is_file_valid(filename) is None:
            print('* Invalid filename - [%s]' % filename)
            continue
        names_dict = extract_name(filename)
        if names_dict is None:
            continue

        print("Top 10 names from - ", filename)
        for i in range(10):
            name_list = names_dict.get(i)
            if name_list is None:
                continue

            print("Position - %s, [M]- %s, [W] - %s" % (i, name_list[0], name_list[1]))


if __name__ == '__main__':
    main()
