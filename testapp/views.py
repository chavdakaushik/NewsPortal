from django.shortcuts import render , redirect
from testapp.form import CustomUserCreationForm , EditProfileForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from testapp.models import news1 , news_items1

@login_required(login_url = '/login')
def home(request): 
    obj= news1.objects.all()
    return render(request,'testapp/home.html',{'news':obj})
    

def logout(request): 
    auth.logout(request)
    return render(request,'testapp/logout.html')
 
def register(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else: 
        f = UserCreationForm()
 
    return render(request, 'testapp/registration.html', {'form': f})

@login_required(login_url = '/login')
def profile(request): 
    return render(request,'testapp/profile.html',{'user':request.user})

@login_required(login_url = '/login')
def edit_profile(request): 
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance =request.user)

        if form.is_valid(): 
            form.save()
            return redirect('profile')
        else: 
            return redirect('editprofile')
    else: 
        form = EditProfileForm(instance=request.user)
        return render(request,'testapp/editprofile.html',{'form':form})

@login_required(login_url = '/login')
def change_password(request): 
    if request.method == 'POST':
        form = PasswordChangeForm(data= request.POST,user =request.user)

        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
        else: 
            return redirect('change_password')

    else: 
        form = PasswordChangeForm(user = request.user)
        return render(request,'testapp/changepassword.html',{'form':form})

@login_required(login_url = '/login')
def show_news(request,id): 
    obj = news1.objects.get(n_id = id)
    obj2 = news_items1.objects.filter(category_id = id)
    return render(request,'testapp/news.html',{'news':obj,'news_item':obj2})
