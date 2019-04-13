from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from commons.success_messages import SuccessMessage
from commons.error_messages import ErrorMessage
from django.core.exceptions import ObjectDoesNotExist

def signup(request):
    if request.method == 'POST':
        form = request.POST
        if User.objects.filter(username=form.__getitem__('username')).exists():
            return render(request, 'signup.html', {'error_message': ErrorMessage.USERNAME_ALREADY_EXISTS.value})
        if User.objects.filter(email=form.__getitem__('email')).exists():
            return render(request, 'signup.html', {'error_message': ErrorMessage.EMAIL_ALREADY_EXISTS.value})
        if form.__getitem__('password') != form.__getitem__('confirm_password'):
            return render(request, 'signup.html', {'error_message': ErrorMessage.PASSWORDS_DONT_MATCH.value})
        user = User.objects.create_user(form.__getitem__(
            'username'), form.__getitem__('email'), form.__getitem__('password'))
        user.save()
        return render(request, 'signup.html', {'success_message': SuccessMessage.ACCOUNT_CREATED.value})
    if request.method == 'GET':
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        form = request.POST
        try:
            user = User.objects.get(username=form.__getitem__('username'))
            if user is not None and user.check_password(form.__getitem__('password')):
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'signin.html', {'error_message': ErrorMessage.USERNAME_OR_PASSWORD_INCORRECT.value})
        except ObjectDoesNotExist:
            return render(request, 'signin.html', {'error_message': ErrorMessage.USERNAME_OR_PASSWORD_INCORRECT.value})
    return render(request, 'signin.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def account_management(request):
    return render(request, 'account_management.html')

def change_password(request):
    return