"""
RA04_b) Se han aplicado métodos y funciones integradas para el manejo de estructuras de datos
2. Registrar jugadores y puntuaciones con listas
    Crea un programa llamado ud3_registro_jugadores.py.
    Declara dos listas vacías al inicio del script:
        jugadores = []
        puntuaciones = []
    Mediante un bucle while o for, pide por teclado el nombre de un jugador y su puntuación (entero) tantas veces como el usuario quiera (por ejemplo, hasta que escriba FIN como nombre).
    En cada iteración:
        Añade el nombre a la lista jugadores.
        Añade la puntuación correspondiente a la lista puntuaciones.
    Al terminar la entrada de datos, muestra:
        El número total de jugadores registrados.
        La lista completa de jugadores y puntuaciones (por ejemplo, una línea por jugador: Nombre – Puntuación).
        La puntuación máxima y mínima, y los nombres de los jugadores que las han obtenido (puedes recorrer las listas con bucles, sin usar funciones propias).
"""

# Declaración listas vacías 
jugadores = []
puntuaciones = []

# Condición
continuar = True

# Bucle
while continuar:
    nombre = input("Introduce el nombre del jugador (o escribre 'FIN' para terminar): ")

    if nombre.upper() == "FIN":
        break # Rompemos el bucle si escribe FIN
    
    # Pedimos la puntuación 
    puntos = int(input(f"Introduce la puntuación de {nombre}: "))
    
    # Añadimos los datos a sus respectivas listas
    jugadores.append(nombre)
    puntuaciones.append(puntos)
# Número total de jugadores [cite: 78, 82]
total = len(jugadores)
print(f"\nTotal de jugadores registrados: {total}")

# Mostrar lista completa usando un bucle por índice 
print("--- Listado de Jugadores ---")
for i in range(total):
    print(f"{jugadores[i]} - {puntuaciones[i]}")
    # Inicializamos con el primer elemento de la lista (índice 0)
max_puntos = puntuaciones[0]
min_puntos = puntuaciones[0]
jugador_max = jugadores[0]
jugador_min = jugadores[0]

# Recorremos para comparar 
for i in range(len(puntuaciones)):
    # ¿Es esta puntuación más alta que la que ya teníamos? 
    if puntuaciones[i] > max_puntos:
        max_puntos = puntuaciones[i]
        jugador_max = jugadores[i]
    
    # ¿Es esta más baja? 
    if puntuaciones[i] < min_puntos:
        min_puntos = puntuaciones[i]
        jugador_min = jugadores[i]

print(f"\nGanador: {jugador_max} con {max_puntos} puntos.")
print(f"Puntuación más baja: {jugador_min} con {min_puntos} puntos.")
