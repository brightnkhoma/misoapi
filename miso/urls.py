"""
URL configuration for miso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import create_catchment,create_project,create_person,add_excel_data,assignFile,clear_users,populateForms,clearAllSnippets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createcatchment/', create_catchment),
    path('createproject/', create_project),
    path('createperson/', create_person),
    path('feeddata/', add_excel_data),
    path('addnumber/', assignFile),
    path('clear/', clear_users),
    path('populate/', populateForms),
    path('delete/', clearAllSnippets),
]
