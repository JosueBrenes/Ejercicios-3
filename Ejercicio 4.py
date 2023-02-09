# = Solictamos el salario de usuario
salario = input("Digite su salario: ")
salario = float(salario)

# = Solicitamos en que categoria quiere estar 
print("Las categorias van del 1 - 4")
categoria = input("Digite en que categoria le gustaria estar: ")
categoria = int(categoria)

# = Hacemos los calculos con if y else
if categoria == 1:
    salario *= 1.1
else:
    if categoria == 2:
        salario *= 1.12
    else:
        if categoria == 3:
            salario *= 1.15
        else:
            if categoria == 4:
                salario *= 1.2

print("Su salario es de:", salario)