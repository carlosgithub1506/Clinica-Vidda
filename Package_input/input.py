from Package_input.validate import *
from Package_funciones.funciones_mensajes import *


# get_int() recibe por parametros un str, minimo(int), maximo(int) y opcionalmente otro entero, pide un numero entero por un input y llama a la funcion validate.int() para que lo valide, retorna un numero int() o false  
def get_int(texto_input:str, minimo:int,maximo:int,reintentos=2)->int|bool:

    retorno = False
    texto_input = f"\n{"*"*115}\n\n{texto_input}"
    numero = input(texto_input).strip()
    numero = validate_int(reintentos,numero,texto_input,minimo,maximo)

    if numero  == False :
        imprimir("Datos ingresados son incorrectos alcanzaste el maximo de reintentos")
    else:
        retorno = int(numero)
        
    return retorno



# get_float() recibe por parametros un str, minimo(int), maximo(int) , pide un numero entero por un input y llama a la funcion validate_float() para que lo valide, retorna un flota | false  
def get_float(texto_input:str, minimo:int,maximo:int)->float|bool:
    
    retorno = False
    texto_input = f"\n{"*"*115}\n\n{texto_input}"
    numero = input(texto_input).strip()
    numero = validate_float(numero,minimo,maximo,texto_input)
    
    if numero == False:
        imprimir("Datos ingresados son incorrectos alcanzaste el maximo de reintentos")
    else:
        
        retorno = numero
    return retorno

# get_str recibe 2 parametros:  str, booleano , pide un cadena por un input y la validad por tipo de dato y longitud, retornar un str | false 
def get_str(texto_input:str,tipo:bool)->None|str:
    
    retorno = False
    texto_input = f"\n{"*"*115}\n\n{texto_input:}"
    cadena = input(texto_input).capitalize()
    
    if tipo == False:
        cadena = validate_str(cadena,texto_input)
    else:
        cadena = validate_str_tipo(cadena.upper(),texto_input)
        
    if cadena == False:
        imprimir("Datos ingresados son incorrectos alcanzaste el maximo de reintentos")
    else:
        
        retorno = cadena

    return retorno 





