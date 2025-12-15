# Função 01: Contar palavras em um texto

# Cabeçalho
print ("\n" + "*" * 40)
print ("1ª Função: Contar palavras")
print ("*" * 40 + "\n")

def contar_palavras(texto):
    texto_minusculo = texto.lower() # converte texto para minúsculo
    palavras = texto_minusculo.split() # separa o texto em minúsculo em palavras
    
    # Incializar o dicionario ==> {palavra:nº de ocorrências}
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem [palavra] += 1
        else:
            contagem [palavra] = 1
    return contagem

texto_teste = "O tempo passa, o vento venta, a vida é vento e o tempo voa."

resultado = contar_palavras(texto_teste)

print (f"Texto teste: \n {texto_teste}")
print (f"Contagem de palavras: {resultado}")


# Função 02: Filtrar dicionário por valor mínimo

print ("\n" + "=" * 60)
print ("# Função 02: Filtrar dicionário por valor mínimo")
print ("=" * 60 + "\n")
