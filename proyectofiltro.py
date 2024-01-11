import json

#FUNCIONES GENEROS
def registrar_genero():
    with open("generos.json", "r") as file:
        generos = json.load(file)
    id_genero = input("Ingrese el ID del genero a crear: ")

    if str(id_genero) in generos:
        print("Este genero ya se encuentra registrado.")
        return

    nuevo_genero = {}

    nuevo_genero["id"] = id_genero
    nuevo_genero["nombre"] = input("Digite el nombre del genero: ")

    generos[str(id_genero)] = nuevo_genero

    with open("generos.json", "w") as file:
        json.dump(generos, file, indent=2)
    print("Genero guardado exitosamente.")

def listar_generos():
    with open("generos.json", "r") as file:
        generos = json.load(file)
    for key, genero in generos.items():
        print(f"ID de genero: {genero['id']}")
        print(f"Nombre del genero: {genero['nombre']} \n")
    file.close()
    
#FUNCIONES ACTORES
def registrar_actor():
    with open("actores.json", "r") as file:
        actores = json.load(file)
    
    id_actor = input("Ingrese el ID del actor a registrar: ")

    if str(id_actor) in actores:
        print("Este actor ya se encuentra registrado.")
        return

    nuevo_actor = {}

    nuevo_actor["id"] = id_actor
    nuevo_actor["nombre"] = input("Digite el nombre del actor: ")

    actores[str(id_actor)] = nuevo_actor

    with open("actores.json", "w") as file:
        json.dump(actores, file, indent=2)
    print("Actor guardado exitosamente.")

def listar_actores():
    with open("actores.json", "r") as file:
        actores = json.load(file)
    for key, actor in actores.items():
        print(f"ID del actor: {actor['id']}")
        print(f"Nombre del actor: {actor['nombre']} \n")
    file.close()

#FUNCIONES FORMATOS
def registrar_formato():
    with open("formatos.json", "r") as file:
        formatos = json.load(file)
    id_formato = input("Ingrese el ID del actor a registrar: ")

    if str(id_formato) in formatos:
        print("Este formato ya se encuentra registrado.")
        return

    nuevo_formato = {}

    nuevo_formato["id"] = id_formato
    nuevo_formato["nombre"] = input("Digite el nombre del formato a registrar: ")

    formatos[str(id_formato)] = nuevo_formato

    with open("formatos.json", "w") as file:
        json.dump(formatos, file, indent=2)
    print("Formato guardado exitosamente.")

def listar_formatos():
    with open("formatos.json", "r") as file:
        formatos = json.load(file)
    for key, formato in formatos.items():
        print(f"ID del formato: {formato['id']}")
        print(f"Nombre del formato: {formato['nombre']} \n")
    file.close()


#FUNCIONES PELICULAS
    
def agregar_pelicula():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    with open("generos.json", "r") as file:
        generos = json.load(file)
    with open("actores.json", "r") as file:
        actores = json.load(file)
    with open("formatos.json", "r") as file:
        formatos = json.load(file)

    id_pelicula = input("Ingrese el ID de la pelicula a registrar: ")

    if str(id_pelicula) in peliculas:
        print("Esta pelicula ya se encuentra registrado.")
        return

    nueva_pelicula = {}

    nueva_pelicula["id"] = id_pelicula
    nueva_pelicula["nombre"] = input("Digite el nombre de la pelicula: ")
    nueva_pelicula["duracion"] = input("Digite la duracion de la pelicula: ")
    nueva_pelicula["sinopsis"] = input("Digite la sinopsis de la pelicula: ")

    for i, genero in enumerate(generos.values(),1):
            print(f"{i}. {genero['id']}. {genero['nombre']}")
    
    selec_genero = input("Seleccione el genero al que corresponde la pelicula (Ingrese el ID del genero)")

    for genero in generos.values():
        if genero["id"] == selec_genero:
            nueva_pelicula["genero"] = genero["id"]

### FORMATO
            
    for i, formato in enumerate(formatos.values(),1):
            print(f"{i}. {formato['id']}. {formato['nombre']}")

    selec_formato = input("Seleccione el formato al que corresponde la pelicula (Ingrese el ID)")
    
    for formato in formatos.values():
        if formato["id"] == selec_formato:
            nueva_pelicula["formato"] = formato["id"]

    ## ACTOR

    for i, actor in enumerate(actores.values(),1):
            print(f"{i}. {actor['id']}. {actor['nombre']}")

    selec_actor = input("Seleccione el actor que aparece la pelicula (Ingrese el ID)")

    for actor in actores.values():
        if actor["id"] == selec_actor:
            nueva_pelicula["actor"] = actor["id"]


    peliculas[str(id_pelicula)] = nueva_pelicula

    with open("peliculas.json", "w") as file:
        json.dump(peliculas, file, indent=2)
    print("Pelicula guardada exitosamente.")



def listar_peliculas():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    for key, pelicula in peliculas.items():
        print(f"----ID de la pelicula: {pelicula['id']}----")
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Duraciòn de pelicula: {pelicula['duracion']}")
        print(f"Sinopsis: {pelicula['sinopsis']}")
        print(f"ID genero: {pelicula['genero']}")
        print(f"ID formato: {pelicula['formato']} \n \n")
    file.close()

def editar_pelicula():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)

    id_pelicula=input("seleccione el ID de la pelicula que desea editar: ")

    for key, pelicula in peliculas.items():
        if id_pelicula == pelicula["id"]:
            pelicula["nombre"] = input("Digite el nuevo nombre de la pelicula: ")
            pelicula["duracion"] = input("Digite la nueva duracion de la pelicula: ")
            pelicula["sinopsis"] = input("Digite la nueva sinopsis de la pelicula: ")
            pelicula["genero"] = input("Digite el ID del nuevo genero de la pelicula: ")

    with open("peliculas.json", "w") as file:
        json.dump(peliculas, file, indent=2)
    print("Pelicula editada exitosamente.")


def buscar_pelicula():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    
    nombre_pelicula=input("seleccione el nombre de la pelicula que desea buscar: ")

    for key, pelicula in peliculas.items():
        if nombre_pelicula == pelicula["nombre"]:
                print("La informacion de esta pelicula es la siguiente: ")
                print(f"----ID de la pelicula: {pelicula['id']}----")
                print(f"Nombre: {pelicula['nombre']}")
                print(f"Duraciòn de pelicula: {pelicula['duracion']}")
                print(f"Sinopsis: {pelicula['sinopsis']}")
                print(f"ID genero: {pelicula['genero']}")
                print(f"ID formato: {pelicula['formato']} \n \n")
        else:
            print("NO se ha encontrado una pelicula con ese nombre. Intente nuevamente con otra pelicula.")
    file.close()


    ##GESTOR DE INFORMES 

def listar_por_genero():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    with open("generos.json", "r") as file:
        generos = json.load(file)

    for i, genero in enumerate(generos.values(),1):
        print(f"{i}. {genero['id']}. {genero['nombre']}")
    
    selec_genero = input("Seleccione el genero del cual desea listar peliculas (Ingrese el ID del genero)")

    peliculasfiltradas = []

    for key, pelicula in peliculas.items():
        if pelicula["genero"] == selec_genero:
            peliculasfiltradas.append(pelicula)

    print("Las peliculas que corresponden a este genero son: ", peliculasfiltradas)

def peliculas_silvester():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    with open("actores.json", "r") as file:
        actores = json.load(file)

    peliculas_silvester_s = []

    for key, pelicula in peliculas.items():
        if pelicula["actor"] == "A04":
            peliculas_silvester_s.append(pelicula)

    print("Las peliculas que protagoniza el actor Silvester Stallone son: \n", peliculas_silvester_s)

def buscar_pelicula_sinop_actores():
    with open("peliculas.json", "r") as file:
        peliculas = json.load(file)
    
    nombre_pelicula=input("seleccione el nombre de la pelicula que desea buscar: ")

    for key, pelicula in peliculas.items():
        if nombre_pelicula == pelicula["nombre"]:
                print("La sinopsis y actores de esta pelicula son los siguientes: ")
                print(f"----ID de la pelicula: {pelicula['id']}----")
                print(f"Nombre: {pelicula['nombre']}")
                print(f"Sinopsis: {pelicula['sinopsis']}")
                print(f"Actores: {pelicula['actor']}")
    else:
        print("NO se ha encontrado una pelicula con ese nombre. Intente nuevamente con otra pelicula.")
    file.close()




# --------------MENUS----------------------

opcion = None
print("------Bienvenido a BLOCKBUSTER------")
while opcion != 6:
    opcion = input(
        "\n MENÚ PRINCIPAL \n 1. Administrador de generos. \n 2. Administrador de actores. \n 3. Administrador de formatos \n 4. Gestor de informes \n 5. Gestor peliculas \n 6. SALIR \n"
    )
    if opcion == "1":
        opcion1 = None
        while opcion1 != "3":
            opcion1 = input(
                "\n ---GESTOR DE GENEROS--- \n 1. Crear genero. \n 2. Listar generos. \n 3. Ir al menú principal \n "
            )
            if opcion1 == "1":
                registrar_genero()
            elif opcion1 == "2":
                listar_generos()
            elif opcion1 == "3":
                break
            else:
                print(
                    "\n Opción inválida. Digite una opción válida de acuerdo al menú.\n"
                )

    elif opcion == "2":
        opcion2 = None
        while opcion2 != 4:
            opcion2 = input(
                "\n ---GESTION DE ACTORES--- \n 1. Crear actor. \n 2. Listar actores. \n 3. Ir al menú principal \n"
            )
            if opcion2 == "1":
                registrar_actor()
            elif opcion2 == "2":
                listar_actores()
            elif opcion2 == "3":
                break
            else:
                print(
                    "\n Opción inválida. Digite una opción válida de acuerdo al menú.\n"
                )

    elif opcion == "3":
        opcion3 = None
        while opcion3 != 7:
            opcion3 = input(
                "\n ---GESTION DE FORMATOS--- \n 1. Crear formatos. \n 2. Listar formatos. \n 3. Ir al menú principal \n"
            )
            if opcion3 == "1":
                registrar_formato()
            elif opcion3 == "2":
                listar_formatos()
            elif opcion3 == "3":
                break
            else:
                print(
                    "\n Opción inválida. Digite una opción válida de acuerdo al menú.\n"
                )
    elif opcion == "4":
        opcion4 = None
        while opcion4 != 4:
            opcion4 = input(
                "\n ---GESTION DE INFORMES--- \n 1. Listar peliculas de un genero especifico. \n 2. Listar peliculas con protagonsista SIlvester Stallone. \n 3. Buscar pelicula mostrar sinoposis y actores \n 4. Ir al menú principal "
            )
            if opcion4 == "1":
                listar_por_genero()
            elif opcion4 == "2":
                peliculas_silvester()
            elif opcion4 == "3":
                buscar_pelicula_sinop_actores()
            elif opcion4 == "4":
                break
    
    
    elif opcion == "5":
        opcion5 = None
        while opcion5 != 7:
            opcion5 = input(
                "\n ---GESTION DE PELICULAS--- \n 1. Agregar pelicula. \n 2. Editar pelicula. \n 3. Eliminar pelicula \n 4. Eliminar actor. \n 5. Buscar pelicula. \n 6. Listar todas las peliculas. \n 7. Ir al menú principal "
            )
            if opcion5 == "1":
                agregar_pelicula()
            elif opcion5 == "2":
                editar_pelicula()
            elif opcion5 == "3":
                print("Funcion en proceso...")
            elif opcion5 == "4":
                print("Funcion en proceso...")
            elif opcion5 == "5":
                buscar_pelicula()
            elif opcion5 == "6":
                listar_peliculas()
            elif opcion5 == "7":
                break
    elif opcion == "6":
        break
    else:
        print("\n Opción inválida. Digite una opción válida de acuerdo al menú.\n")
