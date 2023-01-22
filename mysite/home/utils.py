# Вспомогательные функции


def format_date(date):
    """Форматирование даты"""
    month_dct = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
                 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
                 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

    year, month, day = date.year, date.month, date.day
    return ' '.join(list(map(str, [day, month_dct[month], year])))


def format_file_name(name):
    """Форматирование имени файла"""
    name = name.replace('documents/', '')
    name = name.replace('reports/', '')
    name = name.replace('_', ' ')
    name = name.replace('.pdf', '')
    return name