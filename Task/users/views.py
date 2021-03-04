from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


@login_required
def profile_page(request):
    profile = Profile.objects.get(user=request.user.id)
    return render(request, "users/profile.html", {'profile': profile})


@login_required
def profile_update(request):
    id_ = request.user.id
    user_profile = get_object_or_404(Profile, user=id_)
    form = ProfileForm(instance=user_profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # form.save()
            if request.FILES.get('image',None) != None:
                print(request.FILES)
                # try:
                #     os.remove(profile.user_image.url)
                # except Exception as e:
                #     print('Exception in removing old profile image: ', e)
                user_profile.image = request.FILES['image']
                user_profile.save()
            messages.success(request, "The Profile was updated successfully")
            return redirect('profile_page')
        else:
            messages.error(request, "The profile was not updated")
    return render(request, "users/profile_update.html", {'form': form})


def create(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get('password1')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            user = authenticate(request, username=username, password=password, first_name=first_name,last_name=last_name)
            if user is not None:
                login(request, user)
            return redirect('profile_page')
    return render(request, 'users/create.html', {'form': form})


