from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Year(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)


class Topic(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    classmates = models.ForeignKey(User, related_name='classmates', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    body = models.TextField()

    def __str__(self):
        return self.body
