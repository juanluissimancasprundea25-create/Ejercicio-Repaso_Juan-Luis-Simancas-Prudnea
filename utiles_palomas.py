DISTANCIA_KM = 120

def registrar_paloma(palomas, anilla, nombre, propietario):
    if anilla not in palomas:
        palomas[anilla] = {"nombre": nombre, "propietario": propietario, "tiempo": None, "velocidad": None}
        return True
    return False

def registrar_tiempo(palomas, anilla, tiempo_min):
    if anilla in palomas:
        palomas[anilla]["tiempo"] = tiempo_min
        velocidad = calcular_velocidad(tiempo_min)
        palomas[anilla]["velocidad"] = velocidad
        return velocidad
    return None

def calcular_velocidad(tiempo_min):
    horas = tiempo_min / 60
    if horas > 0:
        return DISTANCIA_KM / horas
    return 0

def mostrar_todas(palomas):
    lista = []
    for anilla in palomas:
        p = palomas[anilla]
        linea = f"{anilla} | {p['nombre']} | {p['propietario']}"
        lista.append(linea)
    return lista

def datos_paloma(palomas, anilla):
    if anilla in palomas:
        return palomas[anilla]
    return None

def top_velocidades(palomas, limite=3):
    lista = []
    for anilla in palomas:
        p = palomas[anilla]
        if p["velocidad"] is not None:
            lista.append((anilla, p["velocidad"]))
    lista_ordenada = sorted(lista, key=lambda x: x[1])
    resultado = []
    indice = len(lista_ordenada) - 1
    contador = 0
    while indice >= 0 and contador < limite:
        resultado.append(lista_ordenada[indice])
        indice -= 1
        contador += 1
    return resultado

def velocidad_por_propietario(palomas):
    acumulados = {}
    conteo = {}
    for anilla in palomas:
        p = palomas[anilla]
        if p["velocidad"] is not None:
            prop = p["propietario"]
            if prop not in acumulados:
                acumulados[prop] = p["velocidad"]
                conteo[prop] = 1
            else:
                acumulados[prop] += p["velocidad"]
                conteo[prop] += 1
    promedios = {}
    for prop in acumulados:
        promedios[prop] = acumulados[prop] / conteo[prop]
    return promedios
