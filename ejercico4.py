#CICLO WHIDEM - Repite un bloque mientra una condicion y ete se usa cuando no save antemano cuanta veses nesesitas reoetir - depende loq ocurra durante el ejercicio
#rregla critica: algo dentro del while debe cambiar cada interaccion para q lao condicion evalualmente sea falsa sin eso el siclo nunca termina
#ejercico while basico contador y acomulador


N = int(input("suma del 1 hasta: "))
i = 1 #contador - enpieza en 1
suma = 0 #acomulador

while i <= N:
    suma = suma + 1
    i = i + 1

    print(f"suma de 1 a {N}: {suma}")

#verificacion de matematicas N*(N+1)/2
formula = N * (N +1) //2
print(f'verificacio con formula: {formula}')

#Tu turno: Reescribe el ejercicio usando for en lugar de while. ¿Cuál versión es más natural para este problema? Explica por qué con tus palabras.
N = int(input("Suma del 1 hasta: "))
suma = 0 # Acumulador

for i in range(1, N + 1):
    suma = suma + i

print(f"Suma de 1 a {N}: {suma}")

formula = N * (N + 1) // 2
print(f'Verificación con fórmula: {formula}')

#ejercicico - while para validar entrada : el patron de tendimiento
nota =float(input('calificacion (0-10)'))

while nota < 0 or nota > 10:
    print("calificacion invalida. Deve ser entre 0y 10.")
    nota +float(input("calificacion (0-10)"))

    print(f"calificacion registrada: {nota:1f}")
    print()

    #while true + break
    while True:
        edad = int(input("tu edad(1-100):"))
        if 1 <= edad <=100:
            break
        print("edad invalida, intentar de nuevo.")
        
print(f'edad registrada: {edad:1f}')



#Tu turno: Crea un programa que pida al usuario adivinar un número secreto (define tú el número con una constante). Con while, sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.
# Definimos el número secreto como una constante (en mayúsculas por convención)
NUMERO_SECRETO = 73
intentos = 0
prediccion = 0  # Inicializamos con un valor distinto al número secreto

print("🕵️‍♂️ ¡Bienvenido al juego de adivinar el número secreto!")

# El ciclo while se ejecutará MIENTRAS la predicción no coincida con el secreto
while prediccion != NUMERO_SECRETO:
    # Pedimos el número al usuario y lo convertimos a entero
    prediccion = int(input("Ingresa tu predicción: "))
    
    # Aumentamos el contador de intentos en 1
    intentos += 1 
    
    # Damos retroalimentación si falló
    if prediccion != NUMERO_SECRETO:
        print("Ese no es el número. ¡Intenta de nuevo!\n")

# Si el programa llega aquí, significa que el ciclo while terminó porque adivinó
print("-" * 40)
print(f"¡Felicidades! 🎉 El número secreto era {NUMERO_SECRETO}.")
print(f"Lograste adivinarlo en {intentos} intentos.")