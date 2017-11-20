"""
    Вход: nameYYYY.html,
    Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
"""

import codecs
import re
import sys


def to_filename(filename):
    if re.match('name[0-9]{4}\.html', filename):
        li = filename.split('.')
        return li[4:]
    return None


def read_data(filename):
    return codecs.open(filename, 'r').read()


def get_filenames(args):
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


def read_names_dict(file_data):
    man_book = dict()
    woman_book = dict()
    for match in re.finditer("<tr align=\"[a-zA-Z]+\"><td>[0-9]+</td><td>[a-zA-Z]+</td><td>[a-zA-Z]+</td>", file_data):
        m_values = list()
        for tag in re.finditer('<td *[0-9a-zA-Z"=]*> *[0-9a-zA-Z]+ *</td>', match.group()):
            m_values.append(remove_tags(tag.group()))
        if len(m_values) != 3:
            continue
        man_book.update({m_values[1]: int(m_values[0])})
        woman_book.update({m_values[2]: int(m_values[0])})
    return man_book, woman_book


def remove_tags(tagged_value):
    return tagged_value[4:-5]


def print_names(names_dict):
    names = list(names_dict.keys())
    names.sort()
    for i in range(10):
        name_position = names_dict.get(names[i])
        if name_position is None:
            name_position = -1

        print("Position - %s, Name - %s" % (name_position, names[i]))


# напечатать ТОП-10 муж и жен имен из всех переданных файлов
# для каждого переданного аргументом имени файла, вывести имена   extract_name
def main():
    for filename in get_filenames(sys.argv[1:]):
        man_dict, woman_dict = read_names_dict(read_data(filename))
        if man_dict is not None:
            print("Top 10 man names from (sorted by name) - ", filename)
            print_names(man_dict)
        if man_dict is not None:
            print("Top 10 woman names from (sorted by name) - ", filename)
            print_names(woman_dict)


if __name__ == '__main__':
    main()
