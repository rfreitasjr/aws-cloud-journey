# Projeto 1: Portfolio Website - Static Site on AWS

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20CloudFront%20%7C%20Route53-orange)

## 📋 Visão Geral

Website estático de portfólio pessoal hospedado na AWS, demonstrando arquitetura serverless básica com foco em performance, segurança e otimização de custos.

**Objetivo do projeto:**  
Criar uma aplicação web simples mas profissional que demonstre conhecimento prático de:
- Hospedagem estática na nuvem (S3)
- Distribuição de conteúdo global (CloudFront CDN)
- Segurança (HTTPS, certificados SSL)
- Otimização de custos (arquitetura serverless)

---

## 📅 Timeline

| Fase | Descrição | Status | Data |
|------|-----------|--------|------|
| 1 | Documentação e planejamento | ✅ Concluído | 29/Nov/2025 |
| 2 | Criação do site (HTML/CSS/JS) | 🔄 Em progresso | 30/Nov-07/Dez |
| 3 | Deploy no S3 + configuração | 📋 Planejado | 08-10/Dez |
| 4 | CloudFront + SSL/HTTPS | 📋 Planejado | 11-13/Dez |
| 5 | Otimizações finais | 📋 Planejado | 14-15/Dez |

---

## 🏗️ Arquitetura

### Diagrama
```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │ HTTPS (443)
       ▼
┌─────────────────────────────┐
│    Amazon CloudFront        │ ◄─── Certificado SSL (ACM)
│  (CDN - Global Distribution)│
└─────────────┬───────────────┘
              │
              ▼
┌──────────────────────────────┐
│      Amazon S3 Bucket        │
│  (Website Hosting Enabled)   │
│   - index.html               │
│   - css/                     │
│   - js/                      │
│   - assets/                  │
└──────────────┬───────────────┘
              │
              ▼
┌──────────────────────────────┐
│      Amazon Route 53         │ (Futuro - quando tiver domínio)
│   (DNS Management)           │
└──────────────────────────────┘
```

### Componentes Detalhados

#### 1. Amazon S3 (Simple Storage Service)
**Função:** Armazenar arquivos estáticos (HTML, CSS, JS, imagens)

**Configurações:**
- Bucket configurado para "Static Website Hosting"
- Versionamento habilitado (rollback em caso de problema)
- Bucket policy para acesso apenas via CloudFront (não público direto)
- Lifecycle policy: mover versões antigas para Glacier após 90 dias

**Custo estimado:** ~$0.023/GB/mês (Free Tier: 5GB grátis nos primeiros 12 meses)

---

#### 2. Amazon CloudFront
**Função:** CDN (Content Delivery Network) para distribuição global rápida

**Benefícios:**
- Latência baixa (edge locations próximas aos usuários)
- Cache inteligente (menos requisições ao S3 = menor custo)
- HTTPS obrigatório (segurança)
- Compressão automática (Gzip/Brotli)

**Configurações:**
- Origin: S3 bucket (via OAI - Origin Access Identity)
- TTL (Time to Live): 24h para assets estáticos, 5min para HTML
- Comportamento de cache customizado por tipo de arquivo
- HTTP → HTTPS redirect automático
- Geo-restriction: nenhuma (site global)

**Custo estimado:** Free Tier - 1TB transferência/mês grátis no primeiro ano

---

#### 3. AWS Certificate Manager (ACM)
**Função:** Certificado SSL/TLS gratuito para HTTPS

**Características:**
- Renovação automática (sem preocupação com expiração)
- Validação via DNS (Route 53) ou email
- Suporte SNI (Server Name Indication)
- Custo: **$0** (gratuito para uso com CloudFront)

---

#### 4. Amazon Route 53 *(implementação futura)*
**Função:** Gerenciamento de DNS para domínio customizado

**Custo estimado:** $0.50/mês (hosted zone)

---

## 💰 Análise de Custos

### Estimativa Mensal (site com 1000 visitantes/mês)

| Serviço | Uso | Cálculo | Custo Mensal |
|---------|-----|---------|--------------|
| **S3 Storage** | 1GB de arquivos | 1GB × $0.023 | $0.023 |
| **S3 Requests** | 10,000 GET | 10k × $0.0004/1000 | $0.004 |
| **CloudFront** | 10GB data transfer | Free Tier | $0.00 |
| **ACM** | Certificado SSL | Grátis com CloudFront | $0.00 |
| **Route 53** | Hosted zone | (futuro) | $0.50 |
| **TOTAL SEM DOMÍNIO** | | | **~$0.03/mês** |
| **TOTAL COM DOMÍNIO** | | | **~$0.53/mês** |

**Observações:**
- Free Tier CloudFront: 1TB/mês grátis no primeiro ano
- Custo real é praticamente ZERO nos primeiros 12 meses
- Mesmo após Free Tier, custo é mínimo (< $1/mês)

### Comparação com Alternativas

| Solução | Custo Mensal | Complexidade |
|---------|--------------|--------------|
| **AWS Serverless** (este projeto) | $0.03 - $0.53 | Baixa |
| Netlify Free | $0 | Muito baixa |
| Vercel Free | $0 | Muito baixa |
| VPS (DigitalOcean) | $5-10 | Média-Alta |
| Shared Hosting | $3-10 | Baixa |

**Por que escolher AWS mesmo com alternativas gratuitas?**
- ✅ Aprendizado prático de serviços AWS reais
- ✅ Demonstra conhecimento de arquitetura cloud
- ✅ Escalável (suporta tráfego massivo se necessário)
- ✅ Diferencial em entrevistas (não é "só Netlify")

---

## 🔧 Stack Tecnológica

**Frontend:**
- HTML5 (estrutura semântica)
- CSS3 (Flexbox/Grid, animações)
- JavaScript Vanilla (sem frameworks - manter simples)

**Cloud Infrastructure:**
- Amazon S3 (storage)
- Amazon CloudFront (CDN)
- AWS Certificate Manager (SSL)
- Amazon Route 53 (DNS - futuro)

**Ferramentas:**
- Git/GitHub (versionamento)
- AWS CLI (automação de deploy)
- Draw.io (diagramas de arquitetura)

**Future Enhancement:**
- CloudFormation (Infrastructure as Code)
- GitHub Actions (CI/CD automatizado)

---

## 📁 Estrutura do Projeto
```
01-portfolio-website/
│
├── README.md                    # Este arquivo (documentação completa)
│
├── docs/                        # Documentação adicional
│   ├── architecture.png         # Diagrama visual da arquitetura
│   ├── setup-guide.md          # Guia passo a passo de implementação
│   ├── cost-analysis.md        # Análise detalhada de custos
│   └── security-notes.md       # Considerações de segurança
│
├── src/                        # Código fonte do website
│   ├── index.html              # Página principal
│   ├── about.html              # Página sobre mim
│   ├── projects.html           # Página de projetos
│   ├── contact.html            # Página de contato
│   │
│   ├── css/
│   │   ├── style.css           # Estilos principais
│   │   ├── responsive.css      # Media queries
│   │   └── animations.css      # Animações CSS
│   │
│   ├── js/
│   │   ├── main.js             # JavaScript principal
│   │   └── form-handler.js     # Manipulação de formulário
│   │
│   └── assets/
│       ├── images/             # Imagens do site
│       ├── icons/              # Ícones SVG
│       └── resume.pdf          # Currículo para download
│
├── cloudformation/             # (Futuro) Templates IaC
│   └── infrastructure.yaml     # Template completo da infra
│
└── scripts/                    # Scripts de automação
    ├── deploy.sh               # Script de deploy para S3
    ├── invalidate-cache.sh     # Invalidar cache CloudFront
    └── sync-s3.sh              # Sync local → S3
```

---

## 🚀 Como Implementar (Guia Rápido)

### Pré-requisitos
- [x] Conta AWS (Free Tier)
- [x] AWS CLI instalado e configurado
- [ ] Conhecimento básico de HTML/CSS
- [ ] Git instalado

### Passo a Passo Simplificado

#### 1. Criar Bucket S3
```bash
# Criar bucket (nome deve ser único globalmente)
aws s3 mb s3://portfolio-ricardo-freitas

# Configurar para website hosting
aws s3 website s3://portfolio-ricardo-freitas \
  --index-document index.html \
  --error-document error.html
```

#### 2. Fazer Upload dos Arquivos
```bash
# Sync pasta local com S3
cd src/
aws s3 sync . s3://portfolio-ricardo-freitas

# Verificar upload
aws s3 ls s3://portfolio-ricardo-freitas
```

#### 3. Configurar Bucket Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::portfolio-ricardo-freitas/*"
    }
  ]
}
```

#### 4. Criar Distribuição CloudFront
```bash
# Via console AWS ou CLI
aws cloudfront create-distribution \
  --origin-domain-name portfolio-ricardo-freitas.s3-website-us-east-1.amazonaws.com \
  --default-root-object index.html
```

**Documentação detalhada:** Ver [docs/setup-guide.md](./docs/setup-guide.md) *(a criar)*

---

## 🔐 Considerações de Segurança

### Implementadas
- ✅ Bucket S3 NÃO é público diretamente
- ✅ Acesso ao S3 APENAS via CloudFront (OAI - Origin Access Identity)
- ✅ HTTPS obrigatório (redirecionamento HTTP → HTTPS)
- ✅ Versionamento habilitado (histórico de mudanças)
- ✅ Certificado SSL/TLS válido (ACM)

### Não Aplicáveis (site estático público)
- ❌ Sem autenticação de usuários (conteúdo público intencional)
- ❌ Sem dados sensíveis armazenados
- ❌ Sem backend/API para proteger

### Melhorias Futuras
- [ ] AWS WAF (Web Application Firewall) - se houver formulário de contato
- [ ] CloudFront signed URLs - se adicionar conteúdo premium
- [ ] AWS Shield Standard (já incluído gratuitamente)

---

## 📚 Aprendizados

### O que aprendi documentando este projeto:
- ✅ Diferença entre S3 website hosting e distribuição via CloudFront
- ✅ Importância de OAI (Origin Access Identity) para segurança
- ✅ Como estruturar arquitetura serverless para custos mínimos
- ✅ Planejamento de projetos com documentação técnica detalhada

### Desafios esperados na implementação:
- ⚠️ Configuração correta de cache policies no CloudFront
- ⚠️ Propagação de DNS (pode levar 24-48h)
- ⚠️ Invalidação de cache (estratégia para updates rápidos)

### Próximos aprendizados (pós-implementação):
- [ ] CloudFormation para automação completa (IaC)
- [ ] CI/CD com GitHub Actions (deploy automático)
- [ ] Monitoramento com CloudWatch (métricas de acesso)
- [ ] Lambda@Edge para otimizações avançadas

---

## 🔗 Links Úteis

### Documentação Oficial AWS
- [S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)
- [ACM User Guide](https://docs.aws.amazon.com/acm/latest/userguide/)

### Tutoriais e Artigos
- [AWS Well-Architected - Static Websites](https://wa.aws.amazon.com/wat.pillar.performance.en.html)
- [CloudFront Cache Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/)

### Ferramentas
- [AWS Pricing Calculator](https://calculator.aws/)
- [Draw.io](https://app.diagrams.net/) - Diagramas de arquitetura

---

## 📝 Checklist de Conclusão

Projeto será considerado completo quando:

### Implementação
- [ ] Site criado (HTML/CSS/JS)
- [ ] Bucket S3 configurado
- [ ] CloudFront distribuição ativa
- [ ] HTTPS funcionando
- [ ] Site acessível globalmente

### Documentação
- [x] README completo (este arquivo)
- [ ] Diagrama de arquitetura visual
- [ ] Setup guide detalhado
- [ ] Screenshots do site e console AWS
- [ ] Post no LinkedIn sobre o projeto

### Código
- [ ] Código fonte no GitHub
- [ ] Comentários explicativos
- [ ] Script de deploy automatizado
- [ ] Testes de responsividade (mobile/desktop)

### Performance
- [ ] Lighthouse score 90+ (performance)
- [ ] Tempo de carregamento < 2s
- [ ] Assets otimizados (imagens comprimidas)

---

## 🎯 Próximos Passos (Pós-Implementação)

1. **CloudFormation Template**
   - Converter toda infraestrutura para código (IaC)
   - Permitir deploy/destroy completo via CLI

2. **CI/CD Pipeline**
   - GitHub Actions para deploy automático
   - Push para main → deploy automático no S3

3. **Formulário de Contato**
   - Adicionar Lambda + API Gateway + SES
   - Processar submissões sem backend tradicional

4. **Analytics**
   - Implementar CloudWatch Logs
   - Dashboard de visitantes/performance

---

## 👨‍💻 Autor

**Ricardo Altino de Freitas Jr**  
Cloud Engineering Student | AWS re/Start Program

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/ricardo-freitas-jr-cloud-ia)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github)](https://github.com/rfreitasjr)

---

**Status:** 🔄 Documentação completa | Implementação iniciando  
**Última atualização:** 29/Novembro/2025
```
