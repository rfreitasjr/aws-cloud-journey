"""
AWS EC2 Cost Calculator
Calculadora de custos mensais para instâncias EC2

Autor: Ricardo Altino de Freitas Jr
Data: 30/Novembro/2025
Repositório: github.com/rfreitasjr/aws-cloud-journey
"""

# Tabela de preços simplificada (região us-east-1)
# Preços por hora em USD (atualizados em Nov/2025)
tabela_precos = {
    't2.micro': 0.0116,
    't2.small': 0.0232,
    't2.medium': 0.0464,
    't2.large': 0.0928,
    't3.micro': 0.0104,
    't3.small': 0.0208,
    't3.medium': 0.0416,
    't3.large': 0.0832,
    't3.xlarge': 0.1664,
    't3.2xlarge': 0.3328,
}


print("\n" + "=" * 60)
print("AWS EC2 COST CALCULATOR")
print("=" * 60)
print("Autor: Ricardo Altino de Freitas Jr.")
print("GitHub: github.com/rfreitasjr/aws-cloud-journey")
print("=" * 60 + "\n")

while True:

    print("\n" + "Escolha uma opção:")
    print("1 - Calcular custo de uma instância")
    print("2 - Ver tabela completa de preços")
    print("3 - Sair" "\n")
    opcao = input("Opção:")

    if opcao == "1":
        print("\n" + "-" * 60)
        tipo_instancia = input("Digite o tipo de instância (ex: t2.micro): ").lower()

        if tipo_instancia in tabela_precos:
            horas_uso_mes = float(input("Digite as horas de uso por mês: "))
    
            # Busca o preço por hora no dicionário:
            preco_por_hora = tabela_precos[tipo_instancia]
    
            # Calcula o custo mensal:
            custo_mensal = preco_por_hora * horas_uso_mes

            # Calcula o custo anual:
            custo_anual = custo_mensal * 12

            print("\n" + "=" * 60)
            print("RESULTADO DA ESTIMATIVA")
            print("\n" + "=" * 60)
            print(f"Tipo de instância:\t{tipo_instancia}")
            print(f"Horas de uso/mês:\t {horas_uso_mes}")
            print(f"Custo mensal:\t {custo_mensal}")
            print(f"Custo anual:\t{custo_anual}")
            print(f"Custo por hora:\t{preco_por_hora}")
            print("\n" + "=" * 60)

        # Verifica se o uso excede o Free Tier    
        if horas_uso_mes >= 750:
            print("\n" + "⚠️ " * 20)
            print("ATENÇÃO: Uso excede Free Tier")
            print("Horas grátis: 750h")
            print(f"Horas pagas: {horas_uso_mes - 750}h")
            print(f"Custo adicional: {(horas_uso_mes - 750) * preco_por_hora}")
            print("\n" + "⚠️ " * 20)
        else:
            print("\n" + "🎉 " * 30)
            print("✅ ESTA CONFIGURAÇÃO ESTÁ DENTRO DO FREE TIER!")
            print(f"Você tem direito a 750h grátis/mês de {tipo_instancia}")
            print(f"Uso planejado: {horas_uso_mes}h/mês")
            print(f"Horas grátis restantes: {750 - horas_uso_mes}")
            print(f"Custo real: $0/mês (primeiros 12 meses)")
            print("🎉 " * 30)
    elif opcao == "2":
        print("\n" + "=" * 60)
        print("TABELA DE PREÇOS EC2 - US-EAST-1")
        print("\n" + "=" * 60)
        print("Tipo Instância\tPreço/Hora\t730h/mês\tAnual")
        print("-" * 60)
        print("t2.micro\t$0.0116\t\t$8.47\t\t$101.62")
        print("t2.small\t$0.0232\t\t$16.94\t\t$203.23")
        print("t2.medium\t$0.0464\t\t$33.87\t\t$406.46")
        print("t2.large\t$0.0928\t\t$67.74\t\t$812.93")
        print("t3.micro\t$0.0104\t\t$7.59\t\t$91.10")
        print("t3.small\t$0.0208\t\t$15.18\t\t$182.21")
        print("t3.medium\t$0.0416\t\t$30.37\t\t$364.42")
        print("t3.large\t$0.0832\t\t$60.74\t\t$728.83")
        print("t3.xlarge\t$0.1664\t\t$121.47\t\t$1,457.66")
        print("t3.2xlarge\t$0.3328\t\t$242.94\t\t$2,915.33")
        print("\n" + "=" * 60)
        print("* Preços para uso contínuo 24/7 (730 horas/mês)")
        print("* Free Tier: t2.micro/t3.micro - 750h grátis/mês (primeiros 12 meses)")
        print("=" * 60 + "\n")

    elif opcao == "3":
        break

    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")

