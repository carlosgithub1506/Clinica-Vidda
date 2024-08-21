from Package_input.input import *
from Package_funciones.funciones_generales import *
import json
import os
from datetime import datetime


#convertir_lista_a_csv: recibe un nombre de archivo y una lista, convierte una lista a un archivo csv 
def convertir_lista_a_csv(path:str,lista:list[dict])->None:

    try:
        # obtener las claves del diccionario
        lista_claves = list(lista[0].keys())
        linea = ""
        # dar formato a las claves de las lista
        for claves in lista_claves:
            linea += f"{claves},"
        linea += f"\n"
        # dar formato a los valores de las lista
        for diccionario in lista:
            for clave in lista_claves:
                linea += f"{diccionario[clave]},"
            linea +=f"\n"
        with open(path,"w",encoding="utf-8") as archivo:
            # escribir en el documento
            archivo.write(linea)
    except Exception as e:
        print(f"Hubo un Error {e}")
# convertir_a_csv("data.csv",lista_empleados)




# parsear_csv: recibe un path de un archivo csv por paramatros y retorna una lista de diccionario 
def parsear_csv(path: str) -> list:

    try:
        lista = []
        with open(path, "r", encoding="utf-8") as archivo:
            # Leer todas las líneas del archivo
            lista_csv = archivo.readlines()# devuelve una lista de cadena d string cada linea del archivo representa una lista
            # Obtener las claves desde la primera línea, eliminando espacios y saltos de línea
            lista_claves = lista_csv[0].strip().split(",") # optenemos las claves para los diccionarios dividiendo la lista en una subcadena con el split()
                                                            # strip()elimina los espacios en blanco
            
            # Iterar sobre las líneas restantes omitiendo la posicion 0 para solo optener los valores
            for i in range(1, len(lista_csv)):
                diccionario = {}
                # Obtener los valores, eliminando espacios y saltos de línea
                lista_valores = lista_csv[i].strip().split(",")
                # Crear el diccionario  claves a valores
                # for clave, valor in zip(lista_claves, lista_valores):
                #     if clave:
                #         diccionario[clave] = valor
                # # Añadir el diccionario a la lista
                for j in range(len(lista_claves)):
                    if lista_claves[j]:
                        diccionario[lista_claves[j]] = lista_valores[j]
                lista.append(diccionario)
        return lista
    except Exception as e:
        print(f"Hubo un Error {e}")
# lista = parsear_csv("datos.csv")





# guarda los diccionarios eliminados de la lista principal
#  agregar_a_json: recibe dos parametros un path y un diccionario, agrega un diccioanrio a un archivo json
def agregar_a_json(path:str, nuevo_diccionario:dict)->None:

    # Verificar si el archivo ya existe
    if os.path.exists(path):
        # Leer el contenido existente del archivo JSON
        with open(path, 'r', encoding='utf-8') as archivo:
            try:
                contenido = json.load(archivo) # lee y devuelve un objecto por ejemplo un diccionarios
            except json.JSONDecodeError: # captura un error que se puede generar al al intentar parsear
                # print("Error al leer el archivo JSON, inicializando una lista vacía.")
                contenido = []
    else:
        # Si el archivo no existe, inicializar una lista vacía
        contenido = []
    
    # Verificar que el contenido sea una lista antes de agregar el nuevo diccionario
    if not isinstance(contenido, list):
        # print("El contenido del archivo JSON debe ser una lista")
        pass
    else:
        # Agregar el nuevo diccionario a la lista
        contenido.append(nuevo_diccionario)
    
    # Escribir la lista actualizada de vuelta al archivo JSON
    try:
        with open(path, 'w', encoding='utf-8') as archivo:
            json.dump(contenido, archivo, ensure_ascii=False, indent=4)
        # print(f"El Paciente se ha agregado  y guardado en {path}")
    except Exception as e:
        print(f"Error al escribir el archivo JSON: {e}")
        


# recibe por parametros un str(path) convierte un archivo json a lista y retorna la lista
def json_a_lista_diccionarios(path:str)->list:

    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            # Cargar el contenido del archivo como un objeto Python
            contenido = json.load(archivo)
            # Verificar si el contenido es una lista
            if isinstance(contenido, list):
                return contenido
            else:
                return []
    except Exception as e:
        print(f"Hubo un Error : {e}")
        

# lista = json_a_lista_diccionarios(path_del_json)



#  Recibe por parametros un str(path), lee el último ID guardado en un archivo JSON, retorna un numero entero
def leer_ultimo_id(path: str) -> int:
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
            retorno = data.get("ultimo_id", 0)  # Si no hay 'ultimo_id', devolver 0
    except (FileNotFoundError, json.JSONDecodeError):
        retorno = 0  # Si el archivo no existe o está vacío, empezamos con 0
    return retorno




# Función para guardar el último ID en un archivo JSON, recibe por parametros path (str) y un entero
def guardar_ultimo_id(path: str, ultimo_id: int)->None:

    try:
        with open(path, 'w', encoding='utf-8') as archivo:
            json.dump({"ultimo_id": ultimo_id}, archivo)  #toma el diccionario y lo escribe en el archivo archivo en formato JSON.

    except Exception as e:
        print(f"Hubo un Error : {e}")




# Filtrar_salario: recibe una lista de diccionarios por parametros, retorna una lista filtrada por alguna clave buscada 
def filtrar_salario(lista:list[dict])->list:
    if type(lista) == list:
        maximo = 234315
        minimo = 0
        lista_salario = []
        mensaje_input = f"Ingresar un sueldo no mayor a ${maximo}: "
        sueldo = get_int(mensaje_input, minimo,maximo)

        for diccionario in lista:
            if diccionario["Salario"] > sueldo:
                lista_salario.append(diccionario)
        
    return lista_salario




# Filtrar_apellido: recibe una lista de diccionarios por parametros, retorna una lista filtrada por alguna clave buscada 
def filtrar_apellido(lista:list[dict])->list:
    
    if type(lista) == list:
        maximo = 234315
        minimo = 0
        lista_apellidos = []
        mensaje_input = f"Ingresar un Apellido : "
        apellido = get_str(mensaje_input,False)

        for diccionario in lista:
            if diccionario["Apellido"] == apellido:
                lista_apellidos.append(diccionario)

    return lista_apellidos





# Función para cargar el número del último reporte desde un archivo de texto, recibe por parametros un str(path). retorna un int
def cargar_numero_reporte(path:str)->int:
    try:
        
        with open(path, 'r', encoding='utf-8') as archivo:
            numero = int(archivo.read().strip())
            return numero 
    except FileNotFoundError:
        numero = 0
    return numero





# Función para guardar el número del último reporte en un archivo de texto. recibe por parametros str(path) y un numero.
def guardar_numero_reporte(path:str, numero_reporte:int)->None:

    try:
        with open(path, 'w', encoding='utf-8') as archivo:
            archivo.write(str(numero_reporte))
    except  Exception as e:
        print(f"Hubo un Error : {e}")





# formatea y y escribe un reporte en un archivo.txt recibe por parametros una lista y un str(path)
def realizar_reporte(lista:list,path:str)->str:
    try:
        numero = cargar_numero_reporte(path)
        numero += 1
        guardar_numero_reporte(path,numero)
        reporte = ""
        numero_reporte = numero
        reporte += f"Reporte N°: {numero}\n"

        # Obtener la fecha y hora actuales, Formatear la fecha y hora actuales como cadena
        fecha_reporte = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reporte +=f"Fecha: {fecha_reporte}\n"
        cantidad_coincidencia = len(lista)
        reporte += f"Cantidad de coincidencia: {cantidad_coincidencia}\n{"-"*80}\n"
        reporte += f"{"ID":<5} {"Apellido":<10} {"Nombre":<8} {"Salario":<9} {"Puesto":<9}\n"

        for e in lista:
            reporte +=(f"{e['ID']:<5} {e['Apellido']:<10} {e['Nombre']:<8} {e['Salario']:<9} {e['Puesto']:<9}\n")

        # Guardar el reporte en un archivo de texto
        reporte_path = f"reporte_{numero}.txt"
        with open(reporte_path, 'w', encoding='utf-8') as archivo:
            archivo.write(reporte)       
        return reporte
    except Exception as e:
        print(f"Hubo un Error : {e}")

