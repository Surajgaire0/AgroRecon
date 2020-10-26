from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser
from .utils import PasswordValidator

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields=('id','username','password','first_name','last_name','email','address','profile_picture')
        extra_kwargs={'password':{'write_only':True}}
        lookup_field='username'

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            validate_password(password,password_validators=[PasswordValidator()])
            instance.set_password(password)
        instance.save()
        return instance


class PasswordChangeSerializer(serializers.Serializer):
    old_password=serializers.CharField(max_length=20)
    new_password=serializers.CharField(max_length=20)