print("Sistema de Login")
login=(input("Digite seu login:"))
senha=(input("Digite sua senha:"))
if login=='admin' and senha=='admin123':
    print("Login efetuado com sucesso!")
else:
    print("Login ou senha incorreto! ")