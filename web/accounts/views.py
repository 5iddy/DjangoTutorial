from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from .models import Account
from django.contrib.auth.models import User
from .decorators import unauthenticated_user_only

# Create your views here.

@unauthenticated_user_only
def register_page(request):
    form = UserRegistrationForm()
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        create_user = UserCreationForm(request.POST)
        if create_user.is_valid():
            create_user.save()
            user = authenticate(username=username,password=password1)
            if user:
                login(request, user)

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_account = Account.objects.create(account=user,
                profile_picture=form.cleaned_data['profile_picture'],
                country=form.cleaned_data['country'],
                phone_number=form.cleaned_data['phone_number']
                                              )
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'signup/index.html', context)

    context={
        'form': form
    }
    return render(request, 'signup/index.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')


def profile_page(request):
    pass
