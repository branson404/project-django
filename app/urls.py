"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, {"page":"index"}, name="index"),
    path('login/', views.index, {"page":"login"},  name="login"),
    path('register/', views.index, {"page":"register"},  name="register"),
    path('logout/', views.index, {"page":"logout"},  name="logout"),
    path('admin-page/', views.admin, name="admin"),
    path('admin-page/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin-page/update/<int:user_id>/', views.update_user, name='update_user'),
]
