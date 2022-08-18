from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
# Create your views here.
def welcome(request):
    return HttpResponse('Hello, There')

def home(request):
    # messages ={'msg_one': 'Hello', 'msg_two': 'World'}
    total_users = User.objects.count()
    users = User.objects.all()
    return render(request, 'home.html', {'total_users': total_users, 'users': users})