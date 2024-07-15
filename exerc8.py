print("Número maior")
num1=int(input("Digite o numero 1:"))
num2=int(input("Digite o numero 2:"))
num3=int(input("Digite o numero 3:"))
if num1+num2<=num3:
    print("O terceiro numero digitado é o maior.")
elif num1+num3<=num2:
    print("O segundo numero digitado é o maior.")
else: 
    print("O primeiro numero digitado é o maior.")