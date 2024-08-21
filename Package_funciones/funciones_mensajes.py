from os import system

 # Imprime un mesaje que recibe por parametros dentro de 2 print que genera una especie de bloque 
def imprimir (parametro_1:str, parametro_2="")->None:

    print(f"\n{"*"*115}")
    print(f"\n{parametro_1} {parametro_2}")
    print(f"\n{"*"*115}")



# Imprime o muestra una linea con el simbolo o icono que recibe como parametro y el tamano de la logintud depende  de los otros 2 parametros numero y longitud_icon
def marcar_sector(icon:str, numero:int, logintud_icon:int)->None:
   
    figura="\n"
    for i in range(numero):

        for j in range(logintud_icon):
            figura += icon

    figura +="\n"        
    print(figura)



# Muestra 2 mensaje dependiendo de la opcion que recibe por parametros(int)
def mensaje_juego(numero:int)->None:
    
    marcar_sector("*",1, 80)
    mensaje=""

    if numero == 1:
        mensaje=f"Bienvenido al Sistema de la Clínica Vidda\n"  
    else:
        mensaje=f"Es gusto poder ayudarte. . . .\n"

    print(mensaje,end=" ")
    marcar_sector("*",1, 80)
    system("pause")
    system("cls")  



# muestra un mensaje dependiendo la opcion que recibe por parametros(int)
def mensaje_programa(numero:int)->None:
   
    mensaje=""
    if numero == 1:    
        mensaje = f"\n{"*"*53}  Menu  {"*"*54}\n\nA) Ingresar Paciente.\nB) Modificar Paciente.\nC) Borrar Paciente.\nD) Mostrar todos los Pacientes\nE) Ordenar Paciente por Nombre | Apellido | Altura | Grupo Sanguinio.\nf) Buscar Paciente por DNI.\nG) Calcular Promedio por Edad | Altura | Peso\nH) Determinar compartibilidad de tipo de Sangre\nI) Mostrar matriz de compatibilidad\nX) Salir.\n\n{"*"*115} \n"
    elif numero == 2:
        mensaje = "*** Debe ingresar los datos solicitado en la opcion `A` ***"    
    elif numero == 3:
        mensaje=f"\nCerrando programa.....\n"
    elif numero == 6:
        mensaje=f"\nNo hay coincidencia.....\n" 
    elif numero == 7:
        mensaje=f"\n{"*"*51}  Sub-Menu  {"*"*51}\n\nA)Buscar Paciente por DNI.\nB)Modificar Nombre.\nC)Modificar Apellido.\nD)Modificar Edad.\nE)Modificar Altura.\nF)Modificar Peso.\nG)Modificar DNI.\nH)Modificar Grupo Sanguinio.\nX Salir del Sub-Menu.\n\n{"*"*115} \n"
    elif numero == 8:
        mensaje=f"\nCerrando Sub-Menu.....\n"

    else:
        mensaje = "\n**** Algo salio mal, ingrese los datos correctamente ****"        

    print(mensaje)    