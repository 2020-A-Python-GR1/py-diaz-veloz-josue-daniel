import ast

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
        print(f'-->{i}._{cancion["nombre"]} -artista: {cancion["artista"]} -año: {cancion["anio"]} -favorito: {cancion["favorito"]} -precio: ${cancion["precio"]}')
        i+=1

def crear_genero():
    nombre = input("Ingrese el nombre del genero: ")
    favorito = validar_favorito()
    region = input("Ingrese la region: ")
    anio = validar_numero("Ingrese el año: ", "año")
    ejemplo = input("Ingrese un ejemplo de este genero: ")
    genero = {
        'genero': nombre,
        'favorito': favorito, 
        'region': region,
        'anio': anio,
        'ejemplo':ejemplo,
        'canciones':[]
    }
    Generos.append(genero)
    escribir_archivo(Generos)
    print("Genero creado y guardado")
    return ejectuar_menu_genero(menu_genero())

def editar_genero(genero):
    if(genero > len(Generos)):
        genero1 = validar_numero("Ingrese un numero de genero valido: ","genero")
        return editar_genero(int(genero1)-1)
    else:
        print(Generos[genero-1]["genero"])
        return ejectuar_editar_genero(editar_genero_menu(),genero)
               
def editar_genero_menu():
    print("1.Nombre")
    print("2.Favorito")
    print("3.Region")
    print("4.Año")
    print("5.Ejemplo")
    print("6.Cancelar")
    respuesta = input("escoger una opcion para editar: ")
    return respuesta

def seguir_editando(genero):
    editar = validar_editar()
    if (editar == 'si'):
        return ejectuar_editar_genero(editar_genero_menu(),genero)
    else:
        return ejectuar_menu_genero(menu_genero())

def ejectuar_editar_genero(opcion, genero):
    opcion = int(opcion)
    if(opcion == 1):
        valor = input("Ingrese el nuevo valor: ")
        Generos[int(genero)-1]['genero'] = valor
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando(genero)
    elif(opcion == 2):
        favorito = validar_favorito()
        Generos[int(genero)-1]['favorito']= favorito
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando(genero)
    elif(opcion == 3):
        valor = input("Ingrese el nuevo valor: ")
        Generos[int(genero)-1]['region']=valor
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando(genero)
    elif(opcion == 4):
        anio = validar_numero("Ingrese el año: ", "año")
        Generos[int(genero)-1]['anio']= anio
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando(genero)
    elif(opcion == 5):
        valor = input("Ingrese el nuevo valor: ")
        Generos[int(genero)-1]['ejemplo']= valor
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando(genero)
    elif(opcion == 6):
        return ejectuar_menu_genero(menu_genero())
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_editar_genero(int(opcion1),genero)

def escribir_archivo(generos):
    f = open("Musica.txt","w")
    f.write( str(generos) )
    f.close()

def eliminar_genero(genero):
    if(genero > len(Generos)):
        genero1 = validar_numero("Ingrese un numero de genero valido: ","genero")
        return eliminar_genero(int(genero1)-1)
    else:  
        del Generos[genero-1]
        print("Genero Eliminado")
        escribir_archivo(Generos)
        return ejectuar_menu_genero(menu_genero())

def validar_editar():
    respuesta = input("Seguir editando si o no: ")
    if(respuesta == "si" or respuesta =="no"):
        return respuesta
    else:
        print("Ingrese una opcion valida")
        return validar_favorito()

def validar_favorito():
    respuesta = input("Genero Favorito si o no: ")
    if(respuesta == "si" or respuesta =="no"):
        return respuesta
    else:
        print("Ingrese una opcion valida")
        return validar_favorito()

def validar_numero(mgs,variable):
    respuesta = input(mgs)
    try:
        val = int(respuesta)
        return respuesta
    except ValueError:
        print(f'Ingrese un {variable} valido')
        return validar_numero(mgs, variable)

def validar_float(mgs,variable):
    respuesta = input(mgs)
    try:
        val = float(respuesta)
        return respuesta
    except ValueError:
        print(f'Ingrese un {variable} valido')
        return validar_numero(mgs, variable)

def crear_cancion(genero):
    nombre = input("Ingrese el nombre de la cancion: ")
    artista = input("Ingrese el artista: ")
    anio = validar_numero("Ingrese el año: ", "año")
    favorito = validar_favorito()
    precio = validar_float("Ingrese le precio: ", "precio")
    cancion = {
        'nombre': nombre,
        'artista': artista,
        'anio': anio,
        'favorito': favorito, 
        'precio':precio,
    }
    Generos[genero-1]["canciones"].append(cancion)
    print(f'Cancion ingresada a {Generos[genero-1]["genero"]}')
    ver_canciones(genero)
    escribir_archivo(Generos)
    return ejectuar_menu_cancion(menu_cancion(genero),genero)

def editar_cancion(genero):
    cancion = validar_numero("Ingrese el numero de cancion: ","cancion")
    if(int(cancion) > len(Generos[genero-1]["canciones"])):
        return editar_cancion(genero)
    else:
        print(Generos[genero-1]["canciones"][int(cancion)-1]["nombre"])
        ejectuar_editar_cancion(editar_cancion_menu(),genero,int(cancion))

def ejectuar_editar_cancion(opcion, genero, cancion):
    opcion = int(opcion)
    if(opcion == 1):
        valor = input("Ingrese el nuevo valor: ")
        Generos[genero-1]['canciones'][cancion-1]['nombre'] = valor
        print("Valor Actualizado")
        escribir_archivo(Generos)
        return seguir_editando_cancion(genero,cancion)
    elif(opcion == 2):
        valor = input("Ingrese el nuevo valor: ")
        Generos[genero-1]['canciones'][cancion-1]['artista']=valor
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando_cancion(genero,cancion)
    elif(opcion == 3):
        anio = validar_numero("Ingrese el año: ", "año")
        Generos[genero-1]['canciones'][cancion-1]['anio']= anio
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando_cancion(genero,cancion)
    elif(opcion == 4):
        favorito = validar_favorito()
        Generos[genero-1]['canciones'][cancion-1]['favorito']= favorito
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando_cancion(genero,cancion)
    elif(opcion == 5):
        valor = validar_float("Ingrese le precio: ", "precio")
        Generos[genero-1]['canciones'][cancion-1]['precio']= valor
        escribir_archivo(Generos)
        print("Valor Actualizado")
        return seguir_editando_cancion(genero,cancion)
    elif(opcion == 6):
        ver_canciones(genero)
        return ejectuar_menu_cancion(menu_cancion(genero),genero)
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_editar_cancion(int(opcion1),genero,cancion)

def seguir_editando_cancion(genero,cancion):
    editar = validar_editar()
    if (editar == 'si'):
        return ejectuar_editar_cancion(editar_genero_menu(),genero,cancion)
    else:
        ver_canciones(genero)
        return ejectuar_menu_cancion(menu_cancion(genero),genero)

def editar_cancion_menu():
    print("1.Nombre")
    print("2.Artista")
    print("3.Año")
    print("4.favorito")
    print("5.Precio")
    print("6.Cancelar")
    respuesta = input("escoger una opcion para editar: ")
    return respuesta

def eliminar_cancion(genero):
    cancion = validar_numero("Ingrese el numero de cancion: ","cancion")
    if(int(cancion) > len(Generos[genero-1]["canciones"])):
        return editar_cancion(genero)
    else:
        del Generos[genero-1]["canciones"][int(cancion)-1]
        print("Cancion Eliminada")
        escribir_archivo(Generos)
        ver_canciones(genero)
        return ejectuar_menu_cancion(menu_cancion(genero),genero)

def menu_genero():
    ver_genero()
    if (len(Generos) == 0):
        print("Menu Principal")
        print("1:Crear Genero")
        print("2:Editar Genero")
        print("3.Elimanar Genero")
        print("5.Cerrar Sistema")
        opcion = input("escoger una opcion: ")
        return opcion
    else:    
        print("Menu Principal")
        print("1:Crear Genero")
        print("2:Editar Genero")
        print("3.Elimanar Genero")
        print("4.Ir a Canciones por genero")
        print("5.Cerrar Sistema")
        opcion = input("escoger una opcion: ")
        return opcion

def menu_cancion(genero):
    if (len(Generos[genero-1]["canciones"]) == 0):
        print("Menu Cancion")
        print("1:Crear Cancion")
        print("4.Volver al menu principal")
    else:
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
        crear_genero()
    elif(opcion == 2):
        genero = validar_numero("Ingrese el numero del genero que quiere editar: ","genero")
        editar_genero(int(genero))
    elif(opcion == 3):
        genero = validar_numero("Ingrese el numero del genero que quiere eliminar: ","genero")
        eliminar_genero(int(genero))
    elif(opcion == 4):
        genero = input("escaga un genero: ")
        ver_canciones(int(genero))
        ejectuar_menu_cancion(menu_cancion(int(genero)),int(genero))
    elif(opcion == 5):
        exit
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_menu_genero(int(opcion1))

def ejectuar_menu_cancion(opcion, genero):
    opcion = int(opcion)
    if(opcion == 1):
        crear_cancion(genero)
    elif(opcion == 2):
        editar_cancion(int(genero))
    elif(opcion == 3):
        eliminar_cancion(int(genero))
    elif(opcion == 4):
        ejectuar_menu_genero(menu_genero())
    else:
        print('Escoga una opcion valida')
        opcion1 = input("Escaga una opcion: ")
        ejectuar_menu_cancion(int(opcion1),genero)

def open_file():
    try:
        file = open("Musica.txt", "r")
        contents = file.read()
        file.close
        return contents
    except IOError:
        file = open("Musica.txt", 'w')
        Generos = []
        escribir_archivo(Generos)
        file = open("Musica.txt", "r")
        contents = file.read()
        return contents

Generos = ast.literal_eval(open_file())   
ejectuar_menu_genero(menu_genero())

