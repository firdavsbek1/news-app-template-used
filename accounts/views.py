from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import User, UserLoginForm,ProfileForm,Profile,UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user and user.is_active:
            login(request, user)
            return redirect("home-page")
        else:
            return redirect('register')
    return render(request, 'registration/login.html', {"form": form, "login": True,'user':request.user})


def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            data=form.cleaned_data
            new_user.set_password(data['password1'])
            new_user.save()
            login(request,new_user)
            return redirect('user-profile',username=new_user.username)
    return render(request,'registration/register.html',{'form':form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home-page')


@login_required()
def user_profile(request, username):
    profile = Profile.objects.get(username=username)
    if request.user.is_authenticated and profile.user == request.user:
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form=ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('user-profile',username=profile.username)
        editable = request.GET.get('editable')
        return render(request, 'accounts/user-profile.html', {'profile': profile,'editable':editable,'form':form})
    else:
        return HttpResponse("get the fuck out of here!!")
