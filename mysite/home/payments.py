import json
import uuid

from django.http import JsonResponse
from rest_framework.views import View
from rest_framework.response import Response
from yookassa import Configuration, Payment


class YooKassaPayment(View):
    def get(self, request):
        Configuration.account_id = '973050'
        Configuration.secret_key = 'test_5N4ujI7BMHe4YRnB3luyFvcnw1fl52fTYXXEp6lAMe0'
        value = request.GET.get('value')
        payment = Payment.create({
            "amount": {
                "value": value,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/"
            },
            "capture": True,
            "description": "Тестовый заказ"
        }, uuid.uuid4())
        response = {'redirect_url': payment.confirmation.confirmation_url}
        return JsonResponse(response)

