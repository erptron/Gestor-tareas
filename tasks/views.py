# views.py

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, TaskCreateForm
from .models import Project, Task, User


def all_projects(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda (si existe)
    projects = Project.objects.all()  # Usamos el related_name para acceder a las tareas

    if query:  # Si hay un término de búsqueda, filtrar las tareas
        projects = projects.filter(title__icontains=query)  # Filtrar por título

    return render(request, 'projects/all_projects.html', {'projects': projects})

def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()  # Usamos el related_name para acceder a las tareas
    return render(request, 'projects/task_list.html', {'project': project, 'tasks': tasks})

def all_tasks(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda (si existe)
    tasks = Task.objects.all()  # Usamos el related_name para acceder a las tareas

    if query:  # Si hay un término de búsqueda, filtrar las tareas
        tasks = tasks.filter(title__icontains=query)  # Filtrar por título

    return render(request, 'projects/task_list.html', {'tasks': tasks})

def all_users(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda (si existe)
    users = User.objects.all()  # Usamos el related_name para acceder a las tareas

    if query:  # Si hay un término de búsqueda, filtrar las tareas
        users = users.filter(name__icontains=query)  # Filtrar por título

    return render(request, 'projects/all_users.html', {'users': users})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', project_id=task.project.id)  # Redirige a la lista de tareas del proyecto
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def new_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_tasks')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
    else:
        form = TaskCreateForm()

    return render(request, 'tasks/new_task.html', {'form': form})

def new_project(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_projects')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
    else:
        form = TaskCreateForm()

    return render(request, 'projects/new_project.html', {'form': form})


def inicio(request):
    # Obtener las tareas agrupadas por estado
    tareas_por_estado = Task.objects.values('state').annotate(count=Count('id'))
    estados = [t['state'] for t in tareas_por_estado]
    counts = [t['count'] for t in tareas_por_estado]

    return render(request, 'inicio.html', {
        'estados': estados,
        'counts': counts
    })