# Lab: Introduction to Amazon EC2

**Data**: 12/Dezembro/2025  
**Duração**: ~1h  
**Dificuldade**: Iniciante

---

## 🎯 Objetivo

Compreender os fundamentos do Amazon EC2 através de um laboratório prático que aborda lançamento, configuração, monitoramento, redimensionamento e terminação de instâncias.

---

## 🏗️ Arquitetura Implementada
```
Internet → Security Group (HTTP:80) → EC2 Instance (Apache Web Server)
                                      ├── EBS Volume (10 GiB)
                                      └── CloudWatch Monitoring
```

**Componentes:**
- **EC2 Instance**: Web Server (t3.micro → t3.small)
- **AMI**: Amazon Linux 2023
- **Security Group**: Web Server security group (inbound HTTP)
- **EBS Volume**: Root volume expandido (8 GiB → 10 GiB)
- **User Data**: Script de instalação automática do Apache
- **Termination Protection**: Habilitado e testado

---

## ✅ O Que Foi Realizado

### 1. **Lançamento da Instância EC2**
- Instance Type: t3.micro (2 vCPUs, 1 GiB RAM)
- AMI: Amazon Linux 2023
- VPC: Lab VPC (Public Subnet 1)
- Security Group: Web Server security group
- Termination Protection: Habilitado
- User Data: Script de instalação do Apache

### 2. **Configuração do Web Server**
User Data script instalou automaticamente:
```bash
#!/bin/bash
dnf -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
```

### 3. **Monitoramento da Instância**
- Status Checks: System reachability ✅
- Instance reachability: ✅
- EBS reachability: ✅
- CloudWatch Metrics: Consultados
- System Log: Analisado (verificado instalação do httpd)
- Instance Screenshot: Capturado

### 4. **Configuração de Security Group**
- Regra inicial: Nenhuma (bloqueado)
- Regra adicionada: HTTP (port 80) from Anywhere (0.0.0.0/0)
- Resultado: Acesso web funcionando ✅

### 5. **Redimensionamento**
**Instance Type:**
- Original: t3.micro (2 vCPUs, 1 GiB)
- Novo: t3.small (2 vCPUs, 2 GiB) ✅

**EBS Volume:**
- Original: 8 GiB
- Novo: 10 GiB ✅

**Processo:**
1. Stop instance
2. Change instance type
3. Modify EBS volume
4. Start instance

### 6. **Termination Protection**
- Primeira tentativa: Bloqueado (proteção ativa) ✅
- Proteção desabilitada
- Segunda tentativa: Sucesso ✅
- Instância terminada

---

## 📚 Conceitos Aprendidos

### Amazon EC2
- **Elastic Compute Cloud**: Capacidade computacional redimensionável na nuvem
- **Instance Types**: Combinações de CPU, memória, storage e rede
- **AMI (Amazon Machine Image)**: Template para o sistema operacional
- **User Data**: Scripts executados no boot da instância
- **Elastic IP**: IPs públicos (não usado neste lab)

### Security Groups
- **Firewall virtual**: Controla tráfego de entrada/saída
- **Stateful**: Regras de retorno automáticas
- **Port 80 (HTTP)**: Necessário para web servers
- **0.0.0.0/0**: Anywhere (não recomendado para produção!)

### Monitoramento
- **CloudWatch**: Métricas de performance
- **System Log**: Output do console (troubleshooting)
- **Instance Screenshot**: Visão do console virtual
- **Status Checks**: System e Instance reachability

### EBS (Elastic Block Store)
- **Root Volume**: Disco de boot da instância
- **Redimensionamento**: Pode ser expandido (não diminuído)
- **Attached to instance**: Sobrevive ao stop (não ao terminate)

### Termination Protection
- **Safeguard**: Previne terminação acidental
- **Modificável**: Pode ser habilitado/desabilitado
- **Importante**: Sempre habilitar em produção!

---

## 📂 Arquivos Neste Diretório

- `instancia_ec2_criada.png` - Screenshot da instância criada
- `system_log_ec2_instance.png` - System log mostrando boot e instalação
- `README.md` - Este arquivo

---

## 🔄 Como Reproduzir

### Pré-requisitos
- Conta AWS (ou AWS Sandbox)
- VPC com subnet pública

### Passo a Passo
```bash
# 1. Lançar instância EC2
# - AMI: Amazon Linux 2023
# - Instance Type: t3.micro
# - VPC: Lab VPC / Public Subnet
# - Security Group: Criar novo (permitir SSH se necessário)
# - User Data: Script de instalação do Apache
# - Termination Protection: Enable

# 2. Aguardar Status Checks (3/3 passed)

# 3. Configurar Security Group
# - Adicionar regra: HTTP (port 80) from Anywhere

# 4. Testar acesso web
# - Copiar Public IPv4 address
# - Acessar: http://[IP-PUBLICO]
# - Verificar: "Hello From Your Web Server!"

# 5. Redimensionar (opcional)
# - Stop instance
# - Actions → Instance Settings → Change instance type
# - Actions → Elastic Block Store → Modify volume
# - Start instance

# 6. Terminar instância
# - Desabilitar Termination Protection
# - Actions → Instance State → Terminate
```

---

## 💡 Aprendizados Principais

### Técnicos
- EC2 é o serviço fundamental de compute da AWS
- User Data permite automação no boot
- Security Groups funcionam como firewall stateful
- Instâncias podem ser redimensionadas (requer stop)
- EBS volumes podem ser expandidos (não diminuídos)
- CloudWatch fornece métricas detalhadas

### Segurança
- **Sempre** usar Security Groups restritivos
- 0.0.0.0/0 é aceitável para labs, **não para produção**
- Termination Protection é crucial em produção
- System Logs ajudam em troubleshooting
- Status Checks monitoram saúde da instância

### Boas Práticas
- Nomear recursos descritivamente
- Usar tags para organização
- Habilitar Termination Protection em produção
- Monitorar custos (EC2 cobra por hora)
- Parar instâncias quando não estiverem em uso
- Documentar configurações com screenshots

### Custos
- **Running instance**: Cobra por hora
- **Stopped instance**: Não cobra compute, apenas EBS
- **Terminated instance**: Não cobra nada
- **EBS**: Cobra por GiB/mês (mesmo stopped)

---

## 🔗 Recursos Adicionais

- [Launch Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [User Data and Shell Scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [CloudWatch Metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)

---

## 🎯 Próximos Passos

- [ ] Conectar via SSH (requer Key Pair)
- [ ] Configurar Elastic IP (IP público fixo)
- [ ] Implementar Auto Scaling
- [ ] Configurar Load Balancer
- [ ] Integrar com RDS (banco de dados)
- [ ] Implementar backup automatizado (snapshots)

---

## 📊 Recursos Criados

| Recurso | Especificação | Região | Status |
|---------|---------------|--------|--------|
| EC2 Instance | t3.micro → t3.small | us-west-2 | ✅ Terminada |
| EBS Volume | 8 GiB → 10 GiB | us-west-2 | ✅ Terminada |
| Security Group | Web Server SG (HTTP:80) | us-west-2 | ✅ Criado |
| Public IP | 44.244.55.208 (exemplo) | - | ✅ Liberado |

---

## 📈 Tempo Investido

- **Lab EC2**: ~1h
- **Documentação**: ~30min (em andamento)
- **Screenshots**: ~5min

**Total**: ~1h 35min

---

**Lab concluído com sucesso!** ✅  

*Ricardo Freitas Jr - AWS re/Start Program - Semana 2 - Sexta 12/Dez*
