from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=300)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='media')
    video = models.FileField(
        default='',
        upload_to='media')
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    #image = models.FilePathField(path="/projects/images/portfolio")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
