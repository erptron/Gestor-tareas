"""
URL configuration for gesproject project.

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
from django.conf import settings  # Importar settings
from django.conf.urls.static import static  # Importar static
from django.urls import path  # Asegúrate de tener esto

from tasks.views import task_list, all_projects, edit_task, inicio, all_tasks, all_users, new_task, new_project, \
    new_subtask, edit_project, update_project_field, new_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('all_projects', all_projects, name='all_projects'),
    path('all_tasks/', all_tasks, name='all_tasks'),
    path('tasks/new/', new_task, name='new_task'),
    path('projects/new/', new_project, name='new_project'),
    path('all_users', all_users, name='all_users'),
    path('project/<int:project_id>/', task_list, name='task_list'),
    path('projects/edit/<int:project_id>', edit_project, name='edit_project'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('subtask/new/<int:task_id>/', new_subtask, name='new_subtask'),
    path('update_project_field/', update_project_field, name='update_project_field'),
    path('comment/new/', new_comment, name='new_comment'),
]

# Solo si estás en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)