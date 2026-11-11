# 🛡️ dio-agent-appsec

> O [DIO Agent](https://github.com/digitalinnovationone/dio-agent) especializado em cibersegurança: um mentor que analisa uma vulnerabilidade com você do jeito que um profissional de segurança faria.

Projeto do desafio da DIO. Nenhum modelo foi treinado: o agente aprende **só pelo que está escrito nos arquivos** (uma skill, um arquivo de conhecimento e uma persona).

## 🎯 A especialização e por quê

Um chat comum responde direto. Um profissional de segurança faz o contrário: **entende o contexto, avalia o risco e só então orienta a correção**. A mesma falha pode ser irrelevante num laboratório isolado e crítica num servidor exposto com dados reais.

Por isso o agente foi especializado em **análise de vulnerabilidades (AppSec e infraestrutura)**, com este fluxo:

1. pergunta o contexto, uma pergunta por vez, antes de sugerir qualquer comando;
2. encontra a falha e explica a causa raiz (com CWE);
3. explica a exploração e cita a técnica do MITRE ATT&CK;
4. avalia **impacto, probabilidade e severidade**;
5. orienta a correção e **valida** com uma nova análise;
6. entrega um relatório sempre no mesmo formato.

Regras defensivas: só analisa o que é do estudante (laboratório ou com autorização), não cria ferramentas de ataque e começa os diagnósticos só com comandos de leitura.

## 🗂️ O que foi criado ou alterado

| Arquivo | Tipo | O que mudou |
|---------|------|-------------|
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | Skill (novo) | O roteiro que o agente segue, com `name` e `description`, regras defensivas e o formato do relatório |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | Skill (novo) | Explica a skill para pessoas |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | Conhecimento (novo) | Vulnerabilidade, ameaça, risco, tríade CIA, matriz de severidade e boas práticas |
| [`agent/persona.md`](agent/persona.md) | Persona (alterado) | Nova seção "Quando o assunto é segurança" |
| [`AGENTS.md`](AGENTS.md) | Definição do agente (alterado) | Linha na tabela de skills, arquivo de conhecimento listado e um limite de escopo em segurança |
| [`lab/app.py`](lab/app.py) | Laboratório (novo) | Login **propositalmente vulnerável** a SQL Injection |
| [`lab/app_corrigido.py`](lab/app_corrigido.py) | Laboratório (novo) | Versão com consulta parametrizada e senha com hash |
| [`lab/testar_login.py`](lab/testar_login.py) | Laboratório (novo) | Compara as duas versões com entradas de teste |
| [`docs/evidencias/README.md`](docs/evidencias/README.md) | Documentação (novo) | Roteiro de testes e prints |

O resto do repositório é o DIO Agent original.

## ▶️ Como rodar o agente no harness

1. **Instale o Hermes** pela [documentação oficial](https://hermes-agent.nousresearch.com/docs).
2. **Baixe o projeto:**
   ```bash
   git clone https://github.com/SEU-USUARIO/dio-agent-appsec.git
   cd dio-agent-appsec
   ```
3. **Abra o terminal na pasta do projeto** (a que tem o `AGENTS.md`) e rode:
   ```bash
   hermes
   ```
   Aberto em outra pasta, o Hermes não encontra os arquivos do agente.
4. **Converse.** Exemplos:
   - "Atue como especialista em AppSec. Analise o `lab/app.py`: encontre a falha, explique a exploração, cite a técnica do MITRE ATT&CK e reescreva o trecho afetado."
   - "Tenho um servidor Ubuntu de laboratório exposto na internet. Está seguro?"

Para ver a falha acontecendo sem o agente (só no seu computador, em memória):

```bash
python3 lab/testar_login.py
```

Resultado esperado: a versão `app.py` aceita entradas de SQL Injection e a `app_corrigido.py` as bloqueia.

## ⭐ A melhoria escolhida: análise sempre no mesmo formato

Escolhi fazer a análise **sair sempre no mesmo formato, com impacto, probabilidade e severidade**, para comparar casos.

- Escala fixa: impacto (Baixo, Médio, Alto), probabilidade (Baixa, Média, Alta) e uma **matriz 3x3** que gera a severidade (Baixa, Média, Alta, Crítica). Está em [`security-basics.md`](agent/knowledge/security-basics.md).
- Relatório com campos fixos, definido no Passo 7 do [`SKILL.md`](skills/vulnerability-analysis/SKILL.md).
- O contexto muda a severidade: o agente explica como ela mudaria se o ambiente fosse outro.

Assim, dois achados diferentes (um SQL Injection e um SSH aberto, por exemplo) podem ser colocados lado a lado e priorizados.

## 📸 Evidências

O roteiro dos testes e a lista de prints estão em [`docs/evidencias/README.md`](docs/evidencias/README.md). Os prints mostram a análise do `app.py`, as perguntas de contexto do agente e a comparação com um chat genérico.

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa vulnerabilidades como um profissional: pergunta o contexto, avalia impacto, probabilidade e severidade e orienta a correção | "Analise o `lab/app.py` e me diga a severidade da falha." |

## 🧪 Aviso

Tudo aqui é para estudo. O `lab/app.py` é vulnerável de propósito e roda só em memória, na sua máquina. Teste somente código e servidores seus, ou com autorização por escrito.

## 🙌 Créditos

Baseado no [DIO Agent](https://github.com/digitalinnovationone/dio-agent), da [DIO](https://dio.me).
