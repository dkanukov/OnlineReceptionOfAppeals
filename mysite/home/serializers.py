from .models import News
from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    caption = serializers.CharField()
    text_before_photo = serializers.CharField()
    image = serializers.ImageField(use_url=True)
    text_after_photo = serializers.CharField()
    additional_images = serializers.ListField(
        child=serializers.ImageField(use_url=True)
    )

