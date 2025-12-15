\# AWS EC2 — Laboratório de Instância e Acesso



\## Visão Geral

Este laboratório documenta a criação, configuração e validação de uma instância \*\*Amazon EC2\*\*, com foco em compreender o funcionamento de servidores virtuais na AWS, acesso remoto e análise de logs do sistema.



O laboratório faz parte da trilha prática do programa \*\*AWS re/Start\*\*, com comparação conceitual entre \*\*EC2 e AWS Lambda\*\*.



---



\## Objetivos do Laboratório

\- Criar uma instância EC2 via console AWS

\- Compreender os principais parâmetros de configuração

\- Acessar a instância e analisar logs do sistema

\- Avaliar quando utilizar EC2 ou Lambda



---



\## Criação da Instância EC2

A instância foi criada com as configurações básicas:



\- Tipo de instância adequado ao laboratório

\- Sistema operacional Linux

\- Configuração de rede padrão

\- Grupo de segurança permitindo acesso controlado



A evidência da criação da instância está registrada em:

assets/instancia\_ec2\_criada.png





---



\## Acesso e Verificação

Após a criação, foi realizado o acesso à instância para validação do funcionamento do sistema.



Foi analisado o \*\*System Log\*\*, que confirma:

\- Inicialização correta da instância

\- Carregamento do sistema operacional

\- Ausência de erros críticos



Evidência:

assets/instancia\_ec2\_criada.png





---



\## Acesso e Verificação

Após a criação, foi realizado o acesso à instância para validação do funcionamento do sistema.



Foi analisado o \*\*System Log\*\*, que confirma:

\- Inicialização correta da instância

\- Carregamento do sistema operacional

\- Ausência de erros críticos



Evidência:

assets/system\_log\_ec2\_instance.png





---



\## EC2 vs AWS Lambda

Foi elaborado um comparativo conceitual entre os dois serviços:



\- \*\*Amazon EC2\*\*: maior controle sobre o ambiente, indicado para workloads persistentes

\- \*\*AWS Lambda\*\*: execução sob demanda, sem gerenciamento de servidores



O comparativo completo está documentado em:

assets/AWS EC2-vs-AWS Lambda-comparacao.pdf





---



\## Conclusão

Este laboratório permitiu compreender:



\- O papel do EC2 como serviço de infraestrutura

\- A importância dos grupos de segurança e logs

\- Critérios de decisão entre EC2 e Lambda



A documentação reforça a base necessária para avançar em arquitetura, automação e otimização de custos na AWS.



---



\## Observações

Este módulo integra o repositório \*\*aws-cloud-journey\*\*, que documenta a evolução prática em computação em nuvem com foco em \*\*AWS, Cloud e DevOps\*\*.

