


# validate_rango_int_float: recibe 3 parametros, dato  int o float, minimo o maximo tipos de enteros para validar rango el rango, retorna true | false
def validate_rango_int_float(dato:int|float, minimo:int, maximo:int)->bool:

    retorno = ""
    try:
        dato = int(dato)
        if int(dato) >= minimo and int(dato) <= maximo:
            retorno = True 
        else:
            retorno = False    
    except:  
        try:
            dato = float(dato)
            if float(dato) >= minimo and float(dato) <= maximo:
                retorno = True 
            else:
                retorno = False   
        except:
            retorno = False
    return retorno




# get_float recibe 4 parametros , pide un numero flotante por un input y lo validad por rango usando otra funcion puede retornar un float | booleano
def validate_float(numero:float, minimo:int, maximo:int, texto_input:str)-> float | bool:

    tipo_flotante="0123456789."
    contador = 2
    retorno=False
    flag=False
    mensaje_error = "Dato Ingresado es invalido"

    while contador >= 0:

        for j in range(len(numero)):

            if numero.count("..") == 1:
                break
            elif numero.count(".") == 1 and len(numero)== 1:
                break
            elif numero[j]  not in tipo_flotante:
                flag=False
                break
            elif "." not in numero:
                break
            elif validate_rango_int_float(numero,minimo,maximo) == False:
                break
            else:
                flag = True
        
        if flag == False and contador > 0 :
                print(f"{mensaje_error}, intento restantes: {contador}")    
                numero = input(texto_input).strip()

        elif flag == True  :
            retorno = float(numero) 
            break

        contador -= 1    
    return retorno
 


#  get_int recibe 5 parametros, pide un numero entero por un input y lo validad por rango usando otra funcion, retornar un str(numero)  
def validate_int(reintentos:int, numero:int, mensaje_input:str, minimo:int, maximo:int)->str:
 
    mensaje_error = "Dato Ingresado es invalido"
    contador = reintentos
    # pregunta si los datos son alfabeticos o sin son diferentes a numeros enteros y si estan fuera de rango vuelve a entrar en while hasta que el ususario ingrese correctamen y si
    # contador = a a cero rope el bucle y retorna false
    while numero.isalpha()== True or numero.isdigit() == False or validate_rango_int_float(numero,minimo,maximo) == False:
        
        if contador == 0:
            numero = False
            break
        print(f"{mensaje_error}, intento restantes: {contador}")    
        numero = input(mensaje_input).strip()
        contador -= 1
         
    return numero


# validate_str: recibe 2 parametros str, valida por tipo de dato y longitud puede retornar str | booleano
def validate_str(cadena:str, mensaje_input:str)->bool|str:
    contador=2
    retorno = False
    mensaje_error = f"Dato Ingresado es invalido, intentos restantes "

    while contador >= 0:
        cadena = cadena.strip()

        if cadena.isalpha() == True and len(cadena) > 0 and len(cadena) < 21:
            retorno = cadena
            break
        elif contador > 0:
            print(f"{mensaje_error} {contador}")
            cadena = input(mensaje_input).capitalize()
                 
        contador -= 1    
    return retorno




# # validate_str_tipo: recibe 2 parametros str, valida por tipo de dato, puede retornar str | booleano    
def validate_str_tipo(cadena: str, mensaje_input: str) -> bool | str:
    contador = 2
    retorno = False
    mensaje_error = "Dato Ingresado es invalido, intentos restantes"
    tipos_validos = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
    
    while contador >= 0: 
        cadena = cadena.strip().upper()  # Convertir a mayúsculas y eliminar espacios en blanco
        
        encontrado = False
        for tipo in tipos_validos:
            if tipo == cadena:
                retorno = cadena
                encontrado = True
                break
        
        if encontrado:
            break
        elif contador > 0:
            print(f"{mensaje_error} {contador}")
            cadena = input(mensaje_input).strip().upper() 
        
        contador -= 1    
    
    return retorno






 
# # validate_str_tipo: recibe 2 parametros str, valida por tipo de dato, puede retornar str | booleano    
# def validate_str_tipo(cadena: str, mensaje_input: str) -> bool | str:

#     contador = 2
#     retorno = False
#     mensaje_error = "Dato Ingresado es invalido, intentos restantes"
#     tipos_validos = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}
    
#     while contador >= 0: 
#         cadena = cadena.strip()  
#         if cadena in tipos_validos:
#             retorno = cadena
#             break
#         elif contador > 0:
#             print(f"{mensaje_error} {contador}")
#             cadena = input(mensaje_input).upper() 
                    
#         contador -= 1    
    
#     return retorno