def porridge_schedule(n):
    """
    Напишите программу, которая строит расписание каш на ближайшие дни.
    """
    porridges = ['Manna', 'Buckwheat', 'Millet', 'Oatmeal', 'Rice']
    schedule = []

    #   генерирует расписание каш на определенное количество дней,
    #   где каши чередуются в фиксированном циклическом порядке.
    for i in range(n):
        porridge_index = i % len(porridges)
        schedule.append(porridges[porridge_index])

    return schedule