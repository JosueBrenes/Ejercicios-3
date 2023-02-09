valorA = input("Digite el valor de A: ")
valorA = int(valorA)

valorB = input("Digite el valor de B: ")
valorB = int(valorB)

valorC = input("Digite el valor de C: ")
valorC = int(valorC)

valorD = input("Digite el valor de D: ")
valorD = int(valorD)


if valorA > valorB and valorA > valorC and valorA > valorD:
    print("A es el numero mayor")
elif valorB > valorA and valorB > valorC and valorB > valorD:
    print("B es el numero mayor")
elif valorC > valorA and valorC > valorB and valorC > valorD:
    print("C es el numero mayor")
elif valorD > valorA and valorD > valorC and valorD > valorC:
    print("D es el numero mayor")