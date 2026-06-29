# python usa la sangia  (espacios al inicio de la linia) para delimitar bloques de codigo.{}, python usa 4 espacios por nivel.esta es la diferencia visual mas inportante entre python y otros lenguajes
#if condicion:
# instruccion1
#esle:
#  instruccion1

#toda estructrur de contro siempre termina en su primera linea con dos puntos ":". los dos puntos le dise a python: el bloque  de esta estructua comienza en la sigiente linea.sise omite,python genera sytaxerror 

#= asignar un valor
#===compra dos valores iguales
#!=diferencia de
#<mayor que / <= mayor o igual
#<menor que   / <=menor o igual
#and ambas condiciones true / o AL menos es true/ not negosiable

#IF ejecuta un bloque únicamente si la condición es True. Si la condición es False, el bloque se salta por completo y el programa continúa. Solo tiene una rama posible.

#SI condicion ENTONCES
#   Instrucción
#FIN SI
    #SI FALSE -> Se omite el bloque

#condicion simple
nota = 8.5

if nota >=6.0:
    print("el alubno aprobo")

    print("fin del programa")

#condicion doble - IF/ESLE
#el esle siempre garaniza que se ejecute algo.sin inportar si importar las condiciones es true  o false  toamunos de lso dos caminos
CALIFICACION_MINIMA  = 7.0

nota = float(input("ingrese la califiacion"))

if nota >= CALIFICACION_MINIMA:
    print("aprova con{nota:.1f}")
else:
    faltaron = CALIFICACION_MINIMA
    print(f"te paltaron {faltaron:.1f} puntos para aprobar")

    #condiciones opuestas:and / or en accion

    edad = int(input("tu edad: "))
    tiene_ine = input("tiene ine (si/no): ")

if edad >= 18 and tiene_ine  =="si":
    print('puedes votar')
else:
    print('no puedes votar aun')

    #validcin con rango "and"
    calificacion = float(input('calificacion (o/10) '))

if calificacion <0 or calificacion >10:
    print('calificacion fuera de rango')
else:
    print(f'calificacion registrada: {calificacion:.1f}')

    #Tu turno: Crea una condición que verifique si un año es bisiesto. Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, también debe ser divisible entre 400. Pista: usa el operador % (módulo).