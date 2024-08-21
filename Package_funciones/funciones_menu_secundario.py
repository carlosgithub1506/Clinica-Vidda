from Package_input.input import *
from Package_funciones.funciones_mensajes import *
from Package_funciones.funciones_generales import *


# desplega un menu con diferentes opciones para modificar claves de diccionarios.
# Recibe una lista por parametros. Retorna una lista modificada
def mostrar_menu_modificar(lista:list[dict])->list:
    flag_1=False
    while True:
        clave = ""
        valor = False
        mensaje_programa(7)
        select_2 = input("Ingrese una opcion : A, B, C, D, E, F, G, H, X: ")
        select_2 = select_2.upper() 
        print("")
        if select_2 == "A":
            # Buscar empleado
            minimo = 4000000
            maximo = 99999999
            clave = "DNI"
            texto_input = f"Ingrese numnero de {clave} entre {minimo} y {maximo}:  " 
            dict_paciente = Buscar_por_numero(lista,clave,texto_input,minimo,maximo)
            if type(dict_paciente) == dict:
                mostrar_paciente(dict_paciente, True)
                flag_1 = True
            
        elif select_2 == "B" and flag_1 == True:
            # Modificar nombre
            clave = "Nombre"
            texto_input = f"Ingrese {clave} que no exceda la logintud de 20 caracteres,\nSin caracteres espeaciales ni numeros: " 
            valor = get_str(texto_input,False)
           
        elif select_2 == "C" and flag_1 == True:
            # Modificar Apellido
            clave = "Apellido"
            texto_input = f"Ingrese {clave} que no exceda la logintud de 20 caracteres,\nSin caracteres espeaciales ni numeros: " 
            valor = get_str(texto_input,False)
            
        elif select_2 == "D" and flag_1 == True:
            # modificar Edad
            clave = "Edad"
            minimo = 1
            maximo = 120
            texto_input = f"Ingrese {clave}: entre años {minimo} y años {maximo}:  " 
            valor = get_int(texto_input,minimo,maximo)

        elif select_2 == "E" and flag_1 == True:
            # modificar Altura
            clave = "Altura"
            minimo = 30
            maximo = 230
            texto_input = f"Ingrese {clave}: entre  {minimo} y {maximo}:  " 
            valor = get_int(texto_input,minimo,maximo) 

        elif select_2 == "F" and flag_1 == True: 
            # Modificar peso
            clave = "Peso"
            minimo = 10.0
            maximo = 300.0
            texto_input = f"Ingrese un Peso entre {minimo} y {maximo} en numero flotante Ej 55.5: "
            valor = get_float(texto_input,minimo,maximo)        

        elif select_2 == "G" and flag_1 == True:
            # Modificar DNI
            clave = "DNI"
            minimo = 4000000 
            maximo_numero = 99999999 
            texto_input = f"Ingrese numero de {clave} entre {minimo} y {maximo_numero}:  " 
            valor = get_int(texto_input,minimo,maximo_numero)
            if type(valor) == int and valor < 10000000:
                valor = str(valor)
                valor = valor.zfill(8)

        elif select_2 == "H" and flag_1 == True:
            # Modificar GRUPO SANGUINIO
            clave = "Grupo Sanguíneo"
            texto_input = f"Ingrese un Grupo Sanguinio:\n A+ / A- / B+ / B- / AB+ / AB- / O+/ O-: " 
            valor = get_str(texto_input,True)
                
        elif select_2 == "X":
            mensaje_programa(8)
            break
        elif flag_1 == False:
            mensaje_programa(2)
        else:            
            mensaje_programa(0)

        if valor != False:
            guardar_cambios = input(f"Desea Guardar los cambios de {clave} Ingrese: SI para guardar O ingrese Cualquier otra tecla para cancelar: ").upper()
            if guardar_cambios == "SI":
                dict_paciente = modificar_paciente(dict_paciente,clave,valor)
                mostrar_paciente(dict_paciente, True)
    
            else:
                imprimir("Cambios NO Guardados")
    return lista        

# desplega un menu con diferentes opciones para ordenar una lista de diccionarios. retorna una lista
def mostrar_menu_ordenar(lista:list[dict])->list:
    retorno = lista
    while True:
        
        mensaje_in=f"A) Ordenar por Nombre.\nB) Ordenar por Apellido.\nC) Ordenar por Altura.\nD) Ordenar por Grupo Sanguinio.\nX) Salir del menu de opciones.\nIngrese una Opcion: "
        print("*"*115)
        select_2 = input(mensaje_in).upper()
        
        clave = ""
        if select_2 == "A":
            clave = "Nombre"
        elif select_2 == "B":
            clave = "Apellido"
        elif select_2 == "C":
            clave = "Altura" 
        elif select_2 == "D":
            clave = "Grupo Sanguíneo" 
        elif select_2 == "X":
            mensaje_programa(8) 
            break   
        else:
            mensaje_programa(0) 
        if clave != "":
            print("*"*115)
            mayor_menor = input(f"A) Ordenar de Mayor a Menor.\nB) Ordenar de Menor a Mayor\nIngrese una Opcion: ").upper()
            if mayor_menor == "A":     
                lista = ordenar_lista_dicc_mayor_a_menor(lista,clave)
                mostrar_lista_paciente(lista) 
                retorno = lista
            elif mayor_menor == "B": 
                lista = ordenar_lista_dicc_menor_a_mayor(lista,clave)
                mostrar_lista_paciente(lista)
                retorno = lista
            else:
                mensaje_programa(0)
        system("pause")         
        system("cls")
    return retorno              


# desplega un menu con diferentes opciones para calcular el promedio  edad ,altura, peso. y muestra los resultados.
# Recibe una lista por parametros
def mostrar_menu_calcular_promedio(lista:list[dict])->None:
    
    while True:
        
        mensaje_in=f"A) Calcular Promedio por Edad.\nB) Calcular Promedio por Altura.\nC) Calcular Promedio por Peso.\nX) Salir del menu de opciones.\nIngrese una Opcion: "
        print("*"*115)
        select_2 = input(mensaje_in).upper()
        
        clave = ""
        if select_2 == "A":
            clave = "Edad"
            promedio = calcular_promedio(lista,clave)
            imprimir(f"El promedio de la {clave} es : {promedio}")

        elif select_2 == "B":
            clave = "Altura"
            promedio = calcular_promedio(lista,clave)
            imprimir(f"El promedio de la {clave} es : {promedio}")

        elif select_2 == "C":
            clave = "Peso" 
            promedio = calcular_promedio(lista,clave)
            imprimir(f"El promedio de la {clave} es : {promedio}")

        elif select_2 == "X":
            mensaje_programa(8) 
            break   
        else:
            mensaje_programa(0) 
        
        system("pause")         
        system("cls")            