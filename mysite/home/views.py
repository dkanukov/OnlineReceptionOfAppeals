from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from . serializers import FeedbackSerializer, AppealSerializer
    #PartnerSerializer
from . models import News, Programs, AboutInfo, Report, Feedback


def get_about_context():
    info = AboutInfo.objects.all()[0]
    return info


def get_news_page(request):
    info = get_about_context()
    news_list = News.objects.all()
    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/newsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator, 'info': info}))


def get_specific_news(request):
    info = get_about_context()
    temp = loader.get_template('home/news.html')
    return HttpResponse(temp.render({'info': info}))


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
    info = get_about_context()
    news_list = Programs.objects.all()
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/programsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator, 'info': info}))


def get_specific_program(request):
    info = get_about_context()
    temp = loader.get_template('home/program.html')
    return HttpResponse(temp.render({'info': info}))


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
    info = get_about_context()
    reports = Report.objects.all()
    feedbacks = Feedback.objects.all()
    temp = loader.get_template('home/about.html')
    return HttpResponse(temp.render({'info': info, 'reports': reports, 'feedbacks': feedbacks}))


def get_personal_data_consent(request):
    temp = loader.get_template(('home/personalDataValidation.html'))
    return HttpResponse(temp.render())



#class APIPartner(APIView):
#
#    def post(self, request):
#        serializer = PartnerSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIFeedback(APIView):

    def post(self, request):
        print(request.data)
        if request.data["rating"] not in [1, 2, 3, 4, 5]:
            return Response("wrong stars count", status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = FeedbackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_contacts_page(request):
    info = get_about_context()
    temp = loader.get_template("home/contacts.html")
    return HttpResponse(temp.render({'info': info}))


class APIAppeal(APIView):
    def post(self, request):
        if request.data["type"] not in ['1', '2', '3']:
            return Response("wrong type value", status=status.HTTP_400_BAD_REQUEST)
        elif request.data["option"] not in ['1', '2', '3']:
            return Response("wrong option value", status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = AppealSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def get_voting_right_ptogram_page(request):
    info = get_about_context()
    temp = loader.get_template("home/votingRightProgram.html")
    return HttpResponse(temp.render({'info': info}))

