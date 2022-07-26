from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'year', 'course', 'section', 'password1', 'password2']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
