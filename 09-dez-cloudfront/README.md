# Lab: Amazon CloudFront - CDN & Origin Access Control

**Data**: 09/Dezembro/2025  
**Duração**: ~30 minutos  
**Dificuldade**: Iniciante

---

## 🎯 Objetivo

Criar uma distribuição CloudFront para servir conteúdo estático (imagem) armazenado em bucket S3, com acesso controlado via Origin Access Identity (OAI).

---

## 🏗️ Arquitetura Implementada
```
Usuário → CloudFront (Edge Location) → S3 Bucket (bloqueado publicamente)
         ↓
    Cache em Edge Location
    (carregamento mais rápido)
```

**Componentes**:
- **S3 Bucket**: `cfrfreitas1234` (origem privada)
- **CloudFront Distribution**: `d2eehg90ik3zd0.cloudfront.net`
- **OAI**: Identidade para CloudFront acessar S3 de forma segura
- **Edge Locations**: Servidores globais para cache

---

## ✅ O Que Foi Realizado

1. **Criação do S3 Bucket**
   - Bucket privado (Block all public access habilitado)
   - Upload de imagem de teste
   - Verificação de bloqueio (AccessDenied ao acessar diretamente)

2. **Configuração CloudFront**
   - Distribuição criada com origem S3
   - Origin Access Identity (OAI) configurado
   - WAF desabilitado (lab de aprendizado)
   - Domain name gerado: `d2eehg90ik3zd0.cloudfront.net`

3. **Teste de Funcionamento**
   - HTML criado referenciando CloudFront URL
   - Imagem carregada com sucesso via CloudFront
   - Segunda requisição mais rápida (cache funcionando)

---

## 📚 Conceitos Aprendidos

### Amazon CloudFront
- **CDN (Content Delivery Network)**: Rede global de servidores para entrega rápida de conteúdo
- **Edge Locations**: Pontos de presença próximos aos usuários
- **Cache**: Armazenamento temporário para reduzir latência
- **Origin**: Fonte original do conteúdo (neste caso, S3)

### Origin Access Control
- **OAI (Origin Access Identity)**: Método legado de controlar acesso
- **OAC (Origin Access Control)**: Evolução moderna do OAI
- **Diferenças**: Ver análise completa no PDF

### Segurança
- Bucket S3 privado (sem acesso público direto)
- Acesso apenas via CloudFront autenticado
- Princípio do menor privilégio aplicado

---

## 📂 Arquivos Neste Diretório

- `s3-bucket-criado.png` - Screenshot do bucket S3 configurado
- `cloudfront-criado.png` - Screenshot da distribuição CloudFront
- `OAI vs OAC - CloudFront.pdf` - Análise técnica comparativa (500 palavras)
- `funcoes-com-listas.py` - Exercício Python: 3 funções com listas
- `README.md` - Este arquivo

---

## 🔄 Como Reproduzir

### Pré-requisitos
- Conta AWS (ou AWS Sandbox)
- Imagem para teste (PNG ou JPG)

### Passo a Passo
```bash
# 1. Criar bucket S3
# Nome: cf<inicial><sobrenome><4números>
# Região: us-east-1 ou us-west-2
# Block all public access: HABILITADO

# 2. Upload de imagem no bucket

# 3. Criar distribuição CloudFront
# Origin: Selecionar o bucket S3 criado
# Origin Access: Usar OAI (ou OAC se disponível)
# WAF: Desabilitado (para lab)
# Aguardar deploy (5-10 minutos)

# 4. Testar acesso
# Criar HTML:
<html>
<head>CloudFront Test</head>
<body>
<img src="https://SEU_DOMAIN.cloudfront.net/SUA_IMAGEM.jpg">
</body>
</html>

# Abrir no navegador e verificar carregamento
```

---

## 💡 Aprendizados Principais

### Técnicos
- CloudFront reduz latência significativamente
- Cache em edge locations melhora performance
- OAI/OAC protege origem S3 de acesso direto
- Distribuições levam 5-10min para deploy

### Segurança
- **Nunca** deixar buckets S3 públicos desnecessariamente
- Usar OAC (não OAI) em implementações novas
- CloudFront pode integrar com WAF para proteção adicional
- Princípio: "Defense in depth" (múltiplas camadas)

### Boas Práticas
- Nomear recursos de forma descritiva
- Documentar configurações com screenshots
- Testar acesso direto vs via CDN
- Revisar custos (CloudFront cobra por transferência)

---

## 🐍 Exercício Python do Dia

Arquivo: `funcoes-com-listas.py`

**3 funções implementadas:**
1. `somar_lista()` - Soma todos os números de uma lista
2. `maior_valor()` - Retorna o maior número de uma lista
3. `filtrar_pares()` - Retorna apenas números pares de uma lista

**Conceitos praticados:**
- Definição de funções com `def`
- Parâmetros e retorno
- Listas e iteração
- Condicionais (`if`)
- Operador módulo (`%`)

---

## 🔗 Recursos Adicionais

- [Documentação CloudFront](https://docs.aws.amazon.com/cloudfront/)
- [OAI vs OAC - AWS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- [S3 + CloudFront: A Match Made in the Cloud](https://aws.amazon.com/blogs/aws/)

---

## 🎯 Próximos Passos

- [ ] Implementar OAC (ao invés de OAI)
- [ ] Adicionar custom domain (Route53)
- [ ] Configurar SSL/TLS (ACM)
- [ ] Integrar com AWS WAF
- [ ] Testar invalidação de cache
- [ ] Analisar logs de acesso (CloudWatch)

---

## 📊 Recursos Criados

| Recurso | Nome/ID | Região | Status |
|---------|---------|--------|--------|
| S3 Bucket | cfrfreitas1234 | us-west-2 | ✅ Criado |
| CloudFront Distribution | EG19XSBVYGOR4 | Global | ✅ Deployed |
| OAI | (gerado automaticamente) | - | ✅ Configurado |

---

## 📈 Tempo Investido

- **Lab AWS**: ~45 minutos
- **Documentação (PDF)**: ~1 hora
- **Exercício Python**: ~45 minutos
- **Screenshots e organização**: ~15 minutos

**Total**: ~2h 45min

---

**Lab concluído com sucesso!** ✅  

*Ricardo Freitas Jr - AWS re/Start Program - Semana 2*
