# = Solicitamos el año
anno = input("Digite el año: ")
anno = int(anno)

if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año " + str(anno) + " NO es bisiesto")