from distutils.command.upload import upload
import email
from email.mime import image
from email.quoprimime import body_check
from importlib.resources import contents
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS= (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )


    category = models.ForeignKey(Category, related_name='posts' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000)
    image= models.ImageField(upload_to = 'images/',blank=True, null= True)
    intro = models.CharField(max_length=1000)
    content = models.CharField(max_length=100000)
    body = models.CharField(max_length=100000)
    create_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
