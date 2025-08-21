# 5) Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições:

# Deve ter pelo menos 8 caracteres.

# Deve conter pelo menos uma letra maiúscula.

# Deve conter pelo menos um número.

# Não pode conter espaços em branco.

senha = "Admin1234"
digite_sua_senha = input("Digite sua senha: ")
if digite_sua_senha == senha :
    print("Acesso Liberado. Seja BEM VINDO!")
    
else:
    print("Senha Incorreta.")