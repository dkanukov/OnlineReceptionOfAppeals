from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.utils import IntegrityError
from .serializers import FeedbackSerializer, AppealSerializer
from .utils import format_date, change_user_done_tasks_count, change_appeal_complete_date
import datetime

from .models import (
    News, Programs, Appeal, Profile
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
                if appeal.user:
                    change_user_done_tasks_count(
                        old_status=appeal.status,
                        new_status=request.data['status'],
                        user=appeal.user
                    )
                else:
                    pass
                change_appeal_complete_date(
                    old_status=appeal.status,
                    new_status=request.data['status'],
                    appeal=appeal
                )
                appeal.status = request.data['status']
            if 'notes' in request.data:
                appeal.notes = request.data['notes']
            if 'flag' in request.data:
                appeal.flag = request.data['flag']
            if 'user_id' in request.data:
                try:
                    appeal.user = User.objects.get(pk=request.data['user_id'])
                except User.DoesNotExist:
                    appeal.user = None
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
            user = request.user
            try:
                user_done_tasks_count = user.profile.done_tasks_count
            except Profile.DoesNotExist:
                user_done_tasks_count = None

            response_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.username,
                'tasks_count': user_done_tasks_count
            }
            return Response(data=response_data)
        else:
            return Response("not authentificated user", status=status.HTTP_403_FORBIDDEN)


class APIAllUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.exclude(username='admin')
        response_data = []
        for user in users:
            try:
                user_done_tasks_count = user.profile.done_tasks_count
            except Profile.DoesNotExist:
                user_done_tasks_count = None
            response_data.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.username,
                'tasks_count': user_done_tasks_count
            })
        return Response(data=response_data)


def get_statistics(queryset):
    response = {}
    total = queryset.count()
    response['total'] = total
    total_status = {}
    total_status['new'] = queryset.filter(status="new").count()
    total_status['work'] = queryset.filter(status="work").count()
    total_status['done'] = queryset.filter(status="done").count()
    total_status['archive'] = queryset.filter(status="archive").count()
    response['status'] = total_status
    total_type = {}
    total_type['1'] = queryset.filter(type=1).count()
    total_type['2'] = queryset.filter(type=2).count()
    total_type['3'] = queryset.filter(type=3).count()
    response['type'] = total_type
    total_option = {}
    total_option['1'] = queryset.filter(option=1).count()
    total_option['2'] = queryset.filter(option=2).count()
    total_option['3'] = queryset.filter(option=3).count()
    total_option['4'] = queryset.filter(option=4).count()
    total_option['5'] = queryset.filter(option=5).count()
    total_option['6'] = queryset.filter(option=6).count()
    total_option['7'] = queryset.filter(option=7).count()
    response['option'] = total_option
    return response


class APIStatistics(APIView):
    permission_classes = [AllowAny ]

    def get(self, request):
        response_data = {}
        appeals = Appeal.objects.all()
        response_data = get_statistics(appeals)
        return Response(data=response_data)


class APIUserStatistics(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.exclude(username="admin")
        appeals = Appeal.objects.all()
        response_data = {}
        for user in users:
            user_appeals = appeals.filter(user=user)
            response_data.setdefault(user.id)
            response_data[user.id] = user.profile.done_tasks_count

        return Response(data=response_data)


class APIStatisticsPerMonth(APIView):
    permission_classes = [AllowAny]

    def get(self, request, year, month):
        response_data = {}
        appeals = Appeal.objects.filter(
            create_date__year=year,
            create_date__month=month
        )

        response_data['1'] = appeals.filter(option=1).count()
        response_data['2'] = appeals.filter(option=2).count()
        response_data['3'] = appeals.filter(option=3).count()
        response_data['4'] = appeals.filter(option=4).count()
        response_data['5'] = appeals.filter(option=5).count()
        response_data['6'] = appeals.filter(option=6).count()
        response_data['7'] = appeals.filter(option=7).count()

        return Response(data=response_data)


class APIUserDoneTasksPerMonth(APIView):
    permission_classes = [AllowAny]

    def get(self, request, year, month):
        response_data = {}
        users = User.objects.exclude(username="admin")
        appeals = Appeal.objects.all()
        for user in users:
            user_month_done_tasks_count = appeals.filter(
                user=user,
                completion_date__year=year,
                completion_date__month=month
            ).count()
            response_data[user.id] = user_month_done_tasks_count

        return Response(data=response_data)
