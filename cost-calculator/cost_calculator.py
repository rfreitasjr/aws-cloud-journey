"""
AWS EC2 Cost Calculator
Calculadora de custos mensais para instâncias EC2

Autor: Ricardo Altino de Freitas Jr
Data: 30/Novembro/2025
Repositório: github.com/rfreitasjr/aws-cloud-journey
"""

def calcular_custo_ec2(tipo_instancia, horas_mes, regiao="us-east-1"):
    """
    Calcula o custo mensal estimado de uma instância EC2
    
    Args:
        tipo_instancia (str): Tipo da instância (ex: t2.micro, t3.medium)
        horas_mes (int): Número de horas de uso no mês
        regiao (str): Região AWS (padrão: us-east-1)
    
    Returns:
        float: Custo estimado em USD, ou None se tipo inválido
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
    
    # Verificar se tipo de instância existe
    if tipo_instancia.lower() not in tabela_precos:
        return None
    
    # Calcular custo mensal
    preco_hora = tabela_precos[tipo_instancia.lower()]
    custo_mensal = preco_hora * horas_mes
    
    return round(custo_mensal, 2)


def exibir_tabela_precos():
    """Exibe tabela completa de preços disponíveis"""
    
    print("\n" + "="*60)
    print("TABELA DE PREÇOS EC2 - US-EAST-1")
    print("="*60)
    print(f"{'Tipo Instância':<15} {'Preço/Hora':<12} {'730h/mês':<12} {'Anual'}")
    print("-"*60)
    
    precos = {
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
    
    for tipo, preco_hora in precos.items():
        mensal = preco_hora * 730
        anual = mensal * 12
        print(f"{tipo:<15} ${preco_hora:<11.4f} ${mensal:<11.2f} ${anual:,.2f}")
    
    print("="*60)
    print("* Preços para uso contínuo 24/7 (730 horas/mês)")
    print("* Free Tier: t2.micro/t3.micro - 750h grátis/mês (primeiros 12 meses)")
    print("="*60 + "\n")


def exibir_comparacao_free_tier(tipo_instancia, horas_mes):
    """Exibe comparação com Free Tier da AWS"""
    
    # Tipos elegíveis para Free Tier
    free_tier_tipos = ['t2.micro', 't3.micro']
    free_tier_horas = 750  # horas grátis por mês
    
    if tipo_instancia.lower() in free_tier_tipos:
        if horas_mes <= free_tier_horas:
            print("\n" + "🎉 " * 20)
            print("✅ ESTA CONFIGURAÇÃO ESTÁ DENTRO DO FREE TIER!")
            print(f"   Você tem direito a {free_tier_horas}h grátis/mês de {tipo_instancia}")
            print(f"   Uso planejado: {horas_mes}h/mês")
            print(f"   Horas grátis restantes: {free_tier_horas - horas_mes}h")
            print("   Custo real: $0.00/mês (primeiros 12 meses)")
            print("🎉 " * 20 + "\n")
        else:
            horas_pagas = horas_mes - free_tier_horas
            custo_adicional = calcular_custo_ec2(tipo_instancia, horas_pagas)
            print("\n" + "⚠️ " * 20)
            print("⚠️  ATENÇÃO: Uso excede Free Tier")
            print(f"   Horas grátis: {free_tier_horas}h")
            print(f"   Horas pagas: {horas_pagas}h")
            print(f"   Custo adicional: ${custo_adicional}/mês")
            print("⚠️ " * 20 + "\n")
    else:
        print(f"\n❌ {tipo_instancia} NÃO é elegível para Free Tier")
        print(f"   Tipos Free Tier: {', '.join(free_tier_tipos)}\n")


def main():
    """Função principal - interface do usuário"""
    
    print("\n" + "="*60)
    print(" AWS EC2 COST CALCULATOR")
    print(" Calculadora de Custos de Instâncias EC2")
    print("="*60)
    print(" Autor: Ricardo Altino de Freitas Jr")
    print(" GitHub: github.com/rfreitasjr/aws-cloud-journey")
    print("="*60 + "\n")
    
    # Menu de opções
    while True:
        print("\nEscolha uma opção:")
        print("1 - Calcular custo de uma instância")
        print("2 - Ver tabela completa de preços")
        print("3 - Sair")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "1":
            # Calcular custo específico
            print("\n" + "-"*60)
            tipo = input("Digite o tipo de instância (ex: t2.micro): ").strip()
            
            try:
                horas = int(input("Digite as horas de uso por mês: "))
                
                if horas <= 0:
                    print("❌ Erro: Número de horas deve ser maior que zero")
                    continue
                
                custo = calcular_custo_ec2(tipo, horas)
                
                if custo is None:
                    print(f"\n❌ Erro: Tipo de instância '{tipo}' não encontrado")
                    print("   Use a opção 2 para ver tipos disponíveis")
                else:
                    print("\n" + "="*60)
                    print("RESULTADO DA ESTIMATIVA")
                    print("="*60)
                    print(f"Tipo de instância: {tipo}")
                    print(f"Horas de uso/mês:  {horas}h")
                    print(f"Custo mensal:      ${custo}")
                    print(f"Custo anual:       ${custo * 12:,.2f}")
                    print(f"Custo por hora:    ${custo/horas:.4f}")
                    print("="*60)
                    
                    # Verificar Free Tier
                    exibir_comparacao_free_tier(tipo, horas)
                    
            except ValueError:
                print("❌ Erro: Digite um número válido de horas")
            
        elif opcao == "2":
            # Exibir tabela completa
            exibir_tabela_precos()
            
        elif opcao == "3":
            # Sair
            print("\n" + "="*60)
            print("Obrigado por usar o AWS EC2 Cost Calculator!")
            print("="*60 + "\n")
            break
        
        else:
            print("❌ Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()