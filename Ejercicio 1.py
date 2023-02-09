# = Solicita el precio y la cantidad del producto
precio = input("Digite el precio del producto: ")
precio = float(precio)

cantidad = input("Digite la cantidad del producto: ")
cantidad = float(cantidad)

# = Aplica descuento
if cantidad >= 12:
    precio *= 0.80  

# = Calcula monto total
total = cantidad * precio

# = Imprime resultado
print("El monto a pagar es de",total)