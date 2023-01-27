from .models import Feedback, Appeal
from rest_framework import serializers


class FeedbackSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=1000)
    rating = serializers.IntegerField(default=5)

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)


class AppealSerializer(serializers.ModelSerializer):
    '''
    id = serializers.IntegerField(read_only=True)
    type = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=20)
    option = serializers.IntegerField()
    status = serializers.CharField(default='new')
    notes = serializers.CharField(max_length=255, read_only=True)
    flag = serializers.BooleanField(read_only=True)
    user = serializers.CharField(read_only=True)
    '''
    create_date = serializers.DateField(read_only=True, format='%d-%m-%Y')

    class Meta:
        model = Appeal
        fields = [
            'id', 'type', 'name', 'last_name',
            'phone_number', 'option', 'status',
            'create_date', 'notes', 'flag', 'user'
        ]
        read_only_fields = [
            'id', 'create_date', 'notes', 'flag', 'user'
        ]

    def create(self, validated_data):
        return Appeal.objects.create(**validated_data)