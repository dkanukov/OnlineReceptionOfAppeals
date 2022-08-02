from django.urls import path
from . import views

urlpatterns = [
        path('news_list', views.get_news_page, name='news'),
        path('api/news', views.APINews.as_view()),
        path('news', views.get_specific_news, name='get_spec_news'),
        path('programs_list', views.get_programs_page, name='programs'),
        path('api/programs', views.APIPrograms.as_view()),
        path('program', views.get_specific_program, name='get_spec_prog')
    ]