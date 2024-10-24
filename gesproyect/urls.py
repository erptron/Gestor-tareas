"""
URL configuration for gesproyect project.

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

from tasks.views import task_list, all_projects, edit_task, inicio, all_tasks, all_users, new_task, new_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('all_projects', all_projects, name='all_projects'),
    path('all_tasks/', all_tasks, name='all_tasks'),
    path('tasks/new/', new_task, name='new_task'),
    path('projects/new/', new_project, name='new_project'),
    path('all_users', all_users, name='all_users'),
    path('project/<int:project_id>/', task_list, name='task_list'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),  # Esta línea es importante
]
