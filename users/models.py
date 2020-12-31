from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(
        _('Username'),
        max_length=20,
        unique=True,
        help_text=_(
            'Required. 4 to 20 characters.Beginning with an alphabet. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[
            RegexValidator(
                regex='^[a-zA-Z][\w@+-.]{3,19}\Z',
                message='Invalid username. Must be 4 to 20 characters long, starting with an alphabet.\
                     Letters, digits and @/./+/-/_ only.'
            )
        ],
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
