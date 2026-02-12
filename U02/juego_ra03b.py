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

# --- VARIABLES GLOBALES ---
partidas_jugadas = 0
victorias = 0

# --- PARTIDAS MÚLTIPLES ---
jugar_otra = "s"

while jugar_otra.lower() == "s":
    # 1. Configuración de la partida
    NUMERO_SECRETO = 42  
    intentos_maximos = 5
    intentos_usados = 0
    ganado = False
    partidas_jugadas += 1 # Sumamos una partida al empezar
    
    print(f"\n--- PARTIDA NÚMERO {partidas_jugadas} ---")
    
    # 2. BUCLE DE INTENTOS
    while intentos_usados < intentos_maximos:
        print(f"Intento #{intentos_usados + 1} de {intentos_maximos}")
        
        try:
            intento = int(input("Introduce un número: "))
        except ValueError:
            print("❌ Error: Debes introducir un número válido. No gastas intento.")
            continue  # El 'continue' salta al principio del bucle sin sumar intento
        
        intentos_usados += 1
        
        # --- LÓGICA DE COMPARACIÓN ---
        if intento == NUMERO_SECRETO:
            print(f"¡CORRECTO! Enhorabuena, lo lograste en {intentos_usados} intentos.")
            victorias += 1
            ganado = True
            break  # Rompemos el bucle de intentos porque ya ganó
        elif intento < NUMERO_SECRETO:
            print("Demasiado bajo...")
        else:
            print("Demasiado alto...")
            
    # Mensaje si agota intentos y no gana
    if not ganado:
        print(f"Se agotaron los intentos. El número era {NUMERO_SECRETO}.")
    
    # --- PREGUNTAR SI CONTINUAR ---
    jugar_otra = input("\n¿Quieres jugar otra partida? (s/n): ")

# --- RESUMEN FINAL ---
print("\n" + "="*20)
print("RESUMEN DE LA SESIÓN")
print(f"Partidas jugadas: {partidas_jugadas}")
print(f"Aciertos: {victorias}")

# Cálculo del porcentaje de éxito 
if partidas_jugadas > 0:
    porcentaje = (victorias / partidas_jugadas) * 100
    print(f"Porcentaje de éxito: {porcentaje}%")

print("¡Gracias por jugar!")
