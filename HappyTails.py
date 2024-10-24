# Codigo Happy Tails

from datetime import datetime # Importamos funcion datetime para registrar dias 
from openpyxl import workbook, load_workbook # Importamos libreria openpyxl para que los datos puedan registrarse en excel
#encoding-utf-8

# Creamos un diccionario que tenga los diferentes menus del programa organizados por llaves 
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
            "Ver mas informacion acerca del servicio",
            "Salir al menu principal"],
        "Costo de servicio": 200,
        "Informacion adicional": "Informacion no disponible por el momento"
    },
    "Visitas a hogar": {
        "Titulo": "Programar visitas a hogar",
        "Opciones": ["Programar visitas a hogar",
                     "Ver mas informacion acerca del servicio",
                     "Salir al menu principal"],
        "Costo del servicio": 120,
    "Informacion adicional": "Informacion no disponible por el momento"
    }
}

# Crearemos una funcion para imprimir un separador que utilizaremos al cambiar de menu
def print_separator() -> None:
    print("*" * 48)

# Crearemos una funcion que utilice el diccionario y separador para imprimir los diferentes menus del programa
def print_menu(menu_name:str) -> None:
    print(f'** {menus[menu_name]["Titulo"]} **')
    print("Seleccione la opcion que desea realizar...")
    for index, option in enumerate(menus[menu_name]["Opciones"]):
        print(f"{index + 1}, {option}")
    print("Ingrese el numero de la opcion a seleccionar:", end="")


# Crearemos una funcion que evalue la respuesta del usuario en el menu y continue con el programa
def render_menu(menu_name:str) -> str:
    while True:
        try:
            print_menu(menu_name)
            return menus[menu_name]["Opciones"][int(input()) - 1]
        except(ValueError, IndexError): # En caso de ser una respuesta no valida imprimira un error
            print_separator()
            print("Opcion no valida")
            print_separator()

# Creamos una funcion para confirmar el servicio deseado
def confirm_service() -> bool:
    while True:
        print(
        (
            "Confirmar servicio:\n"
            "1. Si\n"
            "2. No/n"
        )
    )
        try:
            return int(input("Opcion seleccionada: ")) == 1
        except ValueError:
            print_separator()
            print("Opcion no valida")
            print_separator()

# Crearemos una funcion para que el usuario pueda verificar si sus datos son correctos
def verificar_datos() -> bool:
    print(
        (
            "Confirmar:\n"
            "1. Si\n"
            "2. No/n"
        )
    )
    try:
        return int(input("Opcion seleccionada: ")) == 1
    except ValueError:
            print_separator()
            print("Opcion no valida")
            print_separator()
            return False
    
# Crearemos una funcion que pida al usuario ingresar una fecha y verificar que este escrita correctamente
def get_date_input(prompt) -> datetime:
    while True:
        try:
            date_object = datetime.strptime(input(prompt), '%d %b %Y')
            return date_object
        except ValueError: # En caso de que se equivoque se repetira el proceso
            print("Fecha no valida. Ingrese en el formato indicado (Ejemplo: 23 Aug 2023)")

# Crearemos una funcion que pida al usuario toda la informacion requerida para agendar el servicio
def run_service_based_in_date_range(menu_name:str) -> bool:
    print_separator()
    nombre_cliente = input("Ingrese su nombre: ")
    nombre_mascota = input("Ingrese el nombre de su mascota: ")
    start_date = get_date_input("Ingrese la fecha de inicio (Ejemplo: 23 Aug 2023): ")
    end_date = get_date_input("Ingrese la fecha de inicio (Ejemplo: 23 Aug 2023): ")
    print_separator()
    print(f"¿Sus datos son correctos? \nNombre: {nombre_cliente}\nNombre mascota: {nombre_mascota}")
    print(f"El rango de fechas seleccionado es: {start_date} - {end_date}")
    if verificar_datos() == True:
        print_separator()
        cost = menus[menu_name]["Costo de servicio"]
        print(f"El costo por dia es de {cost}")
        total = (end_date - start_date).days * cost
        print(f"El total de dias es de: {(total)} pesos")
        if confirm_service():
            print_separator()
            print((
                "Su hospedaje queddo programado exitosamente."
                "Gracias por usar Happy Tails ¡Vuelva pronto!"
            ))
            pass_info(nombre_cliente, nombre_mascota, start_date, end_date, total)
            return True
        else: 
            print("\nRegrese al menu principal")
        return False
    else:
        run_service_based_in_date_range(menu_name)
    return False

# Crearemos nuestra funcion principal que servira como un bot que utilice todas las funciones antes definidas para que el usuario pueda navegar por los emnus, registrar fechas de servicio, salir, etc...
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
                    print(menus["Hospedaje"]["Informacion adicional"])
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
                    print(menus["Visitas a hogar"]["Informacion adicional"])
                elif option == menus["Visitas a hogar"]["Opciones"][2]:
                    run_assistant()
                    break
                break    
        elif option == menus["Principal"]["Opciones"][2]:
            print_separator()
            print((
                "Gracias por usar Happy Tails,"
                "¡Vuelva pronto!"
            ))
            break
        else:
            print_separator()
            print("Opcion no valida")
            return False
        return False    # Regresamos un false que nos permitira terminar con el proceso del codigo
    
# Creamos una funcion que usara la informacion que recolectamos en el programa para registrarla en un excel
def pass_info(A1, A2, A3, A4, A5):
    wb = load_workbook("Python_prueba.xlsx") # Aqui seleccionamos el archivo excel que vayamos a utilizar para guardar la informacion
    ws = wb.active
    ws.append([A1, A2, A3, A4, A5]) # Establecemos como queremos que se registren los datos
    wb.save("Python_prueba.xlsx") # Hacemos que los cambios se guarden en el archivo

# Establecemos que mientras nuestra funcion sea verdadera esta continuara funcionando
if run_assistant() == True:
    run_assistant()

    