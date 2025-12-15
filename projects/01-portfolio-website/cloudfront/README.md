\# CloudFront — Distribuição de Conteúdo do Portfólio



\## Visão Geral

Este módulo documenta a implementação do \*\*Amazon CloudFront\*\* como camada de distribuição de conteúdo para o site estático do portfólio pessoal, hospedado em um bucket Amazon S3.



O objetivo foi aplicar boas práticas de \*\*segurança, performance e arquitetura cloud\*\*, conforme os laboratórios do programa \*\*AWS re/Start\*\*.



---



\## Arquitetura da Solução

A arquitetura utilizada é composta pelos seguintes serviços:



\- \*\*Amazon S3\*\*: armazenamento do site estático

\- \*\*Amazon CloudFront\*\*: CDN para distribuição global de conteúdo

\- \*\*Origin Access Control (OAC)\*\*: controle de acesso seguro ao bucket S3



O CloudFront atua como ponto de entrada, garantindo baixa latência, cache eficiente e acesso restrito ao bucket de origem.



---



\## Controle de Acesso: OAI vs OAC

Durante o laboratório, foi analisada a diferença entre os dois mecanismos de controle de acesso do CloudFront:



\- \*\*OAI (Origin Access Identity)\*\*: modelo legado

\- \*\*OAC (Origin Access Control)\*\*: modelo atual e recomendado pela AWS



A implementação final utiliza \*\*OAC\*\*, por oferecer:

\- Melhor integração com políticas IAM

\- Maior segurança

\- Suporte às arquiteturas modernas da AWS



O comparativo completo está documentado em:

assets/OAI vs OAC - CloudFront.pdf





---



\## Evidências da Implementação

Os seguintes artefatos comprovam a configuração e funcionamento da solução:



\- Criação do bucket S3  

&nbsp; `assets/s3-bucket-criado.png`



\- Criação da distribuição CloudFront  

&nbsp; `assets/cloudfront-criado.png`



---



\## Resultado Final

A solução permite:



\- Distribuição global do site com baixa latência

\- Proteção do bucket S3 contra acesso público direto

\- Estrutura alinhada às boas práticas de segurança da AWS

\- Base sólida para evolução futura (HTTPS, WAF, CI/CD)



---



\## Observações

Este módulo faz parte do repositório \*\*aws-cloud-journey\*\*, que documenta a evolução prática em computação em nuvem, com foco em \*\*Cloud, DevOps e Arquitetura AWS\*\*.

