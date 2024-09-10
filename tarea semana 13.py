#tarea semana 13
def calcular_temperatura_promedio(temperaturas, semanas):
    """
    Calcula la temperatura promedio de cada ciudad durante el período dado.

    Parámetros:
    - temperaturas: Un diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas semanales.
    - semanas: El número de semanas para calcular el promedio.

    Retorna:
    - Un diccionario con los nombres de las ciudades como claves y sus temperaturas promedio como valores.
    """
    promedios = {}

    for ciudad, datos_semanales in temperaturas.items():
        suma_total = 0
        num_datos = 0

        for semana in datos_semanales:
            if len(semana) != semanas:
                raise ValueError(f"Las semanas de la ciudad {ciudad} no coinciden con el período especificado")
            suma_total += sum(semana)
            num_datos += len(semana)

        promedio = suma_total / num_datos
        promedios[ciudad] = promedio

    return promedios


# Datos
datos_temperaturas = {
    'Ciudad Manta': [
        [22, 24, 21, 23],  # Semana 1
        [23, 25, 22, 24],  # Semana 2
        [24, 26, 23, 25],  # Semana 3
        [25, 27, 24, 26]  # Semana 4
    ],
    'Ciudad Quito': [
        [18, 20, 17, 19],  # Semana 1
        [19, 21, 18, 20],  # Semana 2
        [20, 22, 19, 21],  # Semana 3
        [21, 23, 20, 22]  # Semana 4
    ],
    'Ciudad Guayaquil': [
        [30, 32, 29, 31],  # Semana 1
        [31, 33, 30, 32],  # Semana 2
        [32, 34, 31, 33],  # Semana 3
        [33, 35, 32, 34]  # Semana 4
    ]
}

#promedios
resultados = calcular_temperatura_promedio(datos_temperaturas, 4)
print(resultados)
