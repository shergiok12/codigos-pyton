# CICLO FOR // Reptte un bloque de cada elemento de una secuncia.se usa antemano cuantas veces quieres repetir o cuando quieres recorrer los elementos de una list
#ejercicio de variante de range()
#range (fin)-enpiesa en 0, termina antes de fin
print('range(5)')
for i in range(5):
    print(i, end=" ")#0 1 2 3  4
print()

#fange(inicio, fin)_desde inicio asta el fin
print('range(1,6):')
for i in range(1, 6):
    print(i, end=' ')
    print()
    
    #range(inicio, fin paso) -paso personalizado
    print('pares del 0 al 10')
    for i in range(0, 11, 2):
        print(i, end=' ')
        print()

#cuenta regresiva cin pasonegativo
print('cuenta regresiva:')
for i in range(5, 0, -1):
    print(i, end=' ')
print('despliegue')

#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 30 usando range() con los argumentos correctos. No uses if dentro del for para filtrar — usa el paso de range().
print('rango del 3 a 30')
for i in range(3, 33, 3):
    print(i, end=' ')
print('despliegue')

#ejercicio -for recorriendo una lista promedio y conteo.
#el for no solo funciona cn numeos 
calificaciones =[8.5, 9.0, 10.0, 7.5, 5.0, 8.0]

print('califivcaciones del grupo:')
for calificacion in calificaciones:
    print(f"{calificacion:.1f}")    

    total =0
    aprovados =0

    for calificacion in calificaciones:
        total = total + calificacion
        if calificacion>=6.0:
            aprovados = aprovados + 1

            promedio = total / len(calificaciones)
            reprovados = total / len(calificaciones) - aprovados

            print(f'\nPromedio de grupo: {promedio:.2f}')
            print(f'aprovados:{aprovados}')
            print(f'reprovados: {reprovados}')

#Turno: encuentra e imprime la calificación más alta y la más baja. Necesitarás dos variables que guarden el máximo y el mínimo mientras recorres la lista.
# Lista de calificaciones de ejemplo
calificaciones = [8.5, 9.2, 7.8, 10.0, 6.5, 9.0, 8.8]

max_cal = calificaciones[0]
min_cal = calificaciones[0]

for nota in calificaciones:
    total = total + calificacion
    if nota < maxima:
        reprovados = reprovados + 1
        maxima = nota
    if nota < minima:
        reprovados = reprovados + 1
        minima = nota

promedio = total / len(calificaciones)
reprovados = total / len (calificaciones) - aprovados
print("--- Reporte de Calificaciones ---")
print(f"La calificación más alta es: {maxima}")
print(f"La calificación más baja es: {minima}")



#Turno: encuentra e imprime la calificación más alta y la más baja. Necesitarás dos variables que guarden el máximo y el mínimo mientras recorres la lista.

alumnos = ['jose, julian, jonatan, shelmi,']
notas = [9.0, 10.0, 7.2, 9.8, 6.7,]

#encavezao de la tabla
print(f"{'no.':<5} {'alumno':12} {'nota':>6} {'estado':<10}")
print("-"*37)

for i, alumno in enumerate(alumnos):
    nota = notas[i]
    estado = "aproado" if nota >= 7.0 else "reprovado"
    print(f"{i+1:<5} {alumno:<12} {nota:>6.1f} {estado:>10}")

#Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y cantidad de aprobados, calculados dentro del mismo for que genera el reporte.
# =============================================================================
# CONSTANTES REQUERIDAS
# =============================================================================
MINIMA_APROBATORIA = 6.0
CANTIDAD_ESTUDIANTES = 15
CALIFICACION_MINIMA_VALIDA = 0.0
CALIFICACION_MAXIMA_VALIDA = 10.0

# INICIALIZACIÓN DE LISTAS
nombres = ['jose, julian, jonatan, shelmi']
calificaciones = [9.0, 10.0, 7.2, 9.8, 6.7]

print("=== Registro de calificaciones ===")
print("(captura de datos...)\n")


# ENTRADA Y VALIDACIÓN DE DATOS
for i in range(CANTIDAD_ESTUDIANTES):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación de {nombre} (0.0 - 10.0): "))
            if CALIFICACION_MINIMA_VALIDA <= calificacion <= CALIFICACION_MAXIMA_VALIDA:
                break
            else:
                print(f"Error: La calificación debe estar entre {CALIFICACION_MINIMA_VALIDA} y {CALIFICACION_MAXIMA_VALIDA}.")
        except ValueError:
            print("Error: Por favor, ingrese un número decimal válido.")
            
    nombres.append(nombre)
    calificaciones.append(calificacion)
    print("-" * 40)

# GENERACIÓN DEL REPORTE Y CÁLCULOS SIMULTÁNEOS (TU REQUERIMIENTO)
print("\n=== Reporte Final ===")
print(f"{'Alumno':<15} {'Nota':<6} {'Estado':<12} {'Letra'}")
print("-" * 40)

# Variables para el resumen final
suma_calificaciones = 0.0
total_aprobados = 0
total_reprobados = 0

mejor_nota = calificaciones[0]
mejor_alumno = nombres[0]
peor_nota = calificaciones[0]
peor_alumno = nombres[0]

# ---> AQUÍ ESTÁ EL CICLO ÚNICO <---
# Recorre a los estudiantes, imprime la tabla y calcula el resumen al mismo tiempo
for i in range(CANTIDAD_ESTUDIANTES):
    nota_actual = calificaciones[i]
    alumno_actual = nombres[i]
    
    # 1. Acumuladores para el resumen final (Promedio y conteo)
    suma_calificaciones += nota_actual
    
    if nota_actual >= MINIMA_APROBATORIA:
        estado = "Aprobado"
        total_aprobados += 1 # Contando aprobados
    else:
        estado = "Reprobado"
        total_reprobados += 1
        
    # 2. Determinación de la letra
    if nota_actual >= 9.0:
        letra = "A"
    elif nota_actual >= 8.0:
        letra = "B"
    elif nota_actual >= 7.0:
        letra = "C"
    elif nota_actual >= 6.0:
        letra = "D"
    else:
        letra = "F"
        
    # 3. Lógica para el mejor y peor (sin usar min ni max)
    if nota_actual > mejor_nota:
        mejor_nota = nota_actual
        mejor_alumno = alumno_actual
        
    if nota_actual < peor_nota:
        peor_nota = nota_actual
        peor_alumno = alumno_actual
        
    # 4. Genera la fila del reporte para este estudiante
    print(f"{alumno_actual:<15} {nota_actual:<6.1f} {estado:<12} {letra}")

# =============================================================================
# IMPRESIÓN DEL RESUMEN FINAL
# =============================================================================
print("-" * 40)

# Se calcula el promedio dividiendo la suma que se generó dentro del FOR
promedio_grupo = suma_calificaciones / CANTIDAD_ESTUDIANTES
porcentaje_aprobacion = (total_aprobados / CANTIDAD_ESTUDIANTES) * 100

print(f"Promedio: {promedio_grupo:.2f}")
print(f"Aprobados: {total_aprobados} | Reprobados: {total_reprobados}")
print(f"Mejor calificación: {mejor_alumno} con {mejor_nota:.1f}")
print(f"Peor calificación: {peor_alumno} con {peor_nota:.1f}")
print(f"Porcentaje de aprobación: {porcentaje_aprobacion:.1f}%")