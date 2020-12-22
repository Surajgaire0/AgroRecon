from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(
        _('Username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator,
                    RegexValidator(regex='^[a-zA-Z]+.*', message='Username should begin with alphabet.')],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('Email'),
        unique=True)
    address = models.CharField(
        _('Address'),
        max_length=127,
        null=True,
        blank=True)
    profile_picture = models.ImageField(
        _('Profile Picture'),
        default='defaultusers.png',
        upload_to='profile',
        blank=True)

    @property
    def question_count(self):
        return self.question_set.count()

    @property
    def answer_count(self):
        return self.answer_set.count()

    @property
    def comment_count(self):
        return self.comment_set.count()
