#Marin Moo Sergio Jesus
# PROGRAMA: Sistema de Venta de un Producto
# OBJETIVO: Aplicar conceptos básicos de Python (I/O, Casting, Tipos)

# DEClARACIÓN DE CONSTANTES (en mayúsculas por buena práctica)
IVA = 0.16
DESCUENTO = 0.10

# SECCIÓN 1: ENTRADA DE INFORMACIÓN (I/O) 
print("--- CAPTURA DE DATOS DE LA VENTA ---")
nombre_cliente = input("Por favor, ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_capturado = input("Ingrese el precio unitario del producto: $")
cantidad_capturada = input("Ingrese la cantidad de productos comprados: ")

# SECCIÓN 2: CONVERSIÓN DE DATOS (CASTING)
# Transformamos los textos de la función input() a tipos numéricos
precio_unitario = float(precio_capturado)
cantidad_productos = int(cantidad_capturada)

# SECCIÓN 3: PROCESAMIENTO Y CÁLCULOS
# Realizamos los cálculos matemáticos correspondientes
subtotal = precio_unitario * cantidad_productos
monto_descuento = subtotal * DESCUENTO
subtotal_con_descuento = subtotal - monto_descuento
monto_iva = subtotal_con_descuento * IVA
total_a_pagar = subtotal_con_descuento + monto_iva

# SECCIÓN 4: SALIDA DE INFORMACIÓN (GENERACIÓN DEL TICKET)
print("\n" + "="*45)
print("   TICKET DE COMPRA  MINI SUPER  shergiok      ")
print("="*45)

# Datos del Cliente y Producto
print(f"Cliente: {nombre_cliente}")
print(f"Producto adquirido: {nombre_producto}")
print(f"Cantidad: {cantidad_productos} pzas. | Precio Unitario: ${precio_unitario:.2f}")
print("-" * 45)

# Demostración del tipo de datos (Uso de la función type)
print("MUESTRA DE TIPOS DE DATOS IDENTIFICADOS:")
print(f"• usuario'nombre_cliente' es de tipo: {type(nombre_cliente)}")
print(f"• usuario 'precio_unitario' es de tipo: {type(precio_unitario)}")
print(f"• usuario 'cantidad_productos' es de tipo: {type(cantidad_productos)}")
print("-" * 45)
# Resumen Financiero de la Compra
print("RESUMEN DE LA COMPRA:")
print(f"nombre del clente:  {nombre_cliente:}" )
print(f"Subtotal bruto:         ${subtotal:.2f}")
print(f"Descuento aplicado (10%): -${monto_descuento:.2f}")
print(f"IVA correspondiente (16%): +${monto_iva:.2f}")
print("-" * 45)
print(f"TOTAL A PAGAR POR EL CLIENTE: ${total_a_pagar:.2f}")
print("="*45)
print("       ¡Gracias por su preferencia tilin ;)!       ")
print("="*45)