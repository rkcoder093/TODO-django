"""
URL configuration for ToDoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from todo.views import todo_list, todo_create, todo_edit, todo_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('edit/<int:pk>/', todo_edit, name='todo_edit'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    
]
