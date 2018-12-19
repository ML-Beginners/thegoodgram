from django.db import models
from .forms import NameForm
# Create your models here.


class Register(models.Model):
  #  details = NameForm.object
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length = 50)