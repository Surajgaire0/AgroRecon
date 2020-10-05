from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.
class CustomUserListView(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    parser_classes=[MultiPartParser,FormParser]

    def post(self,request):
        user_serializer=CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            created_user=user_serializer.save()
            return Response({'message':'user successfully created'},status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    lookup_field='username'

    def get(self,request,username=None):
        retrieved_user=get_object_or_404(get_user_model(),username=username)
        serializer_class=CustomUserSerializer(retrieved_user)
        return Response(serializer_class.data,status=status.HTTP_200_OK)