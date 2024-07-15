print("Cálculo de Salário")
valor_hora=float(input("Digite o valor da sua hora trabalhada:"))
horas_mes=int(input("Digite quantas horas você trabalhou no mês:"))

salario = valor_hora*horas_mes

print(f'Seu salário esse mês é R${salario:.2f}')