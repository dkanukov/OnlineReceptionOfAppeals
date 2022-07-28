from django.urls import path
from . import views

urlpatterns = [
        path('news_list', views.get_news_page, name='news'),
        path('api/news', views.APINews.as_view())
    ]