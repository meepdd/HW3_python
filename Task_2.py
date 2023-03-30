def morse_tue_sequence(n):
    """
     Генерирует первые n цифр последовательности Морзе-Туэ.
    """
    # Инициализируем последовательность первыми двумя цифрами
    seq = "01"

    # Генерируем остальные цифры, используя предыдущие цифры
    for i in range(2, n):
        # Получаем предыдущую цифру и ее количество
        prev_digit = seq[i - 1]
        count = 1
        while i - count >= 0 and seq[i - count] == prev_digit:
            count += 1

        # Добавляем следующую цифру, основываясь на количестве предыдущих цифр
        next_digit = "0" if prev_digit == "1" else "1"
        for j in range(count):
            seq += next_digit

    # Возвращаем первые n цифр последовательности
    return seq[:n]