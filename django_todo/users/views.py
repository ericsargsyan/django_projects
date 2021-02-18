from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_page(request):
    # return HttpResponse("work bitch")
    return render(request, 'users/main_page.html')


def create_user(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('main_page')
    print(form)
    return render(request, "users/create_user.html", {'form': form})


def login(request):
    return render(request, 'users/create_user.html')


def logout(request):
    pass


# def user_register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#
#     form = UserRegisterForm()
#
#     return render(request, 'registration/user_register.html', {'form': form})
#
#
# def user_logout(request):
# 	logout(request)
# 	return redirect("home_page")