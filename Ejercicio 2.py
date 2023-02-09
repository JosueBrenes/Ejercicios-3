# = Solicitamos el salario de un colaborador 
salario = input("Digite el salario de un colaborador: ")
salario = float(salario)

# = Si el salario es igual o mayor a 1000 no se aplica rebaja 
if salario >= 1000:
    print("El salario es 1000")

# = Si el salario es menor a 1000 aplicamos la rebaja 
if salario <= 1000:
    salario *= 1.15
    print("El salario es", salario)