# 1. 
# Вх: список чисел, Возвр: список чисел, где 
# повторяющиеся числа урезаны до одного 
# пример [0, 2, 2, 3] returns [0, 2, 3].


def adj_list(nums):
    li = list(set(nums))
    li.sort()
    return li


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список

def link_lists(nums_1, nums_2):
    res = nums_1
    for val in nums_2:
        res.append(val)
    res.sort()
    return res


def main():
    li_adj = adj_list([1, 2, 2, 6, 3, 1, 7, 7, 6, 5])
    li_link = link_lists([1, 1, 2, 6, 3, 7], [4, 1, 9, 3])
    print(li_adj, sep=', ')
    print(li_link, sep=', ')


if __name__ == '__main__':
    main()
