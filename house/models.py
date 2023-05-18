from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True)
    area = models.TextField(blank=True)
    height = models.TextField(blank=True)
    roof = models.TextField(blank=True)
    floors = models.TextField(blank=True)
    dimensions = models.TextField(blank=True)
    ceiling_height = models.TextField(blank=True)
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    price = models.IntegerField(blank=False)
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты компании'
        ordering = ['name']


class Type(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})

    class Meta:
        verbose_name = 'Типы книг'
        verbose_name_plural = 'Список типов'
        ordering = ['name']


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    contacts = models.TextField(blank=True)
    number = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Status(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a status")

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    file1 = models.FileField(upload_to='files')
    file2 = models.FileField(upload_to='files')
    file3 = models.FileField(upload_to='files')
    file4 = models.FileField(upload_to='files')
    file5 = models.FileField(upload_to='files')

    def __str__(self):
        return self.user
