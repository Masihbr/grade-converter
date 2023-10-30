from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    student_id = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{8,9}$')])
    is_verified = models.BooleanField(default=False)
