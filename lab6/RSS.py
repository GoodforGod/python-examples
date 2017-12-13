"""
Простой RSS reader 

При добавлении ленты (например https://habrahabr.ru/rss/interesting/) 
записи из добавленной ленты сканируются и заносятся в базу (например sqlite)

При нажатии на кнопку обновить - новое сканирование и добавление новых записей (без дублрования существующих)

Отображение ленты начиная с самых свежих записей с пагинацией (несколько записей на странице)

Записи из разных лент хранить и показывать отдельно (по названию ленты).

Продублировать отчет (исходник) на xms@npp-itb.spb.ru
"""

import hashlib
import re

import feedparser

""" RSS links, { ID : URL }  """
feeds = dict()

""" RSS feed content, { ID : list({RSS_ITEM}, {RSS_ITEM}) }  """
feed_items = dict()


def build_feed_id(feed):
    if feed is None:
        return None

    feed_title = feed["channel"]["title"].encode('utf-8')
    feed_url = feed["url"].encode('utf-8')
    feed_descr = feed["channel"]["description"].encode('utf-8')
    feed_link = feed["channel"]["link"].encode('utf-8')

    return hashlib.sha1(feed_title + feed_url + feed_descr + feed_link)


def build_item_id(item):
    if item is None:
        return None

    item_pub = item["published_parsed"].encode('utf-8')
    item_title = item["title"].encode('utf-8')
    item_link = item["link"].encode('utf-8')

    return hashlib.sha1(item_pub + item_title + item_link)


def store_feed(feed):
    if feed is None:
        return None

    feed_id = build_feed_id(feed)
    if feed_id is None:
        return None

    feed_prev = feeds.get(feed_id)
    if feed_prev is not None:
        return feed_id, feed_prev

    feeds.update({feed_id: feed})
    store_items(feed_id, feed["items"])
    return feed_id, feed


def store_items(feed_id, items):
    if feed_id is None or items is None:
        return None

    items_dict = feed_items.get(feed_id)
    if items_dict is None:
        items_dict = dict()

    for item in items:
        item_id = build_item_id(item)
        item_from_dict = items_dict.get(item_id)
        if item_from_dict is None:
            items_dict.update({item_id: item})

    feed_items.update({feed_id: items_dict})
    return items


def get_sorted_items(feed_id):
    items_dict = feed_items.get(feed_id)
    if items_dict is None:
        return None

    items_to_sort = items_dict.values()
    items_sorted = sorted(items_to_sort, key=lambda entry: entry["published_parsed"])
    items_sorted.reverse()
    return items_sorted


def is_url_valid(url):
    return url is not None and re.match("http[s]://.*", url)


def save_feed(url):
    if url is None or not is_url_valid(url):
        return None

    feed = feedparser.parse(url)
    if feed is not None:
        return store_feed(feed)
    return None


def refresh():
    feeds_res = dict()
    for feed_id, feed_url in feeds:
        feed_id, feed = save_feed(feed_url)
        if feed is None:
            continue

        feeds_res.update({feed_id: feed})
    return feeds_res


def main():
    link = "https://habrahabr.ru/rss/interesting/"
    feed_id, feed = save_feed(link)
    print(feed)
    return None


if __name__ == '__main__':
    main()
