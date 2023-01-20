from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader

from . models import (
    News, Programs,
    AboutInfo, Report,
    Feedback, Document
)


def get_about_context():
    """Получить контекст для футера/хедера"""
    info = AboutInfo.objects.first()
    return info


def get_news_page(request):
    """Предоставить страницу новостей"""
    print(request.user)
    info = get_about_context()
    news_list = News.objects.all()
    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/newsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator, 'info': info}))


def get_specific_news(request):
    """Предоставить подробную страницу новости"""
    id = request.GET.get('id')
    info = get_about_context()
    latest_news = News.objects.exclude(id=id).order_by('-id')[:3]
    temp = loader.get_template('home/news.html')
    return HttpResponse(temp.render({'info': info, 'latest_news': latest_news}))


def get_programs_page(request):
    """Предоставить страницу программ фонда"""
    info = get_about_context()
    news_list = Programs.objects.all()
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/programsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator, 'info': info}))


def get_specific_program(request):
    """Предоставить подробную страницу программы фонда"""
    info = get_about_context()
    temp = loader.get_template('home/program.html')
    return HttpResponse(temp.render({'info': info}))


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
    name = name.replace('reposrt/', '')
    name = name.replace('_', ' ')
    name = name.replace('.pdf', '')
    return name


def get_about_page(request):
    """Представление страницы О Фонде"""
    info = get_about_context()
    reports = Report.objects.all()
    documents = Document.objects.all()
    report_names = [report.file.name for report in reports]
    report_urls = [report.file.url for report in reports]
    document_names = [document.file.name for document in documents]
    document_urls = [document.file.url for document in documents]

    for index, report_name in enumerate(report_names):
        report_names[index] = format_file_name(report_name)
    report_files = zip(report_names, report_urls)

    for index, document_name in enumerate(document_names):
        document_names[index] = format_file_name(document_name)
    document_files = zip(document_names, document_urls)

    feedbacks = Feedback.objects.filter(is_published=True)
    temp = loader.get_template('home/about.html')
    return HttpResponse(temp.render({
        'info': info,
        'reports': report_files,
        'documents': document_files,
        'feedbacks': feedbacks,
    }))


def get_personal_data_consent(request):
    """Представление страницы соглашения"""
    temp = loader.get_template(('home/personalDataValidation.html'))
    return HttpResponse(temp.render())


def get_contacts_page(request):
    """"Представление страницы Контакты"""
    info = get_about_context()
    temp = loader.get_template("home/contacts.html")
    return HttpResponse(temp.render({'info': info}))


def get_voting_right_program_page(request):
    """Представление страницы программы Право Голоса"""
    info = get_about_context()
    temp = loader.get_template("home/votingRightProgram.html")
    return HttpResponse(temp.render({'info': info}))

