def count_equal_pairs(lst):
    """
    Подсчитывает количество пар элементов в lst, которые равны друг другу.
    """
    count = 0

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1

    return count
