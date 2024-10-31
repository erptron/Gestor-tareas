import os
import django

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gesproject.settings')
django.setup()

from tasks.models import User, State, Project, Task, ProjectType, TaskType, Comment, Priority
from django.db import connection

def create_initial_data():
    Comment.objects.all().delete()
    Task.objects.all().delete()
    Project.objects.all().delete()
    ProjectType.objects.all().delete()
    TaskType.objects.all().delete()
    State.objects.all().delete()
    User.objects.all().delete()
    Priority.objects.all().delete()

    with connection.cursor() as cursor:
        cursor.execute("ALTER SEQUENCE tasks_task_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_project_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_projecttype_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_state_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_tasktype_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_user_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_comment_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE tasks_priority_id_seq RESTART WITH 1;")

    # Crear Tipos proyectos
    task_types = [
        TaskType.objects.create(name='Tarea'),
        TaskType.objects.create(name='Error'),
        TaskType.objects.create(name='Documentacion')
    ]

    # Crear Tipos proyectos
    project_types = [
        ProjectType.objects.create(name='Interno'),
        ProjectType.objects.create(name='Cliente'),
        ProjectType.objects.create(name='Documentacion')
    ]

    # Crear usuarios
    users = [
        User.objects.create(name='Jonathan', email='jonathan@example.com'),
        User.objects.create(name='Diego', email='diego@example.com')
    ]

    # Crear estados
    states = [
        State.objects.create(name='Nuevo'),
        State.objects.create(name='En Progreso'),
        State.objects.create(name='Revisando'),
        State.objects.create(name='Cerrada')
    ]

    # Crear prioridades
    priorities = [
        Priority.objects.create(name='Urgente'),
        Priority.objects.create(name='Alta'),
        Priority.objects.create(name='Normal'),
        Priority.objects.create(name='Baja'),
        Priority.objects.create(name='Muy baja')
    ]

    proyectos = [
        ['Importación de datos', 'Importar datos de prueba desde GsBase.'],
        ['Gestor de tareas', 'Módulo para gestionar las tareas y los futuros tickets de cliente.'],
        ['Backend ERP', 'Código de servidor del ERP.'],
        ['Frontend ERP', 'Interfaz de usuario  generado con Angular.'],
        ['Aplicación fichajes', 'Aplicación para gestionar los marcajes de los empleados´.'],
        ['Aplicación SAT', 'Aplicación de movilidad por la que los técnicos puedan realizar su trabajo.'],
        ['Aplicación almacén', 'Aplicación para la gestión integral del almacén.'],
        ['Enlace A3', 'Enlace a la aplicación de contabilidad A3.'],
    ]

    # Crear proyectos y tareas
    for i in range(len(proyectos)):
        title, description = proyectos[i]
        st = states[0]
        if i in [0, 1, 3]:
            st = states[1]
        project = Project.objects.create(
            title=title,
            state=st,
            description=description,
            type=project_types[0]
        )

        Comment.objects.create(project=project, description='Comentario proyecto')
        num = 5 if i % 2 == 0 else 7
        for j in range(num):
            t=Task.objects.create(
                title=f'{j + 1} del Proyecto {i + 1}',
                description=f'Que hay que hacer',
                assignee=users[j % 2],
                state=states[0],
                priority=priorities[0],
                project=project
            )
            c = Comment.objects.create(task=t, description='Comentario')
            Comment.objects.create(parent=c, description='subComentario')
if __name__ == "__main__":
    create_initial_data()
    print("Datos iniciales creados exitosamente.")