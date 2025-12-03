# AWS EC2 Cost Calculator

![Python](https://img.shields.io/badge/Python-3.14-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)

## 📋 Sobre

Calculadora de custos mensais para instâncias EC2 da AWS, desenvolvida para praticar Python e entender o modelo de precificação da AWS.

**Autor:** Ricardo Altino de Freitas Jr  
**Data:** 30/Novembro/2025  
**Repositório:** [aws-cloud-journey](https://github.com/rfreitasjr/aws-cloud-journey)

---

## 🎯 Objetivo

Este script foi criado como parte do meu aprendizado no programa AWS re/Start para:
- Praticar Python básico (funções, loops, input/output)
- Entender modelo de precificação AWS EC2
- Calcular custos antes de provisionar recursos
- Identificar oportunidades de Free Tier

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado
- Nenhuma biblioteca externa necessária (usa apenas Python padrão)

### Executar
```bash
python cost_calculator.py
```

### Opções Disponíveis

**1. Calcular custo de uma instância**
- Digite o tipo (ex: t2.micro, t3.medium)
- Digite as horas de uso mensal
- Receba estimativa de custo + verificação de Free Tier

**2. Ver tabela completa de preços**
- Exibe todos os tipos de instância disponíveis
- Preços por hora, mensal e anual
- Informações sobre Free Tier

**3. Sair**
- Encerra o programa

---

## 💰 Tipos de Instância Suportados

### Família T2 (Burstable Performance)
- `t2.micro` - $0.0116/hora
- `t2.small` - $0.0232/hora
- `t2.medium` - $0.0464/hora
- `t2.large` - $0.0928/hora

### Família T3 (Burstable Performance - Geração Atual)
- `t3.micro` - $0.0104/hora
- `t3.small` - $0.0208/hora
- `t3.medium` - $0.0416/hora
- `t3.large` - $0.0832/hora
- `t3.xlarge` - $0.1664/hora
- `t3.2xlarge` - $0.3328/hora

*Preços para região us-east-1 (N. Virginia)*

---

## 🎁 AWS Free Tier

**Instâncias elegíveis:**
- t2.micro
- t3.micro

**Benefício:**
- 750 horas/mês grátis
- Válido por 12 meses após criar conta AWS
- Se usar 24/7 = 730h/mês = dentro do Free Tier!

**O script automaticamente:**
- ✅ Detecta se sua configuração está no Free Tier
- ✅ Calcula horas grátis restantes
- ✅ Avisa se exceder o limite

---

## 📊 Exemplos de Uso

### Exemplo 1: Site pessoal (sempre ligado)
```
Tipo: t2.micro
Horas: 730 (24/7 por 30 dias)
Resultado: $8.47/mês
Status: ✅ FREE TIER (primeiros 12 meses)
```

### Exemplo 2: Ambiente de desenvolvimento (8h/dia útil)
```
Tipo: t3.medium
Horas: 160 (8h × 20 dias úteis)
Resultado: $6.66/mês
Status: ❌ Não elegível para Free Tier
```

### Exemplo 3: Servidor de produção (sempre ligado)
```
Tipo: t3.large
Horas: 730
Resultado: $60.74/mês ($728.88/ano)
Status: ❌ Não elegível para Free Tier
```

---

## 🧠 Conceitos AWS Aprendidos

### 1. Modelo de Precificação On-Demand
- Pagamento por hora de uso
- Sem compromisso de longo prazo
- Pode ligar/desligar quando quiser

### 2. Famílias de Instâncias
- **T2/T3:** Uso geral, burstable (ideal para workloads variáveis)
- Outras famílias: C (compute), M (memory), R (RAM), etc.

### 3. Free Tier
- 750h/mês de t2.micro ou t3.micro
- Suficiente para 1 instância 24/7
- Renovado mensalmente durante 12 meses

### 4. Otimização de Custos
- Desligar instâncias quando não usar
- Escolher tipo adequado ao workload
- Usar Reserved Instances para descontos (não implementado neste script)

---

## 🔄 Melhorias Futuras

- [ ] Adicionar mais tipos de instância (C5, M5, R5, etc.)
- [ ] Suporte para múltiplas regiões AWS
- [ ] Integração com AWS Price List API (preços em tempo real)
- [ ] Calcular custos de storage (EBS)
- [ ] Calcular custos de data transfer
- [ ] Comparar Reserved Instances vs On-Demand
- [ ] Exportar resultados para CSV
- [ ] Interface gráfica (GUI)

---

## 📚 Recursos Utilizados

- [AWS EC2 Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [Python Documentation](https://docs.python.org/3/)

---

## 🤝 Contribuições

Este é um projeto de aprendizado pessoal, mas sugestões são bem-vindas!

Abra uma issue no repositório: [aws-cloud-journey](https://github.com/rfreitasjr/aws-cloud-journey/issues)

---

## 📝 Licença

MIT License - Livre para usar e modificar

---

**Desenvolvido durante o programa AWS re/Start | Escola da Nuvem**  
**Parte do portfólio:** [github.com/rfreitasjr/aws-cloud-journey](https://github.com/rfreitasjr/aws-cloud-journey)