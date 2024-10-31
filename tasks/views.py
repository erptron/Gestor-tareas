# views.py

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import TaskForm, TaskCreateForm, SubTaskForm, ProjectCreateForm, ProjectEditForm
from .models import Project, Task, User, Comment, ProjectType, State


@csrf_exempt
def update_project_field(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        project_id = request.POST.get("project_id")
        field_name = request.POST.get("field_name")
        new_value = request.POST.get("new_value")

        # Verifica que el campo es válido y actualiza el proyecto
        if project_id and field_name:
            try:
                project = Project.objects.get(id=project_id)

                if field_name == "type":
                    # Convertir el valor al tipo correcto para el campo de clave foránea
                    new_value = ProjectType.objects.get(id=new_value)
                elif field_name == "state":
                    # Convertir el valor al tipo correcto para el campo de clave foránea
                    new_value = State.objects.get(id=new_value)


                setattr(project, field_name, new_value)

                project.save()
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

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

def get_comments_structure(comment):
    """Recursively retrieves comments and their children."""
    return {
        'comment': comment,
        'children': [get_comments_structure(child) for child in comment.comment_parent.all()]
    }

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    # Recupera los comentarios de nivel superior para el proyecto
    top_level_comments = Comment.objects.filter(project=project_id, parent=None).order_by('creation_date')

    # Arma la estructura de comentarios y subcomentarios
    comments_structure = [get_comments_structure(comment) for comment in top_level_comments]
    if request.method == "POST":
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('all_projects')  # Redirige a la lista de tareas del proyecto
    else:
        form = ProjectEditForm(instance=project)
    return render(request, 'projects/edit_project.html',
                  {'form': form, 'project': project, 'comments_structure': comments_structure})

def new_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.state_id = request.POST.get('state', 3)  # Asignar el estado (1 por defecto)
            task.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_tasks')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
    else:
        form = TaskCreateForm()

    return render(request, 'tasks/new_task.html', {'form': form})

def new_comment(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.state_id = request.POST.get('state', 3)  # Asignar el estado (1 por defecto)
            task.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_tasks')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
    else:
        form = TaskCreateForm()

    return render(request, 'comments/new_comment.html', {'form': form})

def new_subtask(request, task_id):
    parent = get_object_or_404(Task, id=task_id)  # Esto asegura que la tarea existe

    if request.method == "POST":
        form = SubTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.state_id = request.POST.get('state', 3)
            task.parent_id = request.POST.get('parent', task_id)
            task.project_id = parent.project.id
            task.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_tasks')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
        else:
            # Si el formulario no es válido, se pasa el formulario con los errores a la plantilla
            return render(request, 'tasks/new_subtask.html', {'form': form, 'project_id': parent.project.id})
    else:
        form = SubTaskForm(initial={'parent': task_id})

    return render(request, 'tasks/new_subtask.html', {'form': form, 'project_id': parent.project.id})

def new_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva tarea en la base de datos
            return redirect('all_projects')  # Redirige a la lista de tareas, ajusta este nombre según tu configuración
    else:
        form = ProjectCreateForm()

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
