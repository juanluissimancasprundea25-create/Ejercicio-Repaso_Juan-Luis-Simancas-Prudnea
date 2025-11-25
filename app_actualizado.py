import utiles_palomas

def menu_principal():
    palomas = {}
    opcion = ""
    while opcion != "6":
        print("\n--- Gestor de colombofilia ---")
        print("1. Gestion de carrera")
        print("2. Consultas")
        print("3. Guardar datos en archivo")
        print("4. Cargar datos desde archivo")
        print("5. Mostrar todas las palomas")
        print("6. Salir")
        opcion = input("Elige la opcion que te mostramos: ")
        match opcion:
            case "1":
                menu_gestion(palomas)
            case "2":
                menu_consultas(palomas)
            case "3":
                ok = utiles_palomas.guardar_datos(palomas)
                if ok:
                    print("Hemos guardado tus datos en el archivo , disfruta crack ;)")
            case "4":
                ok = utiles_palomas.cargar_datos(palomas)
                if ok:
                    print("Datos cargados perfect :)")
                else:
                    print("Ese archivo no existe , mira si has escrito bien :D")
            case "5":
                print("\nLas palomas registradas son:")
                lista = utiles_palomas.mostrar_todas(palomas)
                for linea in lista:
                    print(linea)
            case _:
                if opcion != "6":
                    print("Esa opcion no existe, no ves ?")

def menu_gestion(palomas):
    opcion = ""
    while opcion != "c":
        print("\n--- Gestion de carrera ---")
        print("a) Registrar paloma")
        print("b) Registrar tiempo de llegada")
        print("c) Volver")
        opcion = input("Elige la opcion que te mostramos: ")
        match opcion:
            case "a":
                anilla = input("Escribe la anilla de la paloma que quieres añadir: ")
                nombre = input("Escribe el nombre de la paloma que deseas añadir: ")
                propietario = input("Escribe el nombre del propietario de la paloma que vas a añadir: ")

                ok = utiles_palomas.registrar_paloma(palomas, anilla, nombre, propietario)
                if ok:
                    print("Hemos añadido tu paloma :D")
                else:
                    print("Esa paloma ya existe, se mas creativo ;)")
            case "b":
                anilla = input("Escribe la anilla de la paloma que va a llegar: ")
                t = input("Escribe el tiempo en minutos de la llegada de la paloma: ")
                if t.isdigit():
                    t = int(t)
                    v = utiles_palomas.registrar_tiempo(palomas, anilla, t)
                    if v is not None:
                        print(f"La velocidad de tu paloma es de: {v:.2f} km/h")
                    else:
                        print("Esa paloma no existe, mira a ver si has escrito correctamente ;)")
                else:
                    print("El tiempo tiene que ser positivo crack, ¿o crees que estamos viajando al pasado?")
            case "c":
                print("Hasta ahora")
            case _:
                print("Esa opcion no existe, no ves ?")

def menu_consultas(palomas):
    print("\n--- Consultas ---")
    print("\nLas palomas registradas son:")
    lista = utiles_palomas.mostrar_todas(palomas)
    for linea in lista:
        print(linea)
    anilla = input("\nEscribe la anilla de la paloma que quieres buscar (si no, dejalo en blanco): ")
    if anilla != "":
        datos = utiles_palomas.datos_paloma(palomas, anilla)
        if datos is not None:
            print(f"Tiempo: {datos['tiempo']} min — Velocidad: {datos['velocidad']:.2f} km/h")
        else:
            print("Esa paloma no existe, mira a ver si has escrito correctamente ;)")
    print("\nEl top 3 palomas mas rapidas son:")
    top = utiles_palomas.top_velocidades(palomas)
    pos = 1
    for anilla, vel in top:
        print(f"{pos}) {anilla} — {vel:.2f} km/h")
        pos += 1
    print("\nLa velocidad media por propietario es:")
    proms = utiles_palomas.velocidad_por_propietario(palomas)
    for prop in proms:
        print(f"{prop} — {proms[prop]:.2f} km/h")

menu_principal()
