# Sua função aqui
def contar_letras(palavra):
    return len(palavra)


# Testando
fruta = input("Digite o nome de uma fruta: ")
comprimento_palavra = contar_letras(fruta)
print(f"A fruta {fruta} tem {comprimento_palavra} letras")

