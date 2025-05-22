"""
Procesa un archivo de temperaturas por estación, 
calculando suma, conteo, mínimo y máximo en tiempo O(1) por línea gracias al uso de un diccionario. 
Luego calcula el promedio y muestra resultados ordenados alfabéticamente.

v1: se usaron tuplas para almacenar (suma, conteo, mínimo, máximo), 
lo que requiere crear y reasignar la tupla en cada actualización.

v2: se usa defaultdict con listas mutables para actualizar los valores in-place, 
evitando la creación de nuevas tuplas y simplificando el código. 
Ambos enfoques mantienen O(1) la actualización por línea.
"""

from collections import defaultdict
import time

def default_station():
    return [0.0, 0, float('inf'), float('-inf')]

stations = defaultdict(default_station)

start = time.time()

with open("weather_stations.csv", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.rstrip('\n').split(';')
        if len(parts) != 2:
            continue
        station, temp_str = parts
        try:
            temp = float(temp_str)
        except ValueError:
            continue

        data = stations[station]
        data[0] += temp     # sum
        data[1] += 1        # count
        data[2] = min(data[2], temp)
        data[3] = max(data[3], temp)

result = [
    (station, round(data[2], 1), round(data[0] / data[1], 1), round(data[3], 1))
    for station, data in stations.items()
]

result.sort(key=lambda x: x[0])

for station, min_, avg, max_ in result:
    print(f"{station}: {min_}/{avg}/{max_}")

end = time.time()
print(f"\nTiempo total: {round(end - start, 2)} segundos")

