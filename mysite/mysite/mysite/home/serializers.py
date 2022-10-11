from .models import Feedback, Appeal
#Partner
from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    caption = serializers.CharField()
    text_before_photo = serializers.CharField()
    image = serializers.ImageField(use_url=True)
    text_after_photo = serializers.CharField()
    additional_images = serializers.ListField(
        child=serializers.ImageField(use_url=True)
    )


#class PartnerSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=50)
#    last_name = serializers.CharField(max_length=50)
#    phone_number = serializers.CharField(max_length=20)
#   email = serializers.EmailField()
#   message = serializers.CharField(max_length=1000)
#    is_agree = serializers.BooleanField(default=False)
#
#    def create(self, validated_data):
#       return Partner.objects.create(**validated_data)


class FeedbackSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=1000)
    rating = serializers.IntegerField(default=5)

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)


class AppealSerializer(serializers.Serializer):

    type = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=20)
    option = serializers.IntegerField()

    def create(self, validated_data):
        return Appeal.objects.create(**validated_data)
''' прописать все поля и метод create, в апиview прописать метод пост, is_valid(), save() '''
