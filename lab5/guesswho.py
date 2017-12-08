
"""
Вход: файл guess.txt содержащий имена для угадывания 

(например из http://www.biographyonline.net/people/famous-100.html можно взять имена)


Написать игру "Угадай по фото"

3 уровня сложности:
1) используются имена только 1-10
2) имена 1-50
3) имена 1-100

- из используемых имен случайно выбрать одно
- запустить поиск картинок в Google по выбранному
- получить ~30-50 первых ссылок на найденные по имени изображения
- выбрать случайно картинку и показать ее пользователю для угадывания
  (можно выбрать из выпадающего списка вариантов имен)
- после выбора сказать Правильно или Нет

п.с. желательно делать серверную часть, т.е. клиент играет в обычном браузере обращаясь к веб-серверу.

п.с. для поиска картинок желательно эмулировать обычный пользовательский запрос к Google
т.е. можно использовать и Google image search API
https://ajax.googleapis.com/ajax/services/search/images? или др. варианты
НО в таком случае нужно предусмотреть существующие ограничения по кол-ву запросов
т.е. кешировать информацию на случай исчерпания кол-ва разрешенных (бесплатных)
запросов или другим образом обходить ограничение.
Т.е. игра не должна прерываться после N запросов (ограничение API)


п.с. желательно "сбалансировать" параметры поиска (например искать только лица, 
использовать только первые 1-30 найденных и т.п.)
для минимизации того что найденная картинка не соответствует имени

p.s. Отчеты также высылать на xms@npp.itb.spb.ru
"""


import codecs
import random
import re
import sys
from urllib.request import Request, urlopen, quote


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


def build_google_url(name):
    if names is None:
        return None
    return "https://www.google.ru/search?dcr=0&source=lnms&tbm=isch&sa=X&q=" + quote(name)


def extract_page_data(link):
    if link is None:
        return None

    q = Request(link)
    q.add_header('User-Agent', 'Mozilla/5.0')
    page_bytes = urlopen(q).read()
    page_utf = page_bytes.decode("utf8")

    return page_utf


def extract_pic_link(page_data, limit):
    if page_data is None:
        return None

    matches = list(re.finditer("<img *height=\"[0-9]*\" *src=\"https://encrypted-tbn0.gstatic.com/images[^>]*\">", page_data))

    filter_limit = limit
    if filter_limit is None or filter_limit > len(matches):
        filter_limit = len(matches)

    match = matches[random.randint(0, filter_limit)]
    link = re.search("\"https://encrypted-tbn0.gstatic.com/images[^\"]*\"", match.group())
    if link is None:
        return None

    return link.group()[1:-1]


def setup():
    files = get_file_names(["words"])
    for file in files:
        names_dict = build_name_dict(read_data(file))
        if names_dict is not None:
            i = len(names)
            for num, name in names_dict.items():
                i += 1
                names.update({i: name})
    print(names)
    rand_num = random.randint(0, len(names) - 1)
    rand_name = names.get(rand_num)
    google_url = build_google_url(rand_name)
    page_data = extract_page_data(google_url)
    link = extract_pic_link(page_data, 10)
    print(rand_name)
    print(link)


def main():
    setup()


if __name__ == '__main__':
    main()
