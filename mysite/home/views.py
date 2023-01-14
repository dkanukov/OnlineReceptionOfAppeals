from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.utils import IntegrityError
from . serializers import FeedbackSerializer, AppealSerializer

from . models import (
    News, Programs,
    AboutInfo, Report,
    Feedback, Document, Appeal
)


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
    latest_news = News.objects.order_by('-id')[3:]
    temp = loader.get_template('home/news.html')
    return HttpResponse(temp.render({'info': info, 'latest_news': latest_news}))


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
    documents = Document.objects.all()
    report_names = [report.file.name for report in reports]
    report_urls = [report.file.url for report in reports]
    document_names = [document.file.name for document in documents]
    document_urls= [document.file.url for document in documents]

    for index, report_name in enumerate(report_names):
        report_name = report_name.replace('reports/', '')
        report_name = report_name.replace('_', ' ')
        report_name = report_name.replace('.pdf', '')
        report_names[index] = report_name
    report_files = zip(report_names, report_urls)

    for index, document_name in enumerate(document_names):
        document_name = document_name.replace('documents/', '')
        document_name = document_name.replace('_', ' ')
        document_name = document_name.replace('.pdf', '')
        document_names[index] = document_name
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
    temp = loader.get_template(('home/personalDataValidation.html'))
    return HttpResponse(temp.render())


class APIFeedback(APIView):

    def post(self, request):
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

    def get(self, request):
        if request.user.is_authenticated:
            object_list = Appeal.objects.all()
            serializer = AppealSerializer(instance=object_list, many=True)
            return Response(serializer.data)
        else:
            return Response("not authentificated user", status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        serializer = AppealSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response("wrong type/option data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIAppealDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, id):
            appeal = get_object_or_404(Appeal, id=id)
            appeal.status = request.data['status']
            appeal.notes = request.data['notes']
            try:
                appeal.save()
                return Response("status changed", status=status.HTTP_205_RESET_CONTENT)
            except IntegrityError:
                return Response("wrong status value", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        appeal = get_object_or_404(Appeal, id=id)
        appeal.delete()
        return Response('object deleted', status=status.HTTP_204_NO_CONTENT)


'''
@api_view(['GET', 'PATCH'])
def appeal_api(request):
    print(request.user)
    print(request.user.has_perm('home.change_appeal'))
    print(request.user.is_authenticated)
    print(request.data)

    if request.method == 'GET':
        object_list = Appeal.objects.all()
        serializer = AppealSerializer(instance=object_list, many=True)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        return Response("patch request", status=203)
'''


def get_voting_right_program_page(request):
    info = get_about_context()
    temp = loader.get_template("home/votingRightProgram.html")
    return HttpResponse(temp.render({'info': info}))

