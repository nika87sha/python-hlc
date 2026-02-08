"""
RA03_b) Se han realizado entradas y salidas de datos de forma adecuada.
Completa el juego con E/S robusta y mensajes claros:
    Entrada válida
        Cada intento debe ser numérico. Si el usuario introduce algo no numérico, muestra un mensaje y vuelve a pedir el dato sin gastar intento.
        Usa prompts claros (ej.: Intento #2 de 5. Escribe un número:).
    Salida clara
        Muestra mensajes legibles en cada caso ("Te quedan X intentos", "No acertaste. El número era …", "¡Correcto en N intentos!").
        Al salir del juego (cuando el usuario responda n a “¿Jugar otra?”) imprime un resumen: partidas jugadas, aciertos, porcentaje de éxito.
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

