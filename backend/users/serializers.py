from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser
from .utils import PasswordValidator
from forum.serializers import QuestionSerializer, AnswerSerializer, CommentSerializer
from forum.models import Question, Answer, Comment

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields=('id','username','first_name','last_name','email','address','profile_picture','question_count','question_set','answer_count','answer_set','comment_count','comment_set')
        lookup_field='username'


class CustomUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields=('id','username','password','first_name','last_name','email','address','profile_picture','question_count','answer_count','comment_count')
        extra_kwargs={'password':{'write_only':True}}

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