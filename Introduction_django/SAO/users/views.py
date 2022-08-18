from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
# Create your views here.
from users.models import User

def detail(request, id):
    # user = User.objects.get(id=id)
    user = get_object_or_404(User, id=id)
    return render(request, 'details.html', {'user': user})

UserForm = modelform_factory(User, fields=['first_name', 'last_name', 'email', 'delivery'])

def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'newuser.html', {'form': form})
    else:
        form = UserForm()  
    return render(request, 'newuser.html', {'form': form})

def editUser(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'edituser.html', {'form': form, 'user': user})
    else:
        form = UserForm(instance=user)
    return render(request, 'edituser.html', {'form': form, 'user': user})

def deleteUser(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('home')