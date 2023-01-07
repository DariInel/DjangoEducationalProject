from django.db import models


# Create your models here.
class Profession(models.Model):
    name = models.CharField('Название', max_length=40)
    description = models.TextField('Описание')
