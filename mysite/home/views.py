from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsSerializer
from . models import News


def get_news_page(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    temp = loader.get_template('home/newsList.html')
    return HttpResponse(temp.render({'page_obj': page_obj, 'paginator': paginator}))


class APINews(APIView):
    def post(self, request):
        obj = News.objects.get(id=int(request.data['id']))
        additional_photos = []
        for block_photo in obj.additional_images:
            additional_photos.append(block_photo._as_tuple()[1].file.url)
        return Response({'caption': obj.caption,
                         'date': obj.create_date,
                         'text_before_photo': obj.text_before_photo,
                         'image_url': obj.image.file.url,
                         'text_after_photo': obj.text_after_photo,
                         'additional_photos': additional_photos})





