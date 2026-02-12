"""
RA04_c) Se han implementado estructuras de datos en programas para almacenar y procesar información.
3. Ordenar las puntuaciones con el algoritmo de la burbuja
    Crea un programa llamado ud3_ordenar_puntuaciones.py.
    Declara una lista de puntuaciones desordenadas (puedes reutilizar una lista fija, o bien copiar/pegar al inicio las puntuaciones usadas en el apartado anterior).
    Implementa el algoritmo de ordenación burbuja directamente en el cuerpo del script, usando bucles for o while, sin encapsularlo en una función.
        Recorre la lista comparando elementos adyacentes.
        Intercambia sus posiciones cuando el anterior sea mayor que el siguiente.
        Repite el proceso las veces necesarias hasta que la lista quede ordenada.
    Durante el proceso, muestra por pantalla algunos pasos intermedios (por ejemplo, la lista después de cada pasada completa) para poder seguir la evolución del algoritmo.

    Al final, muestra:
        La lista original (antes de ordenar).
        La lista ordenada de menor a mayor.
        Un breve mensaje indicando cuántas “pasadas” se han realizado.
"""

# 1. Listas
puntuaciones = [85, 92, 70, 45, 99, 60]
original = list(puntuaciones) # Guardamos una copia
n = len(puntuaciones)

print(f"Lista original: {original}")

# 2. Algoritmo
pasadas = 0

for i in range(n):
    pasadas += 1
    for j in range(0, n - i - 1):
        if puntuaciones[j] > puntuaciones[j+1]:
            puntuaciones[j], puntuaciones[j+1] = puntuaciones[j+1], puntuaciones[j]
    
    print(f"Pasada {pasadas}: {puntuaciones}")

# 3. Resultado final
print("\n--- RESULTADOS ---")
print(f"Original: {original}")
print(f"Ordenada: {puntuaciones}")
print(f"Se han realizado {pasadas} pasadas.")
