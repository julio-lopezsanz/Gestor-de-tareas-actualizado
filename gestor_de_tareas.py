"""
Gestor de tareas
Crear un pequeño programa que permita:
- Agregar tareas
- Marcar tareas como completadas
- Eliminar tareas (completadas o no)
- Mostrar la lista actual

Reglas claras
- Las tareas se guardan en una lista.
- Una tarea completada debe mostrarse con " ✔" al final.
- Ojo: aunque una tarea esté marcada como completada, debe poder eliminarse sin problemas.
- No uses librerías externas.
- Usa funciones (obligatorio).
"""

tasks = []
CHECK_MARK = "\u2705"

def normalize_task(task):
    """
    Elimina el check y espacios extras para comparar correctamente
    """
    return task.replace(CHECK_MARK, "").strip()


def add_task(tasks):
    """
    Agrega una tarea
    """
    task = input("Ingrese la tarea que desea registrar: ").strip()
    tasks.append(task)
    print("¡La tarea ha sido registrada!")


def mark_task(tasks):
    """
    Marca como completada una tarea de la lista
    """
    if not tasks:
        print("No hay tareas para completar")
        return

    task_input = input("Ingrese la tarea que ha completado: ").strip()
    for i, task in enumerate(tasks):
        if normalize_task(task).lower() == task_input.lower():
            if CHECK_MARK in task:
                print("Esta tarea ya está completada")
                return
            tasks[i] = f"{task} {CHECK_MARK}"
            print(f"La tarea '{task_input}' se ha marcado como completada")
            return
    print("No se ha encontrado la tarea")


def delete_task(tasks):
    """
    Elimina una tarea de la lista
    """
    if not tasks:
        print("No hay tareas para eliminar")
        return

    task_input = input("Ingrese la tarea que desea eliminar: ").strip()
    for task in tasks:
        if normalize_task(task).lower() == task_input.lower():
            tasks.remove(task)
            print(f"La tarea {task_input} ha sido eliminada")
            return
    print("No se ha encontrado la tarea")


def show_list(tasks):
    """
    Muestra la lista completa de tareas
    """
    if not tasks:
        print("No hay tareas para mostrar")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


while True:
    print("\n1- Agregar tarea")
    print("2- Marcar tarea como completada")
    print("3- Eliminar tarea")
    print("4- Ver todas las tareas")
    print("5- Salir")

    try:
        option = int(input("Ingrese la acción a realizar: "))

        if option == 1:
            add_task(tasks)
        elif option == 2:
            mark_task(tasks)
        elif option == 3:
            delete_task(tasks)
        elif option == 4:
            show_list(tasks)
        elif option == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Seleccione entre 1 y 5")

    except ValueError:
        print("Error: Solo se permiten números enteros")
