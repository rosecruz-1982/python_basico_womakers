print("Classifica usuário")
idade=int(input("Digite sua idade:"))
if idade>0 and idade<12:
    print("Você é uma criança.")
elif idade>=12 and idade<18:
    print("Você é adolescente.")
elif idade>=18 and idade<65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")