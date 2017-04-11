from rest_framework.serializers import ModelSerializer
from .models import message, image


class messageSerializer(ModelSerializer):

    class Meta:
        model = message
        fields = '__all__'


class imageSerializer(ModelSerializer):

    class Meta:
        model = image
        fields = '__all__'

