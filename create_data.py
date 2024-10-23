import os
import django

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gesproyect.settings')
django.setup()

from tasks.models import User, State, Project, Task

def create_initial_data():
    # Crear usuarios
    jonathan = User.objects.create(name='Jonathan', email='jonathan@example.com')
    diego = User.objects.create(name='Diego', email='diego@example.com')

    # Crear estados
    nuevo = State.objects.create(name='Nuevo')
    en_progreso = State.objects.create(name='En Progreso')
    revisando = State.objects.create(name='Revisando')
    cerrada = State.objects.create(name='Cerrada')

    # Crear proyectos y tareas
    for i in range(3):
        project = Project.objects.create(title=f'Proyecto {i + 1}', state=en_progreso)  # Asignar el estado 'Nuevo'

        for j in range(5):
            Task.objects.create(
                title=f'Tarea {j + 1} del Proyecto {i + 1}',
                description=f'Descripción de la Tarea {j + 1} del Proyecto {i + 1}',
                asignee=jonathan if j % 2 == 0 else diego,  # Alternar asignaciones entre Jonathan y Diego
                state=nuevo,  # Puedes asignar un estado inicial
                project=project
            )

if __name__ == "__main__":
    create_initial_data()
    print("Datos iniciales creados exitosamente.")