# Minha Primeira Função
# Data: 05/12/2025

# Função 1: Simples (Sem entrada, sem saída)
def dizer_ola():
    print("Olá mundo!")

# Testando função 1
dizer_ola()
dizer_ola()
dizer_ola()

print("\n" + "="*40 + "\n")

# Função 2: Com entrada (parâmetro)
def saudar(nome):
    print(f"Olá, {nome}!")

# Testando função 2
saudar("Ricardo")
saudar("Maria")
saudar("AWS")

print("\n" + "="*40 + "\n")

# Função 3: Com entrada e saída (return)
def somar_dois_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# Testando função 3
soma = somar_dois_numeros(5,3)
print(f"5 + 3 = {soma}")

soma2 = somar_dois_numeros(10,20)
print(f"10 + 20 = {soma2}")

print("\n" + "="*40 + "\n")

#Função 4: Mais complexa
def calcular_idade(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade

# Testando função 4
idade_ricardo = calcular_idade(1972)
print(f"Se você nasceu em 1972, tem {idade_ricardo} anos")

idade_joao = calcular_idade(1995)
print(f"Se você nasceu em 1995, tem {idade_joao} anos")
