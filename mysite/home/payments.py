import uuid

from django.http import HttpResponseRedirect
from rest_framework.views import View
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

        return HttpResponseRedirect(payment.confirmation.confirmation_url)

