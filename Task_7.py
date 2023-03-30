def find_f_indexes(s):
    """
    Находит индекс(ы) буквы 'f' в строке s.
    Если буква 'f' встречается только один раз, возвращается ее индекс.
    Если 'f' встречается два или более раз, возвращается индекс ее первого и последнего появления.
    Если 'f' не встречается в строке, возвращается None.
    """
    first_index = s.find('f')
    last_index = s.rfind('f')

    if first_index == -1:
        return None

    if first_index == last_index:
        return first_index
    else:
        return (first_index, last_index)