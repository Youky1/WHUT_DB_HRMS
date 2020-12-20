"""hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import re_path,path
from django.contrib import admin
from . import view

urlpatterns = [
    path('login',view.login),
    path('info/user',view.getUserInfo),
    path('info/wage',view.getWageInfo),
    path('department/info',view.getDepartmentInfo),
    path('department/change',view.changeDepartmentInfo),
    path('department/staff',view.getStaffByDepartment),
    path('hr/hire',view.hireNewStaff),
    path('hr/staff',view.getAllStaffInfo),
    path('hr/distribution',view.distribution),
    path('hr/manage',view.manage),
]