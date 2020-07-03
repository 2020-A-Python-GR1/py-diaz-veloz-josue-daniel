import ast

print("Welcome to the Event System")

def ver_genero():
    i = 1
    print("Generos Disponibles:")
    for d in Generos:
        print(f'-->{i}._{d["genero"]}')
        print(f'    -Favorito: {d["favorito"]} -Region: {d["region"]} -Año: {d["anio"]} -Ejemplo: {d["ejemplo"]}')   
        i+=1
def ver_canciones(genero):
    i = 1
    for cancion in Generos[genero-1]['canciones']:
        print(f'-->{i}._{cancion["nombre"]}')
        i+=1

def menu_genero():
    ver_genero()
    print("Menu Principal")
    print("1:Crear Genero")
    print("2:Editar Genero")
    print("3.Elimanar Genero")
    print("4.Ir a Canciones por genero")
    print("5.Cerrar Sistema")
    opcion = input("escoger una opcion: ")
    return opcion
def menu_cancion():
    genero = input("escaga un genero: ")
    ver_canciones(int(genero))
    print("Menu Cancion")
    print("1:Crear Cancion")
    print("2:Editar Cancion")
    print("3.Elimanar Cancion")
    print("4.Volver al menu principal")
    opcion = input("escoger una opcion: ")
    return opcion

def ejectuar_menu_genero(opcion):
    opcion = int(opcion)
    if(opcion == 1):
        print(1)
    elif(opcion == 2):
        print(2)
    elif(opcion == 3):
        print(3)
    elif(opcion == 4):
        ejectuar_menu_cancion(menu_cancion())
    elif(opcion == 5):
        exit
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_menu_genero(int(opcion1))

def ejectuar_menu_cancion(opcion):
    opcion = int(opcion)
    if(opcion == 1):
        print(1)
    elif(opcion == 2):
        print(2)
    elif(opcion == 3):
        print(3)
    elif(opcion == 4):
        ejectuar_menu_genero(menu_genero())
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_menu_cancion(int(opcion1))


file = open("Musica.txt", "r")
contents = file.read()
Generos = ast.literal_eval(contents)
file.close()

ejectuar_menu_genero(menu_genero())