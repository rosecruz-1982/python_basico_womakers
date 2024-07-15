print("Cálculo do IMC")
altura=float(input("Digite sua altura:"))
peso=int(input("Digite seu peso:"))

imc = peso/(altura*altura)

print(f'Seu IMC é : {imc:.2f}' )