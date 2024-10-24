# Codigo Happy Tails

# -*- coding: utf-8 -*-

from datetime import datetime  # Importamos función datetime para registrar días
from openpyxl import Workbook, load_workbook  # Importamos openpyxl para trabajar con Excel
import os

# Creamos un diccionario que tenga los diferentes menús del programa organizados por llaves
menus = {
    "Principal": {
        "Titulo": "Menu Principal",
        "Opciones": [
            "Agendar hospedaje canino",
            "Programar visitas a hogar",
            "Salir"
        ],
    },
    "Hospedaje": {
        "Titulo": "Agendar hospedaje canino",
        "Opciones": [
            "Agendar hospedaje canino",
            "Ver más información acerca del servicio",
            "Salir al menú principal"],
        "Costo de servicio": 200,
        "Información adicional": "Información no disponible por el momento"
    },
    "Visitas a hogar": {
        "Titulo": "Programar visitas a hogar",
        "Opciones": ["Programar visitas a hogar",
                     "Ver más información acerca del servicio",
                     "Salir al menú principal"],
        "Costo del servicio": 120,
        "Información adicional": "Información no disponible por el momento"
    }
}

# Función para imprimir un separador
def print_separator() -> None:
    print("*" * 48)

# Función para imprimir el menú
def print_menu(menu_name: str) -> None:
    print(f'** {menus[menu_name]["Titulo"]} **')
    print("Seleccione la opción que desea realizar...")
    for index, option in enumerate(menus[menu_name]["Opciones"]):
        print(f"{index + 1}, {option}")
    print("Ingrese el número de la opción a seleccionar:", end="")

# Función para evaluar la respuesta del usuario en el menú
def render_menu(menu_name: str) -> str:
    while True:
        try:
            print_menu(menu_name)
            return menus[menu_name]["Opciones"][int(input()) - 1]
        except (ValueError, IndexError):  # Manejo de error en caso de respuesta no válida
            print_separator()
            print("Opción no válida")
            print_separator()

# Función para confirmar el servicio deseado
def confirm_service() -> bool:
    while True:
        print(
            (
                "Confirmar servicio:\n"
                "1. Sí\n"
                "2. No\n"
            )
        )
        try:
            return int(input("Opción seleccionada: ")) == 1
        except ValueError:
            print_separator()
            print("Opción no válida")
            print_separator()

# Función para verificar si los datos son correctos
def verificar_datos() -> bool:
    print(
        (
            "Confirmar:\n"
            "1. Sí\n"
            "2. No\n"
        )
    )
    try:
        return int(input("Opción seleccionada: ")) == 1
    except ValueError:
        print_separator()
        print("Opción no válida")
        print_separator()
        return False

# Función para ingresar y verificar una fecha
def get_date_input(prompt) -> datetime:
    while True:
        try:
            date_object = datetime.strptime(input(prompt), '%d %b %Y')
            return date_object
        except ValueError:  # En caso de que se equivoque, se repetirá el proceso
            print("Fecha no válida. Ingrese en el formato indicado (Ejemplo: 23 Aug 2023)")

# Función para agendar un servicio basado en rango de fechas
def run_service_based_in_date_range(menu_name: str) -> bool:
    print_separator()
    nombre_cliente = input("Ingrese su nombre: ")
    nombre_mascota = input("Ingrese el nombre de su mascota: ")
    start_date = get_date_input("Ingrese la fecha de inicio (Ejemplo: 23 Aug 2023): ")
    end_date = get_date_input("Ingrese la fecha de fin (Ejemplo: 23 Aug 2023): ")
    print_separator()
    print(f"¿Sus datos son correctos? \nNombre: {nombre_cliente}\nNombre mascota: {nombre_mascota}")
    print(f"El rango de fechas seleccionado es: {start_date} - {end_date}")
    
    while not verificar_datos():
        print("Por favor, ingrese los datos nuevamente.")
        nombre_cliente = input("Ingrese su nombre: ")
        nombre_mascota = input("Ingrese el nombre de su mascota: ")
        start_date = get_date_input("Ingrese la fecha de inicio (Ejemplo: 23 Aug 2023): ")
        end_date = get_date_input("Ingrese la fecha de fin (Ejemplo: 23 Aug 2023): ")

    print_separator()
    cost = menus[menu_name]["Costo de servicio"]
    dias = (end_date - start_date).days
    total = dias * cost
    print(f"El costo por día es de {cost} pesos")
    print(f"El total de días es de: {dias} días, con un costo total de: {total} pesos")
    
    if confirm_service():
        print_separator()
        print("Su hospedaje quedó programado exitosamente. Gracias por usar Happy Tails ¡Vuelva pronto!")
        pass_info(nombre_cliente, nombre_mascota, start_date, end_date, total)
        return True
    else:
        print("\nRegrese al menú principal")
        return False

# Función principal que controla la navegación por los menús
def run_assistant() -> None:
    while True:
        option = render_menu("Principal")
        if option == menus["Principal"]["Opciones"][0]:
            while True:
                print_separator()
                option = render_menu("Hospedaje")
                if option == menus["Hospedaje"]["Opciones"][0]:
                    if run_service_based_in_date_range("Hospedaje"):
                        break
                elif option == menus["Hospedaje"]["Opciones"][1]:
                    print_separator()
                    print(menus["Hospedaje"]["Información adicional"])
                elif option == menus["Hospedaje"]["Opciones"][2]:
                    run_assistant()
                    break
                break
        elif option == menus["Principal"]["Opciones"][1]:
            while True:
                print_separator()
                option = render_menu("Visitas a hogar")
                if option == menus["Visitas a hogar"]["Opciones"][0]:
                    if run_service_based_in_date_range("Visitas a hogar"):
                        break
                elif option == menus["Visitas a hogar"]["Opciones"][1]:
                    print_separator()
                    print(menus["Visitas a hogar"]["Información adicional"])
                elif option == menus["Visitas a hogar"]["Opciones"][2]:
                    run_assistant()
                    break
                break
        elif option == menus["Principal"]["Opciones"][2]:
            print_separator()
            print("Gracias por usar Happy Tails, ¡Vuelva pronto!")
            break

# Función que registra la información en un archivo Excel
def pass_info(A1, A2, A3, A4, A5):
    file_name = "Python_prueba.xlsx"
    if os.path.exists(file_name):
        wb = load_workbook(file_name)  # Si existe, lo carga
    else:
        wb = Workbook()  # Si no existe, crea un nuevo archivo
    
    ws = wb.active
    ws.append([A1, A2, A3.date(), A4.date(), A5])
    wb.save(file_name)

# Ejecutar el asistente
if run_assistant() == True:
    run_assistant()
