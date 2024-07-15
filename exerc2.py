def reverso_numero(numero):
    # Convertendo o número para uma lista de dígitos
    digitos = list(str(numero))
    
    # Invertendo a lista de dígitos
    digitos.reverse()
    
    # Convertendo a lista invertida de volta para um número inteiro
    reverso = int(''.join(digitos))
    
    return reverso

# Pedindo ao usuário para digitar o número
numero_str = input("Digite um número inteiro para calcular seu reverso: ")

# Verificando se o input é um número inteiro válido
try:
    numero = int(numero_str)
    reverso = reverso_numero(numero)
    print(f"O reverso de {numero} é {reverso}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
