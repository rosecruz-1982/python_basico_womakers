print("Qual o triangulo?")
medida1=int(input("Digite a medida do lado 1:"))
medida2=int(input("Digite a medida do lado 2:"))

medida3=int(input("Digite a medida do lado 3:"))

if medida1!=medida2!=medida3:
    print("Triangulo Escaleno")
elif medida1==medida2==medida3:
    print("Triangulo Equilátero")
else:
    print("Triangulo Isósceles")