from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            user = User.objects.get(username=username)
        except:
            print(request, 'User does not exist')

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Username OR password does not exit')

    return render(request, 'login.html')


def registerUser(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
        else:
            print(request, 'An error occurred during registration')

    return render(request, 'register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


def homePage(request):
    topics = Topic.objects.all()
    classmates = User.objects.all()

    context = {
        'topics': topics,
        'classmates': classmates,
    }
    return render(request, 'home.html', context)


def topic(request, pk):
    get_topic = Topic.objects.get(id=pk)
    topics = Topic.objects.all()
    topic_messages = get_topic.message_set.all()
    classmates = User.objects.all()

    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            topic=get_topic,
            body=request.POST.get('body')
        )
        return redirect('topic', pk=get_topic.id)

    context = {
        'topics': topics,
        'topic_messages': topic_messages,
        'classmates': classmates,
    }

    return render(request, 'home.html', context)


def createTopic(request):
    form = TopicForm()
    if request.method == 'POST':
        Topic.objects.create(
            host=request.user,
            year=request.user.year,
            course=request.user.course,
            section=request.user.section,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'create-topic.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)

    context = {
        'user': user
    }
    return render(request, 'profile.html', context)
