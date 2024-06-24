from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, SigninForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from blog_app.models import Blog
 


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been successfully registered!")
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful signin
            else:
                # Invalid login credentials, display error message
                error_message = "Invalid email or password."
                return render(request, 'core/signin.html', {'form': form, 'error_message': error_message})
    else:
        form = SigninForm()
    return render(request, 'core/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after signout

@login_required(login_url='signin')
def profile(request):
    # Retrieve the user's profile
    user = request.user
    user_blogs = Blog.objects.filter(user=user)  # Retrieve blogs created by the user
    context = {'user': user, 'user_blogs': user_blogs}
    return render(request, 'core/profile.html', context)

@login_required(login_url='signin')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        # Handle form submission
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Redirect to profile page after update
    else:
        # Render form for updating profile
        form = ProfileUpdateForm(instance=user)
    context = {'form': form}
    return render(request, 'core/update_profile.html', context)


