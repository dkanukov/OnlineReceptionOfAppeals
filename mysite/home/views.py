from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView

from . models import News, Programs, AboutInfo


def get_news_page(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/newsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator}))


def get_specific_news(request):
    temp = loader.get_template('home/news.html')
    return HttpResponse(temp.render())


class APINews(APIView):
    def get(self, request):
        obj = News.objects.get(id=int(request.GET.get('id')))
        additional_photos = []
        for block_photo in obj.additional_images:
            additional_photos.append(block_photo._as_tuple()[1].file.url)
        return Response({'caption': obj.caption,
                         'date': format_date(obj.create_date),
                         'textBeforePhoto': obj.text_before_photo,
                         'imageUrl': obj.image.file.url,
                         'textAfterPhoto': obj.text_after_photo,
                         'additionalPhotos': additional_photos})


def get_programs_page(request):
    news_list = Programs.objects.all()
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/programsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator}))


def get_specific_program(request):
    temp = loader.get_template('home/program.html')
    return HttpResponse(temp.render())


class APIPrograms(APIView):
    def get(self, request):
        obj = Programs.objects.get(id=int(request.GET.get('id')))
        return Response({'title': obj.title,
                         'caption': obj.caption,
                         'description': obj.description,
                         'date': format_date(obj.create_date),
                         'imageUrl': obj.image.file.url
                         })


def format_date(date):
    month_dct = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
                 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
                 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

    year, month, day = date.year, date.month, date.day
    return ' '.join(list(map(str, [day, month_dct[month], year])))


def get_about_page(request):
    info = AboutInfo.objects.all()[0]

    temp = loader.get_template('home/about.html')
    return HttpResponse(temp.render({'information': info.information,
                                     'phone_number': info.phone_number,
                                     'second_phone_number': info.second_phone_number,
                                     'email': info.email,
                                     'address': info.address}))
