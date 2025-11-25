import utiles_palomas

def menu_principal():
    palomas = {}
    opcion = ""
    while opcion != "3":
        print("\n--- Gestor de colombofilia ---")
        print("1.Gestion de carrera")
        print("2.Consultas")
        print("3.Salir")
        opcion = input("Eligue la opcion que te mostramos :")
        match opcion:
            case "1":
                menu_gestion(palomas)
            case "2":
                menu_consultas(palomas)
            case _:
                if opcion != "3":
                    print("Esa opcion no existe , no ves ?")

def menu_gestion(palomas):
    opcion = ""
    while opcion != "c":
        print("\n--- Gestion de carrera ---")
        print("a) Registrar paloma")
        print("b) Registrar tiempo de llegada")
        print("c) Volver")
        opcion = input("Eligue la opcion que te mostramos :")
        match opcion:
            case "a":
                anilla = input("Escribe la anilla de la paloma que quieres añadir: ")
                nombre = input("Escribe el nombre de la paloma que deseas añadir: ")
                propietario = input("Escribe el nombre del propietario de la paloma que vas a añadir: ")
                ok = utiles_palomas.registrar_paloma(palomas, anilla, nombre, propietario)
                if ok:
                    print("Hemos añadido tu paloma : D")
                else:
                    print("Esa paloma ya eiste , se mas creativo ;)")
            case "b":
                anilla = input("Escribe la anilla de la paloma que va a llegar: ")
                t = input("Escribe el tiempo en minutos de la llegada de la paloma: ")
                if t.isdigit():
                    t = int(t)
                    v = utiles_palomas.registrar_tiempo(palomas, anilla, t)
                    if v is not None:
                        print(f"La velocidad de tu paloma es de: {v:.2f} km/h")
                    else:
                        print("Esa paloma no existe , mira a ver si has escrito correctamente ;)")
                else:
                    print("El tiempo tiene que ser positivo crack , o crees que estamos viaando al pasado ?")
            case "c":
                print("Hasta ahora")
            case _:
                print("Esa opcion no existe , no ves ?")

def menu_consultas(palomas):
    print("\n--- Consultas ---")
    print("\nLas palomas registradas son:")
    lista = utiles_palomas.mostrar_todas(palomas)
    for linea in lista:
        print(linea)
    anilla = input("\nEscribe la anilla de la paloma que quieres buscar (si no dejalo en blanco): ")
    if anilla != "":
        datos = utiles_palomas.datos_paloma(palomas, anilla)
        if datos is not None:
            print(f"Tiempo: {datos['tiempo']} min — Velocidad: {datos['velocidad']:.2f} km/h")
        else:
            print("Esa paloma no existe , mira a ver si has escrito correctamente ;)")
    print("\nEl top 3 palomas mas rappidas son:")
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
