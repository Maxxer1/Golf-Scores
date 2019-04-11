from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login
from commons.success_messages import SuccessMessage
from commons.error_messages import ErrorMessage
from django.core.exceptions import ObjectDoesNotExist

def signup(request):
    if request.method == 'POST':
        form = request.POST
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
                return redirect('/index')
            else:
                return render(request, 'signin.html', {'error_message': ErrorMessage.USERNAME_OR_PASSWORD_INCORRECT.value})
        except ObjectDoesNotExist:
            return render(request, 'signin.html', {'error_message': ErrorMessage.USERNAME_OR_PASSWORD_INCORRECT.value})
    return render(request, 'signin.html')
