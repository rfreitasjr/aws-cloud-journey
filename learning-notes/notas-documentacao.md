Anotações para documentar:

S3:
✏️ S3 é para armazenar arquivos estáticos
✏️ Você pode servir websites via S3
✏️ Preço é bem barato (alguns centavos/mês)
✏️ É altamente disponível (99.99% uptime)

EC2:
✏️ EC2 é para rodar aplicações (servidores web, bancos, etc)
✏️ Você escolhe tamanho da máquina (pequeno/grande)
✏️ Pode usar Linux ou Windows
✏️ Você controla segurança (quem conecta via SSH)
✏️ Preço varia conforme tamanho/tempo ligado

RDS:

✏️ RDS é gerenciado = AWS cuida de manutenção
✏️ Suporta MySQL, PostgreSQL, MariaDB, Oracle
✏️ Backup automático (você não se preocupa)
✏️ Multi-AZ = alta disponibilidade
✏️ Preço mais alto que EC2(mas você economiza em operação)

IAM:
✏️ IAM é CRÍTICO para segurança
✏️ Você cria usuários com permissões específicas
✏️ Princípio de "least privilege" (dar só o necessário)
✏️ Roles são usadas para Lambda, EC2, etc acessarem outros serviços
✏️ Access keys são como "senhas programáticas"

Cloudwatch:
✏️ CloudWatch é essencial para monitorar saúde
✏️ Você vê CPU, RAM, latência, requisições
✏️ Alarmes avisam quando algo anda errado
✏️ Logs ajudam a debugar problemas
✏️ Integra com SNS (envia email/SMS quando algo acontece)






