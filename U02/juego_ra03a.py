"""
RA03_a) Se han implementado correctamente estructuras de control en programas en Python.
Implementa el núcleo del juego “Adivina el número” usando condicionales y bucles:
    Flujo de partida
        Establece un número secreto (constante).
        Pide intentos al usuario en un bucle.
        Compara el intento con el secreto y muestra pistas (if/elif/else): "Demasiado alto", "Demasiado bajo", "¡Correcto!".
        Finaliza la partida cuando acierte o se agoten los intentos (usa break si procede).
    Partidas múltiples
        Tras cada partida, pregunta "¿Jugar otra? (s/n)".
        Repite partidas mientras el usuario responda s.
"""

while True:
    # 1. Se define el número secreto
    NUMERO_SECRETO = 42 
    intentos_maximos = 5
    intentos_gastados = 0

    # Bucle de la partida
    while intentos_gastados < intentos_maximos:
        intento = int(input(f"Intento {intentos_gastados + 1}: "))
        intentos_gastados += 1

        if intento == NUMERO_SECRETO:
            print("¡Correcto!")
            break
        elif intento < NUMERO_SECRETO:
            print("Demasiado bajo")
        else:
            print("Demasiado alto")

    # 2. El input decide directamente si rompemos el bucle o no
    if input("¿Quieres jugar otra partida? (s/n): ") == "n":
        break # Si el usuario pone 'n', salimos del bucle infinito

print("Programa finalizado.")

