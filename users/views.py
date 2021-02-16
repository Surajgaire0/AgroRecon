from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import MinimumLengthValidator, NumericPasswordValidator, validate_password
from django.shortcuts import get_object_or_404

from rest_framework import generics, serializers, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .serializers import CustomUserCreateSerializer, CustomUserSerializer, PasswordChangeSerializer
from .validators import PasswordValidator


class CustomUserListView(generics.ListCreateAPIView):
    """
    APIView to list users and register new users
    """
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
    ordering_fields=('answer_count','comment_count','date_joined','question_count')
    search_fields=('first_name','last_name','username')

    def post(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            created_user = user_serializer.save()
            return Response({'message': 'user successfully created'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    """
    APIView to retrieve and update user details
    """
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, username=None):
        retrieved_user = get_object_or_404(get_user_model(), username=username)
        serializer_obj = self.serializer_class(retrieved_user,context={'request': request})
        return Response(serializer_obj.data, status=status.HTTP_200_OK)


class MeUserView(APIView):
    """
    APIView for logged in user.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_obj = self.serializer_class(instance,context={'request': request})
        return Response(serializer_obj.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_obj = self.serializer_class(
            instance, data=request.data, partial=True)
        if serializer_obj.is_valid():
            updated_user = serializer_obj.save()
            if updated_user:
                return Response(serializer_obj.data, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PasswordChangeView(APIView):
    """
    APIView to change password.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def put(self, request, *args, **kwargs):
        user_instance = request.user
        old_password = request.data.get('old_password', None)
        new_password = request.data.get('new_password', None)
        if old_password and new_password:
            if user_instance.check_password(old_password):
                validate_password(new_password, password_validators=[
                                  PasswordValidator()])
                user_instance.set_password(new_password)
                user_instance.save()
                return Response(
                    {'status': 'success', 'message': 'password successfully changed'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'status': 'error', 'message': 'old password not matched'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {'status': 'error',
                'message': 'Both old password and new password need to be given'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
