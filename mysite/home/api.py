from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.utils import IntegrityError
from .serializers import FeedbackSerializer, AppealSerializer
from .utils import format_date

from .models import (
    News, Programs, Appeal
)


class APINews(APIView):
    """Предоставление новости по id"""
    def get(self, request):
        id = request.GET.get('id')
        try:
            obj = get_object_or_404(News, id=int(id))
            additional_photos = []
            for block_photo in obj.additional_images:
                additional_photos.append(block_photo._as_tuple()[1].file.url)
            return Response({
                'caption': obj.caption,
                'date': format_date(obj.create_date),
                'textBeforePhoto': obj.text_before_photo,
                'imageUrl': obj.image.file.url,
                'textAfterPhoto': obj.text_after_photo,
                'additionalPhotos': additional_photos
            })
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class APIPrograms(APIView):
    """Предоставление программы по id"""
    def get(self, request):
        id = request.GET.get('id')
        obj = get_object_or_404(Programs, id = int(id))
        try:
            return Response({
                'title': obj.title,
                 'caption': obj.caption,
                 'description': obj.description,
                 'date': format_date(obj.create_date),
                'imageUrl': obj.image.file.url
            })
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class APIFeedback(APIView):
    """Прием пользовательских отзывов"""
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


class APIAppeal(APIView):
    """Преим и предоставление обращений"""
    permission_classes = [AllowAny]

    def get(self, request):
        print(request.COOKIES)
        if request.user.is_authenticated:
            object_list = Appeal.objects.all()
            serializer = AppealSerializer(instance=object_list, many=True)
            return Response(serializer.data)
        else:
            return Response("not authentificated user", status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        print(request.data)
        serializer = AppealSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                print("ошибка записи")
                return Response("wrong type/option data", status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIAppealDetail(APIView):
    """Изменение и удаления обращения по id"""
    permission_classes = [IsAuthenticated]

    def patch(self, request, id):
            appeal = get_object_or_404(Appeal, id=id)
            if 'status' in request.data:
                appeal.status = request.data['status']
            if 'notes' in request.data:
                appeal.notes = request.data['notes']
            if 'flag' in request.data:
                print(request.data)
                print(type(request.data['flag']))
                print(request.data['flag'])
                appeal.flag = request.data['flag']
            try:
                appeal.save()
                return Response("updated", status=status.HTTP_205_RESET_CONTENT)
            except IntegrityError:
                return Response("wrong status value", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        appeal = get_object_or_404(Appeal, id=id)
        appeal.delete()
        return Response('object deleted', status=status.HTTP_204_NO_CONTENT)


class APIUser(APIView):
    """Предоставление ФИ сотрудника-пользователя"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            response_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
            return Response(data=response_data)
        else:
            return Response("not authentificated user", status=status.HTTP_403_FORBIDDEN)
