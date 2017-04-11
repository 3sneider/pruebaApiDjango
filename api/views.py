from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import message, image
from .serializers import messageSerializer, imageSerializer

# Create your views here.


class messageList(APIView):

    def get(self, request):
        messages = message.objects.all()
        serializer = messageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = messageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class imageList(APIView):

    def get(self, request):
        images = image.objects.all()
        serializer = imageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = imageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
