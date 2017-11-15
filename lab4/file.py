"""
    Прочитать из файла (имя - параметр командной строки)
    все слова (разделитель пробел)

    Создать "Похожий" словарь который отображает каждое слово из файла
    на список всех слов, которые следуют за ним (все варианты).

    Список слов может быть в любом порядке и включать повторения.
    например "and" ['best", "then", "after", "then", ...]

    Считаем , что пустая строка предшествует всем словам в файле.

    С помощью "Похожего" словаря сгенерировать новый текст
    похожий на оригинал.
    Т.е. напечатать слово - посмотреть какое может быть следующим
    и выбрать случайное.

    В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
    (для первой вход.парам. - файл)

    Файл:
    He is not what he should be
    He is not what he need to be
    But at least he is not what he used to be
      (c) Team Coach


"""

import codecs
import random
import re
import sys


def to_filename(filename):
    if filename is not None and filename != "":
        return filename
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


def mem_dict(file_data):
    word_dict = dict()
    for newline in re.compile('\n').split(file_data):
        prev_word = None
        for word in re.compile(' +').split(newline):
            # Update prev word
            if prev_word is not None:
                prev_words_associated = word_dict.get(prev_word)
                prev_words_associated.append(word)
                word_dict.update({prev_word: prev_words_associated})

            # Update current word
            words_associated = word_dict.get(word)
            if words_associated is None:
                words_associated = list()
            if prev_word is not None:
                words_associated.append(prev_word)
            prev_word = word
            word_dict.update({word: words_associated})

    return word_dict


def print_phrase(phrase):
    result = ""
    for w in phrase:
        result += w + " "
    print(result)


def main():
    files = get_filenames(sys.argv[1:])
    for file in files:
        words_dict = mem_dict(read_data(file))
        keys = list(words_dict.keys())
        first_word = keys[random.randint(0, len(keys) - 1)]
        phrase = list()
        phrase.append(first_word)
        words_associated = words_dict.get(first_word)

        for i in range(10):
            next_word = words_associated[random.randint(0, len(words_associated) - 1)]
            words_associated = words_dict.get(next_word)
            if words_associated is None:
                break
            phrase.append(next_word)

        print_phrase(phrase)


if __name__ == '__main__':
    main()
