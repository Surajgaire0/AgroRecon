from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, MinimumLengthValidator, NumericPasswordValidator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import CustomUser
from .serializers import CustomUserSerializer, PasswordChangeSerializer
from .utils import PasswordValidator

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

# TODO: isownerorreadonly 
class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    lookup_field='username'

    def get(self,request,username=None):
        retrieved_user=get_object_or_404(get_user_model(),username=username)
        serializer_class=CustomUserSerializer(retrieved_user)
        return Response(serializer_class.data,status=status.HTTP_200_OK)

    # def update(self,request,username=None,*args,**kwargs):
    #     print (request.data)
    #     data=request.data
    #     password=data.get('password',None)
    #     retrieved_user=get_object_or_404(get_user_model(),username=username)
    #     if password:
    #         if not retrieved_user.check_password(password):
    #             return Response({'message':'password is not matched'},status=status.HTTP_400_BAD_REQUEST)
    #     serializer_class=CustomUserSerializer(retrieved_user,data)
    #     if serializer_class.is_valid(raise_exception=True):
    #         serializer_class.save(partial=True)
    #         return Response(serializer_class.data,status=status.HTTP_200_OK)
    #     return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PasswordChangeSerializer

    def post(self,request,*args,**kwargs):
        user_instance=request.user
        old_password=request.data.get('old_password',None)
        new_password=request.data.get('new_password',None)
        if old_password and new_password:
            if user_instance.check_password(old_password):
                validate_password(new_password,password_validators=[PasswordValidator()])
                user_instance.set_password(new_password)
                user_instance.save()
                return Response({'status':'success','message':'password successfully changed'},status=status.HTTP_200_OK)
            else:
                return Response({'status':'error','message':'old password not matched'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'error','message':'Both old password and new password need to be given'},status=status.HTTP_400_BAD_REQUEST)