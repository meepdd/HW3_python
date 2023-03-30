def can_eat(knight_pos, piece_pos):
    """
    Возвращает True, если конь может съесть фигуру, False в противном случае.
    """
    # Вычислите абсолютную разницу между координатами x и y двух отрезков
    x_diff = abs(knight_pos[0] - piece_pos[0])
    y_diff = abs(knight_pos[1] - piece_pos[1])

    # Проверка, удовлетворяет ли абсолютная разница шаблону хода коня.
    if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
        return True
    else:
        return False