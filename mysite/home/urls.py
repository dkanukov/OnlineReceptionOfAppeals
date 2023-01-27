from django.urls import path
from . import views, api
from .payments import YooKassaPayment


urlpatterns = [
        path('news_list', views.get_news_page, name='news'),
        path('news', views.get_specific_news, name='get_spec_news'),
        path('programs_list', views.get_programs_page, name='programs'),
        path('program', views.get_specific_program, name='get_spec_prog'),
        path('about', views.get_about_page, name='about'),
        path('personal_data', views.get_personal_data_consent, name='pers_data'),
        path('contacts', views.get_contacts_page, name='contacts'),
        path('voting_right', views.get_voting_right_program_page, name='voting_right'),

        path('api/news', api.APINews.as_view()),
        path('api/programs', api.APIPrograms.as_view()),
        path('api/feedback', api.APIFeedback.as_view()),
        path('api/appeal', api.APIAppeal.as_view()),
        path('api/appeal/<int:id>', api.APIAppealDetail.as_view()),
        path('api/pay', YooKassaPayment.as_view(), name='payment'),
        path('api/user', api.APIUser.as_view()),
        path('api/all-users', api.APIAllUsers.as_view())
    ]

