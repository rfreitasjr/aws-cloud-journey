# Função 01: Receber uma lista de números e somá-los

# Imprimindo o cabeçalho:
print("\n" + "="*40 + "\n" + "1ª Função: Somar uma lista de números")
print("="*40)

def somar_lista(numeros):
    return sum(numeros)

# Lista de números:
lista01 = [10, 20, 30, 40]
resultado = somar_lista(lista01)

# Imprimir a lista e os resultados:
print ("\n" + "="*40)
print (f"Lista de números: {lista01}")
print("-"*40)
print (f"Soma: {resultado}")
print ("="*40 + "\n")


# Função 02: Receber uma lista e retornar o maior valor:

# Imprimindo o cabeçalho:
print("\n" + "="*60 + "\n" + "2ª Função: Identificar o maior número em uma lista")
print("="*60 + "\n")

#Determinar a função para extrair o maior valor:
def maior_valor(numeros):
    return max(numeros)

# Lista de números:
lista02 = [5, 12, 3, 99, 45]

# Determinar o resultado com a função e atribuir a uma variável:
resultado02 = maior_valor(lista02)

# Imprimindo o resultado:
print("\n" + "="*40)
print(f"A lista de números é: {lista02}")
print("-"*40 + "\n" + f"O maior número da lista é: {resultado02}")
print("="*40 + "\n")


# Função 03: Receber uma lista de números e filtrar os pares:

# Imprimir o cabeçalho:
print("\n" + "="*60)
print("3ª Função: Identificar os números pares em uma lista")
print("="*60 + "\n")

''' Sintaxe errada, precisou ser corrigida:
def filtrar_pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            pares = pares.append(n)  # ❌ ERRO AQUI!'''


# Determinar a função para filtrar os pares:
def filtrar_pares(numeros):
    pares =[]
    for n in numeros:
        if n %2 == 0:
            pares.append(n)
    return pares

''' Correções:
    1. Diminuída a identação do "return pares", para não ficar dentro do laço "for";
    2. A inicialização da lista "pares" foi transferida para dentro da função.
    3. "pares.append(n)", é uma função, não precisa ser atribuída a uma variável. '''

# Lista de números:
lista03 = [1, 2, 3, 4, 5, 6]

resultado03 = filtrar_pares(lista03)

# Imprimindo o resultado:
print("\n" + "="*40)
print(f"A lista de números é: {lista03}")
print("-"*40)
print(f"Os números pares da lista, são: {resultado03}")
print("\n" + "="*40)