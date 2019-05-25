"""dropdownlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path           
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
        PasswordResetView,
        PasswordResetDoneView,
        PasswordResetConfirmView,
        PasswordResetCompleteView
    )
# from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home,name = 'home'),
    path('login', auth_views.LoginView.as_view(template_name='testapp/login.html'),name = 'login'),
    path('logout',views.logout,name ='logout'),
    path('register', views.register,name = 'register'),
    path('profile', views.profile,name = 'profile'),
    path('profile/edit', views.edit_profile,name = 'edit_profile'),
    path('changepassword', views.change_password,name = 'change_password'),
    #Reset password
    path('passwordreset', PasswordResetView.as_view(),name = 'password_reset'),
    path('passwordreset/done', PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('passwordreset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
    path('passwordreset/complete', PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),
    #reset complete
    path('news/<int:id>/', views.show_news)
]