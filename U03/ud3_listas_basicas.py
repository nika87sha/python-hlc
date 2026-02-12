"""
RA04_a) Se han declarado y manipulado listas, tuplas y diccionarios

1. Crear y manipular una lista de puntuaciones

    Crea un programa llamado ud3_listas_basicas.py.
    Dentro del programa, declara una lista con al menos 6 puntuaciones de jugadores (por ejemplo, enteros de 0 a 100).

    Muestra en pantalla:
        La lista completa.
        La primera y la última puntuación (usando índices).
        La longitud de la lista con len().
    Modifica la lista en el propio script:
        Añade una nueva puntuación al final.
        Cambia el valor de una de las posiciones intermedias.
        Elimina una puntuación concreta usando del
    Vuelve a mostrar la lista actualizada y un breve mensaje indicando qué cambios has hecho.

"""

# Declarar la lista con 6 puntuaciones
puntuaciones_jugadores = [85, 92, 70, 45, 99, 60]

# Mostrar la lista completa
print("Lista completa:", puntuaciones_jugadores)

# Acceso a la primera y última usando índices

print("Primera puntuación:", puntuaciones_jugadores[0])
print("Última puntuación:", puntuaciones_jugadores[-1])

# Mostrar la longitud
print("Lista de jugadores:", len(puntuaciones_jugadores))

# Nueva puntuación
puntuaciones_jugadores.append(97)

# Actualizar tercera posición 
puntuaciones_jugadores[2] = 75

# Eliminar puntuación en el indice 4
del puntuaciones_jugadores[4]

print("\n--- Lista actualizada ---")
print(puntuaciones_jugadores)
print("Cambios realizados: Se a añadido 97 al final, modificado el tercer valor y eliminado el quinto")

