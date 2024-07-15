#Conversão
def dolar_americano(valor):
    conversao = valor/4.91
    print(f'Você poderia comprar:{conversao:.2f} doláres')
  
def peso_argentino(valor):
    conversao = valor/0.02
    print(f'{conversao:.2f} pesos argetinos')

def dolar_australiano(valor):
    conversao = valor/3.18
    print(f'{conversao:.2f} dólares australianos')  

def dolar_canadense(valor):
    conversao = valor/3.64
    print(f'{conversao:.2f} dólares canadenses')  
    
def franco_suiço(valor):   
    conversao = valor/0.42
    print(f'{conversao:.2f} francos suíços')  

def euro(valor):
    conversao = valor/5.36
    print(f'{conversao:.2f} euros')      

def libra_esterlina(valor):
    conversao = valor/6.21
    print(f'{conversao:.2f} libras esterlinas')     

valor = float(input("Digite quanto você tem em Reais para saber quanto vale em moedas estrangeiras:"))

dolar_americano(valor)
peso_argentino(valor)
dolar_australiano(valor)
dolar_canadense(valor)
franco_suiço(valor)
euro(valor)
libra_esterlina(valor)

