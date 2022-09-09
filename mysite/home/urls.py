from django.urls import path
from . import views

urlpatterns = [
        path('news_list', views.get_news_page, name='news'),
        path('api/news', views.APINews.as_view()),
        path('news', views.get_specific_news, name='get_spec_news'),
        path('programs_list', views.get_programs_page, name='programs'),
        path('api/programs', views.APIPrograms.as_view()),
        path('program', views.get_specific_program, name='get_spec_prog'),
        path('about', views.get_about_page, name='about'),
        path('personal_data', views.get_personal_data_consent, name='pers_data'),
        #path('api/partner', views.APIPartner.as_view()),
        path('api/feedback', views.APIFeedback.as_view()),
        path('contacts', views.get_contacts_page, name='contacts'),
        path('api/appeal', views.APIAppeal.as_view()),
        path('voting_right', views.get_voting_right_ptogram_page, name='voting_right')
    ]
