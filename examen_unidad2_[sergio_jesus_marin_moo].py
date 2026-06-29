
total_ventas = 0.0
total_comisiones = 0.0
venta_maxima = 0.0
vendedor_estrella = ""


registros = [500, 1499.99, 2000, 5000]


print("--- SISTEMA DE VENTAS ---")
while True:
    try:
        num_ventas = int(input("¿Cuántas ventas deseas registrar en el día?: "))
        if num_ventas > 0:
            break  # Salimos del ciclo si el número es válido
        else:
            print("Error: Debes ingresar al menos 1 venta.")
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")


print("\n--- REGISTRO DE DATOS ---")
for i in range(1, num_ventas + 1):
    print(f"\nRegistro #{i}")
    nombre = input("Nombre del vendedor: ")
    

    while True:
        try:
            monto = float(input(f"Monto de la venta de {nombre}: $"))
            if monto > 0:
                break
            else:
                print("Error: El monto de la venta debe ser mayor a cero.")
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
            
    if monto < 500:
        porcentaje = 0.03  # 3%
    elif monto < 2000:
        porcentaje = 0.05  # 5%
    elif monto < 5000:
        porcentaje = 0.08  # 8%
    else:
        porcentaje = 0.12  # 12%
        
    # Cálculo matemático de la comisión
    comision = monto * porcentaje
    
    # 6. Actualización de acumuladores
    total_ventas += monto
    total_comisiones += comision
    

    if monto > venta_maxima:
        venta_maxima = monto
        vendedor_estrella = nombre
        
    # Guardamos los datos de esta iteración en un diccionario dentro de nuestra lista
    registros.append({
        "nombre": nombre,
        "monto": monto,
        "porc": porcentaje * 100,  
        "comision": comision
    })

print("\n" + "="*45)
print("   TICKET DE COMPRA  MINI SUPER  shergiok      ")
print("="*45)


print(f"vendedor: {nombre}")
print(f"porsentaje adquirido: {porcentaje}")
print(f"comicion adqiurida {comision}")
print("-" * 45)

print("MUESTRA DE TIPOS DE DATOS IDENTIFICADOS:")
print(f"• usuario'nombre_vendedor' es de tipo: {type(vendedor_estrella)}")
print(f"• usuario 'comision' es de tipo: {type(comision)}")

print("-" * 45)
# Resumen Financiero de la Compra
print("RESUMEN DE LA COMPRA:")
print(f"nombre del clente:  {nombre:}" )
print(f"comicion (3%,5%,8%,12%): -${comision:.2f}")

print("-" * 45)
print(f"TOTAL A PAGAR POR EL VENDEDOR: ${vendedor_estrella:.2f}")
print("="*45)
print("       ¡MONTO DE VENTAS ;)!       ")
print("="*45)