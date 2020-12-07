from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Resume(models.Model):
    cvupload = models.FileField(default='', upload_to='media')
    title = models.CharField(max_length=50)


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    #description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(
        default='',
        blank='False',
        upload_to='media')
    #video = models.FileField(
     #   default='',
     #   upload_to='media')
    adminupload = models.FileField(default='',             upload_to='media')

    #image = models.FilePathField(path="/projects/images/portfolio")
