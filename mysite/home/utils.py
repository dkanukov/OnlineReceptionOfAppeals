# Вспомогательные функции
import datetime


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


def change_user_done_tasks_count(old_status, new_status, user):
    if old_status in ('new', 'work', 'done') and new_status == 'archive':
        user.profile.done_tasks_count += 1
    if old_status == 'archive' and new_status in ('new', 'work', 'done'):
        user.profile.done_tasks_count -= 1
    user.save()
    return


def change_appeal_complete_date(old_status, new_status, appeal):
    if old_status in ('new', 'work', 'done') and new_status == 'archive':
        appeal.completion_date = datetime.date.today()
    if old_status == 'archive' and new_status in ('new', 'work', 'done'):
        appeal.completion_date = None
    appeal.save()
    return
