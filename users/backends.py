from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class CustomUserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = get_user_model().objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password) is True:
                return user
        except get_user_model().DoesNotExist:
            pass
