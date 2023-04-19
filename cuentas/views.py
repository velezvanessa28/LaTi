from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.

'''Accounts'''
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login')
            
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')

def logoutaccount(request):
    logout(request)
    return redirect('home')
'''Accounts'''