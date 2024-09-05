
# Nombre y Apellido: carlos lopez
# Comision 111
##

from data import *
from Package_funciones.funciones_generales import *
from Package_funciones.funciones_menu_secundario import *
from Package_funciones.funciones_archivos import *
from os import system

# menu() recibe una lista  y un path, desplega opciones para que el usuario pueda realizar
def menu(lista:list[dict], path, lista_compatibilidad:list[dict], matriz:list[list])->None:
    mensaje_juego(1)
    mensaje_juego(2)

    if not os.path.exists(path):
        convertir_lista_a_csv(path,lista)
    lista = parsear_csv(path)
    lista = normalizar_lista(lista)
    flag = False
    continuar=True

    while continuar:

        mensaje_programa(1)
        select= input("Ingrese una opcion : A, B, C, D, E, F, G, H, X: ")
        select = select.upper()
        system("cls")

        if select == "A":
            # 1. Ingresar paciente:
            istuple = ingresar_lista_paciente(lista)
            if type(istuple) == tuple:
                lista = istuple[0]
                flag = istuple[1]

        elif select == "B" and flag == True :
            # 2. Modificar paciente:
            lista = mostrar_menu_modificar(lista)

        elif select == "C" and flag == True:
            # 3 Eliminará permanentemente a un PACIENTE de la lista original. Se pedirá el DNI del PACIENTE a eliminar
            minimo = 4000000
            maximo = 99999999
            retorno = eliminar_dni_id(lista,"DNI",minimo,maximo)
            if type(retorno) == tuple:
                lista = retorno[0]
                diccionario = retorno[1]
                agregar_a_json("Bajas.json",diccionario)

        elif select == "D" and flag == True:
            # 4. Mostrar todos, Imprimirá por consola la información de todos los paciente en formato de tabla:
            mostrar_lista_paciente(lista)

        elif select == "E" and flag == True:
            # 5 Ordenar Pacientes: por nombre, apellido, altura, grupo sanguinio de forma ascendente o descendente.
            lista = mostrar_menu_ordenar(lista)

        elif select == "F" and flag == True:
            # 6 Buscar empleado paciente por DNI
            minimo = 4000000
            maximo = 99999999
            mensaje_input = f"Ingrese numero de DNI entre {minimo} y {maximo}:  "
            dict_paciente = Buscar_por_numero(lista,"DNI",mensaje_input,minimo,maximo)
            mostrar_paciente(dict_paciente,True)

        elif select == "G" and flag == True:
            # 7 Calculará  promedio de todos los pacientes por edad, altura, peso.
            mostrar_menu_calcular_promedio(lista)

        elif select == "H" and flag == True:
            # “Determinar compartibilidad”
            minimo = 4000000
            maximo = 99999999
            mensaje_input = f"Ingrese numero de DNI entre {minimo} y {maximo}:  " 
            dict_paciente = Buscar_por_numero(lista,"DNI",mensaje_input,minimo,maximo)
            tipo_sangre = dict_paciente["Grupo Sanguíneo"]
            mostrar_paciente(dict_paciente, True)
            list_validos = mostrar_compatibles(tipo_sangre, lista_compatibilidad)
            buscar_mostrar_donates(list_validos,lista)

        elif select == "I" and flag == True:
            # tercera parte
            matriz = sumar_coincidencia(matriz, lista, lista_compatibilidad)
            mostrar_matriz_tipos_sanguineos(matriz)

        elif select == "X":
                # Cerrar programa(salir)
                convertir_lista_a_csv(path,lista)
                mensaje_programa(3)
                continuar = False

        else:
            mensaje_programa(0)
            mensaje_programa(2)

        system("pause")

        system("cls")


menu(lista_pacientes, "datos.csv", lista_compatibilidad_sangre, matriz_tipos_sanguineos)
     
