diccionario = {

}

def Ingresa_usuario() :
    contador_numeros = 0
    contador_letras = 0 
    contador_espacios = 0
    flag= True
    while flag == True :
        nombre= input('Ingrese nombre del usuario: ').capitalize()
        if nombre in diccionario :
            print('El nombre ya esta ingresado, use otro')
        else: 
            while flag == True :
                sexo = input('Ingrese sexo: ').upper()
                if sexo == 'M' or sexo == 'F' :
                    while flag == True :
                        contraseña = (input('Ingrese contraseña: '))
                        if len(contraseña) >= 8 :
                            for i in contraseña :
                                if i.isspace() :
                                    contador_espacios += 1 
                                if i.isalpha() :
                                    contador_letras += 1
                                if i.isnumeric():
                                    contador_numeros += 1 
                            if contador_espacios == 0 and contador_letras >= 1 and contador_numeros >= 1 :
                                diccionario[nombre] = [sexo, contraseña]
                                print('Contraseña creada con existo ')
                                flag = False 
                            else :
                                print('Contraseña no valida ')
                        else :
                            print('Ingrese contraseña mas larga ')           
                else :
                    print('Seleccione un sexo valido ')

def Buscar_usuario() :
    while True :
        nombre_buscar = input('Ingrese nombre de usuario: ').title()
        if nombre_buscar in diccionario :
            print(f'El sexo del usuario es: {diccionario[nombre_buscar][0]} y la contraseña es : {diccionario[nombre_buscar][1]}')
            break
        else :
            print('El usuario no se encuentra ')

def Borrar_usuario() :
    nombre_borrar = input('Ingrese usuario a borrar: ').title()
    if nombre_borrar in diccionario :
        diccionario.pop(nombre_borrar)
        print('Usuario borrado con exito ')
    else :
        print('No se pudo eliminar usuario ')

print('***MENU PRINCIPAL***')
print('1.- Ingresa usuario ')
print('2.- Buscar usuario ')
print('3.- Eliminar usuario ')
print('4.- Salir ')
while True :
    try :
        op = int(input('Ingrese opcion: '))
    except ValueError :
        print('Ingrese una opcion valida por favor ')
        continue
    if op >= 5 or op <= 0 :
        print('Ingrese una opcion valida por favor ')
    elif op == 1 :
        Ingresa_usuario() 
        print(diccionario)
    elif op == 2 :
        Buscar_usuario()
    elif op == 3 :
        Borrar_usuario()
        print(diccionario)
    elif op == 4 :
        print('Programa terminando . . .')
        break
#hola profe lo quiero mucho 

