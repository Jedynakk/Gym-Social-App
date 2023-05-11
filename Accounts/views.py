from django.shortcuts import render,redirect
from Accounts.models import User, Profile
from django.views import View
from Accounts.forms import NewUserForm, LoginForm
from django.contrib.auth import authenticate, login

class NewUserView(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, "new_user.html", {"form":form})
    
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_staff = False
            user.save()
            Profile.objects.create(user=user)
            return redirect('login')
        return render(request, "new_user.html", {"form":form})
    

class LoginView(View):
    def get(self, request):
        form =  LoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        form =  LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html', {'form':form})