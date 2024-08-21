from Package_input.input import *
from Package_funciones.funciones_mensajes import *
from Package_funciones.funciones_archivos import *
from os import system
import json
import os




# obtener_claves_dict: Recibe un diccionario y retorna una lista con las claves de un diccionario | bool
def obtener_claves_dict(diccionario:dict)->list|bool:
    retorno = False
    if type(diccionario) == dict: 
        lista_claves = list(diccionario.keys())
        retorno = lista_claves
    return retorno


# obtener_valores_dict recibe un diccionario y retorna una lista con los valores de un diccionario | bool
def obtener_valores_dict(diccionario:dict)->list | bool:
    retorno = False
    if type(diccionario) == dict: 
        lista_valores = list(diccionario.values())
        retorno = lista_valores
    return retorno

# convertir_a_str: recibe una lista, convierte  cada elemento de la lista a str, lo concadena y da formato a una variable que luego retorna | puede retorna un string con un caracter repetidos 115 veces 
def convertir_a_str(lista:list,caracter="*")->str:

    string=f"{caracter*115}\n"
    separador = " | "

    if type(lista) == list:
        for elemento in lista:
            elemento = str(elemento)
            if len(elemento) < 1:
                string += f"{separador}{elemento:<3}"

            elif len(elemento) >3  and len(elemento)< 10:
                string += f"{separador}{elemento:<10}"

            else:
                string += f"{separador}{elemento:<12}"

        string +=f"{separador}"
    return string 
   

# crear_id: recibe una lista y un path(nombre de un archivo). retorna un numero entero | bool
def crear_id(lista:list[dict],path)->int | bool:
    
    retorno = None
    if type(lista) == list:
        # Verificar si el archivo ya existe
        if os.path.exists(path):
            id = leer_ultimo_id(path)  # Leer el último ID del archivo JSON  # Generar el nuevo ID  
        elif len(lista) == 0:
            id = 0    
        else:   
            flag = True
            buscando_id = 0
            for diccionario in lista: 
                if diccionario["ID"] > buscando_id or flag == True:
                    buscando_id = diccionario["ID"]
                    ultimo_id = buscando_id 
            id = ultimo_id 
        id += 1
        retorno = id
    return retorno

# ################### CRUD #######################

# ########## create ############

# crear_paciente: recibe 2 listas por parametros crea un diccionario con las lista de claves y  lista de valores. retorna un diccionario
def crear_paciente(lista_claves:list, lista_valores:list)->dict:
    diccionario={}
    for i in range(len(lista_claves)):
        diccionario[lista_claves[i]] = lista_valores[i]
    return diccionario


# Ingresar_lista_paciente: recibe una lista crea un id con la funcion crear un id, pide y valida datos si los datos estan todos ok llama a una funcion para crear un diccionario luego dicho dicionario es ingresado en una lista. puede retornar una lista o una tupla. 
def ingresar_lista_paciente(lista:list[dict])-> list | tuple:
    retorno = lista
    flag = True
    if type(lista) == list:
        lista_valores = []
        # obtenemos las claves
        diccionario = lista[0]  
        lista_claves = list(diccionario.keys())
        id = 0
        valor = True
        for claves in lista_claves:
            # se consigue el id usando otra funcion que la lee directamente de un json
            if claves == "ID":
               id = crear_id(lista,"Id.json")
               valor = id
            # verifica la clave que estan iterando en es momento en el for pide un dato y lo valida 
            elif claves == "Nombre" or  claves == "Apellido": 
                texto_input = f"Ingrese {claves} que no exceda la logintud de 20 caracteres,\nsin caracteres espeaciales ni numeros: "
                # si el dato es diferente false
                valor = get_str(texto_input,False)

            elif claves == "Edad":
                minimo = 1
                maximo = 120
                texto_input = f"Ingrese {claves}: entre años {minimo} y años {maximo}:  " 
                valor = get_int(texto_input,minimo,maximo)

            elif claves == "Altura":
                minimo = 30
                maximo = 230
                texto_input = f"Ingrese {claves}: entre  {minimo} y {maximo}:  " 
                valor = get_int(texto_input,minimo,maximo) 

            elif claves == "Peso":
                minimo = 10.0
                maximo = 300.0
                texto_input = f"Ingrese un Peso entre {minimo} y {maximo} en numero flotante Ej 55.5: "
                valor = get_float(texto_input,minimo,maximo) 

            elif claves == "DNI":
                minimo = 4000000
                maximo = 99999999
                texto_input = f"Ingrese numnero de {claves} entre {minimo} y {maximo}: "
                valor = get_int(texto_input,minimo,maximo)
                if type(valor) == int and valor < 10000000:
                    valor = str(valor)
                    valor = valor.zfill(8)
            
            else:
                texto_input = f"Ingrese un Grupo Sanguinio:\n A+ / A- /  B+ / B- /  AB+  /  AB- / “ O+ ”/ “ O- ”: " 
                valor = get_str(texto_input,True)
            # si el dato es diferente que false los agrega a una lista de valores
            if valor != False:
                lista_valores.append(valor)
                flag = True
            else:
                flag = False
                break

        if flag == True:
            # si todo salio bien y se logro validar correctamente llama a la funcion crear paciente y crea un nuevo diccionario y se agrega a la lista de pacientes
            nuevo_dicc = crear_paciente(lista_claves,lista_valores)
            lista.append(nuevo_dicc)
            guardar_ultimo_id("Id.json", id)  # Guardar el nuevo ID en el archivo JSON 
            # retorna una tupla con una lista y un boolenao setiando a una variable que permita ingresar en la otras funciones del menu
            retorno =(lista,flag) 
            imprimir("Se ingresaron correctamente los datos del nuevo Paciente")
        else:
            # si hubo algun error o la persona no puedo ingresar los datos correspondientes se imprime
            imprimir("Hubo un error al ingresar los datos")

    return retorno

# ######### Read #########

# mostrar_lista_paciente recibe una lista de diccionario la recorrre y muestra todos los elementos en formato de tabla, hace usos de otras funciones para obtener claves de un diccionario y formatear y mostrar
def mostrar_lista_paciente(lista:list[dict])->None:

    if type(lista) == list and  len(lista) > 0:
        lista_claves = obtener_claves_dict(lista[0])
        string_claves = convertir_a_str(lista_claves)
        print(string_claves)

        for empleado in lista:
            mostrar_paciente(empleado,False)
        base_tabla=convertir_a_str(False)                
        print(base_tabla)


# mostrar_paciente: recibe un diccionario y un booleano segun el estado del booleano va hacer el formato que se va a mostrar, hace uso de otras funciones para dar formato
def mostrar_paciente(empleado:dict, mostrar_un_elemento:bool) ->None:
    
    mensaje = "hubo un error"

    if type(empleado) == dict:
        lista_valores = obtener_valores_dict(empleado)
        string_valores = convertir_a_str(lista_valores,"-")
        mensaje = string_valores

        if  mostrar_un_elemento:
            lista_claves = obtener_claves_dict(empleado)
            string_claves = convertir_a_str(lista_claves)
            base_tabla=convertir_a_str(False)     
            mensaje=f"{string_claves}\n{string_valores}\n{base_tabla}"

    print(mensaje)

# ######### Update #########

# modificar_paciente: recibe un diccioanrio la clave y un valor que se va a modificar, retorna un dict | false
def modificar_paciente(diccionario:dict, clave:str, valor:str)-> dict | bool:

    retorno = False
    if type(diccionario) == dict:
        diccionario[clave] = valor
        imprimir(f"{clave} modificado correctamente")
        retorno = diccionario
    return  retorno


# ######### Delete ########

# eliminar_dni_id: recibe una lista, una clave, minimo(para validar por un rango), usa otra funcion que hace una busqueda, y borra un elemento de la lista, puede retornar una tupla | false 
def eliminar_dni_id(lista:list[dict], clave:str, minimo:int, maximo:int)->tuple | bool:
    retorno = False
    if type(lista) == list:

        mensaje_input = f"Ingrese numero de {clave} entre {minimo} y {maximo}: "
        diccionario = Buscar_por_numero(lista,clave,mensaje_input,minimo,maximo)
        
        if type(diccionario) == dict:
            mostrar_paciente(diccionario,True)
            confirmar=input("Esta seguro que quiere eliminar al Paciente.\nIngrese (1) para confirmar, O cualquier tecla para cancelar:")
            
            if confirmar == "1":
                eliminado = diccionario
                lista.remove(diccionario)
                tupla=(lista,eliminado)
                retorno = tupla
                imprimir("Paciente Borrado")
            else :
                imprimir("El Paciente NO se Elimino ")

    return  retorno

#######################################################################################


# buscar_clave: recibe una lista de diccionarios, una clave de un diccionario y un valor a buscar, si lo consigue retorna el diccionario o en caso contrario false  
def buscar_clave(lista: list[dict], clave: str, valor: str) -> dict | bool:
    retorno = False
    for diccionario in lista:

        if clave == "DNI":
            if int(diccionario[clave]) == int(valor):
                retorno = diccionario
                break
        else:
            if diccionario[clave] == valor:
                retorno = diccionario
                break
    if retorno == False:
        imprimir(f"{clave} no encontrado")
    return retorno



# Buscar_por_numero: recibe una lista, una clave, mensaje para usar en un input, un minimo y maximo para realizar una validacion por rango, hace llamados de varias funciones que piden datos, validan, buscan y muestran, retorna el diccionario si todo esta ok | false si no se pudo ejecutar correctamente 
def Buscar_por_numero(lista:list[dict],clave:str,mensaje_input:str,minimo,maximo)->dict | bool:

    retorno = False
    if type(lista) == list:
        valor = get_int(mensaje_input,minimo,maximo)

        if valor != False:
            valor = int(valor)
            dict_paciente = buscar_clave(lista,clave,valor)

            if type(dict_paciente) == dict:
                retorno = dict_paciente

    return retorno



# calcular_promedio: recibe una lista y una clave por la que va a calcular el promedio, puede retornar un entero | false 
def calcular_promedio(lista:list[dict],clave:str)->int|bool:
    retorno = False
    acumulador = 0 
    contador = 0
    if type(lista) == list:

        for diccionario in lista:
         
            if clave in diccionario: 
                acumulador += diccionario[clave]
                contador += 1      
        promedio = acumulador // contador
        retorno = promedio
    return retorno
           
# ********* ordenamientos *******************

# ordenar_lista_dicc_mayor_a_menor: recibe una lista y una clave con la cual va hacer compararaciones y ordenar de mayor a menor, puede retornar la lista ordenada | false
def ordenar_lista_dicc_mayor_a_menor(lista:list[dict], clave:str)->list|bool:
    retorno = False
    if type(lista) == list:

        for i in range(len(lista)):# Itera sobre los índices de la lista desde la primera posicion

            # Itera sobre los índices restantes después de i
            for j in range(i+1, len(lista)):
            # Compara el valor de la clave en el elemento i con el valor en el elemento j
                if lista[i][clave] < lista[j][clave]:
                    # Si el valor en j es mayor que en i, intercambia los elementos en la lista
                    lista[j], lista[i] = lista[i], lista[j]
        retorno = lista
    return  retorno    



# ordenar_lista_dicc_menor_a_mayor: recibe una lista y una clave con la cual va hacer compararaciones y ordenar de menor a mayor, puede retornar la lista ordenada | false
def ordenar_lista_dicc_menor_a_mayor(lista:list[dict], clave:str)->dict | bool:
    retorno = False
    if type(lista) == list:

        for i in range(len(lista)):
            for j in range(i+1, len(lista)):

                if lista[i][clave] > lista[j][clave]:
                    lista[j], lista[i] = lista[i], lista[j]
        retorno = lista
    return  retorno  


# Normaliza_lista: recibe una lista de diccionarios convierte los valores de la siguientes claves: altura y edad a tipo int, y peso a tipo float. retorna una lista.
def normalizar_lista(lista:list[dict])->list:

    if type(lista) == list:
        # obtiene las claves de un diccionario
        lista_claves = list(lista[0].keys())
        for diccionario in lista:

            for claves in lista_claves:

                key = diccionario[claves]
                if claves == "DNI":
                    pass
                elif claves == "Peso":
                    diccionario[claves] = float(key)
                elif key.isdigit():
                    diccionario[claves] = int(key)
    return lista

# determinar_compatibles recibe una lista y un diccionario busca compatibles y los muestras
def mostrar_compatibles( tipo_de_sangre:str, lista_compartibilidad)-> bool | list:
    retorno = False
    if type(tipo_de_sangre) == str:
       
        tipos_validos = ""
        mensaje = ""
        mensaje += f"{"-"*90}\n|{"Tipo de sangre ":<15} |  {"Puede donar a":<31} |  {"Puede recibir de ":<32}|\n{"-"*90}\n"
        resultado = determinar_compartibilidad_sangre(tipo_de_sangre, lista_compartibilidad)
        if resultado != False:
            donar =  ", ".join(resultado[0])
            recibir =  ", ".join(resultado[1])
            mensaje += f"|{tipo_de_sangre:<15} | {donar:<31} |  {recibir:<32}|\n{"-"*90}\n"
            tipos_validos = resultado[1]
            imprimir(mensaje)
            retorno = tipos_validos
    return retorno
    
def buscar_mostrar_donates(list_validos:list, lista:list[dict])->None:

        lista_donates = []
        for pacientes in lista:
            for tipos in list_validos:
                if pacientes["Grupo Sanguíneo"] == tipos:
                    lista_donates.append(pacientes)
            if len(lista_donates) == 3:
                break

        imprimir("Donates posibles")
        mostrar_lista_paciente(lista_donates)




def determinar_compartibilidad_sangre(tipo_de_sangre:str, lista:list[dict])->list:
    retorno = False
    if type(lista) == list and len(lista) > 0:
        donar = None
        recibir = None
        for tipo in lista:
            if tipo_de_sangre == tipo["Tipo"]:
                donar = tipo["Donar"]
                recibir = tipo["Recibir"]
                break
        retorno = (donar,recibir)
    return retorno


def sumar_donar_recibir(lista:list, tipos:str, matriz:list[list], iterador:int, posicion:int )->list:
    retorno = False
    if type(lista) == list and len(lista) > 0:
        for elemento in lista:
            if elemento == tipos:
                matriz[iterador][posicion] += 1
                break
        retorno = matriz
    return retorno
        


def sumar_coincidencia(matriz:list[list], lista_pacientes, lista_compartibilidad):
    retorno = False
    if type(matriz) == list and len(matriz) > 0:
        for i in range(len(matriz)):
            tipo_de_sangre = matriz[i][0]
            retorno = determinar_compartibilidad_sangre(tipo_de_sangre, lista_compartibilidad)
            if retorno != False:
                    donar = retorno[0] 
                    recibir = retorno[1] 
                    for paciente in lista_pacientes:
                        tipo_de_sangre_paciente = paciente["Grupo Sanguíneo"]
                        sumar_donar_recibir(donar, tipo_de_sangre_paciente, matriz, i , 1)                
                        sumar_donar_recibir(recibir, tipo_de_sangre_paciente, matriz, i , 2)
        retorno = matriz
    return  retorno 


def mostrar_matriz_tipos_sanguineos(matriz):
    if type(matriz) == list and len(matriz) > 0:
        print(f"{"*"*45}\nTipos Sanguíneos\tDonar\tRecibir")
        print(f"{"_"*40}|")
        for tipo in matriz:
            print(f"\t{tipo[0]:10}{tipo[1]:8}{tipo[2]:10}")
            print(f"{"_"*40}|")
        print(f"{"*"*45}")




