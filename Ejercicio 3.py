# = Solicitamos el salario del usuario
salario = input("Digite el salario: ")
salario = float(salario)

# = Si el salario es igual o mayor a 1000 se aplica un incremento del 15%
if salario >= 1000:
    salario *= 1.15
    print("El salario es de ", salario)

# = Si no se cumple lo de arriba se le aplica un incremento del 20%
else:
    salario *= 1.20
    print("El salario es de ",salario)