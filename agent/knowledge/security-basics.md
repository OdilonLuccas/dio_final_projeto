# Fundamentos de segurança da informação

Base de conhecimento para a skill `vulnerability-analysis`. Leia este arquivo quando a conversa envolver vulnerabilidades, riscos, ameaças ou boas práticas de segurança.

## Conceitos-chave

| Termo | O que é | Exemplo |
|-------|---------|---------|
| **Ativo** | Qualquer coisa que tem valor e precisa ser protegida: dado, sistema, servidor, conta. | O banco de usuários de um app. |
| **Vulnerabilidade** | Uma fraqueza no ativo que pode ser explorada. | Consulta SQL montada com texto digitado pela pessoa. |
| **Ameaça** | Algo ou alguém que pode explorar a fraqueza e causar dano. | Uma pessoa mal-intencionada na internet, ou um erro interno. |
| **Exploração (exploit)** | O ato, ou a técnica, de usar a vulnerabilidade. | Digitar uma entrada que altera a lógica do login. |
| **Risco** | A chance de uma ameaça explorar uma vulnerabilidade, combinada com o dano que isso causaria. | Risco = probabilidade x impacto. |
| **Superfície de ataque** | Tudo o que está exposto e pode ser alvo: portas, telas de login, APIs. | Servidor com SSH aberto para a internet. |
| **Controle** | Medida que reduz o risco: prevenir, detectar ou responder. | Consulta parametrizada, firewall, log de acesso. |
| **Risco residual** | O risco que sobra depois de aplicar os controles. | Ainda falta limitar tentativas de login. |

Analogia: a vulnerabilidade é uma janela sem trinco, a ameaça é quem passa pela rua olhando janelas, e o risco é a chance de alguém entrar multiplicada pelo prejuízo se entrar.

## A tríade CIA (confidencialidade, integridade, disponibilidade)

| Pilar | Pergunta | Quebra quando... |
|-------|----------|------------------|
| **Confidencialidade** | Só quem deve acessar, acessa? | Dados vazam ou alguém entra numa conta que não é dele. |
| **Integridade** | O dado é confiável e só muda por quem pode? | Registros são alterados ou apagados sem autorização. |
| **Disponibilidade** | O sistema está de pé quando precisam dele? | Serviço cai por ataque, falha ou falta de capacidade. |

Ao avaliar impacto, pergunte qual pilar é afetado e o quanto. Uma mesma falha pode afetar mais de um.

## Como avaliar: impacto, probabilidade, severidade

- **Impacto:** o dano se a falha for explorada. Considere os pilares da tríade, o tipo de dado (pessoal, financeiro, saúde) e o que o ambiente representa (laboratório ou produção).
- **Probabilidade:** a chance de acontecer. Depende da exposição (internet ou rede interna), da facilidade de explorar, de quem consegue chegar até o ativo e dos controles que já existem.
- **Severidade:** a combinação dos dois, para priorizar o que corrigir primeiro.

Escala usada nesta skill:

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|-------------------------|-------|-------|------|
| **Baixa** | Baixa | Baixa | Média |
| **Média** | Baixa | Média | Alta |
| **Alta** | Média | Alta | Crítica |

O **contexto muda a severidade**. A mesma falha num servidor de laboratório isolado e num servidor exposto à internet com dados reais não tem a mesma severidade. Por isso, pergunte o contexto antes de classificar.

Para quem quer se aprofundar: o **CVSS** é o padrão de mercado para pontuar a severidade de vulnerabilidades conhecidas (de 0 a 10). A matriz acima é uma versão simplificada, para estudo.

## Referências padronizadas

- **CWE** (Common Weakness Enumeration): catálogo de tipos de fraqueza. SQL Injection é a CWE-89.
- **CVE** (Common Vulnerabilities and Exposures): identificador de uma vulnerabilidade específica, num produto específico.
- **OWASP Top 10**: lista das categorias mais críticas de risco em aplicações web. A categoria *Injection* inclui o SQL Injection.
- **MITRE ATT&CK**: catálogo de táticas e técnicas usadas por atacantes, útil para descrever *como* uma falha seria explorada. SQL Injection numa aplicação exposta se encaixa em **T1190 (Exploit Public-Facing Application)**. Confirme o ID e o nome em https://attack.mitre.org antes de citar.

## Boas práticas defensivas

**Em código**
- Nunca monte comandos (SQL, shell, HTML) juntando entrada do usuário. Use consultas parametrizadas e APIs seguras.
- Valide a entrada no servidor (tipo, tamanho, formato), sem confiar no que vem do cliente.
- Guarde senhas com hash lento e salt (bcrypt, scrypt, Argon2). Nunca em texto puro.
- Não coloque segredos (senhas, chaves, tokens) no código nem no repositório.
- Mostre mensagens de erro genéricas para o usuário e registre o detalhe só no log.

**Em servidores e infraestrutura**
- Menor privilégio: cada conta e cada serviço com só o acesso de que precisa.
- Reduza a superfície: desligue serviços que não usa e feche portas desnecessárias.
- Mantenha o sistema e os pacotes atualizados.
- SSH com chave em vez de senha, sem login direto como root.
- Firewall com regra padrão de negar, liberando só o necessário.
- Faça backup e teste a restauração.
- Registre logs e olhe para eles.

**Em processo**
- **Defesa em profundidade:** várias camadas, para que uma falha só não derrube tudo.
- Revise a segurança antes de ir para produção, a cada alteração (ideia do DevSecOps).
- Valide a correção: depois de corrigir, teste de novo para confirmar que a falha acabou.
- Teste apenas sistemas seus ou com autorização por escrito.
