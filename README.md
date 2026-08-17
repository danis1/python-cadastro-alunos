# 🎓 Sistema de Cadastro de Alunos e Turma

Projeto prático desenvolvido para a disciplina de **Desenvolvimento de Software 3** do curso de **Desenvolvimento de Software Multiplataforma (DSM)** na **Fatec Praia Grande**.

---

## 📌 Sobre o Projeto

O sistema é uma aplicação de linha de comando (CLI) em Python criada para demonstrar o uso e a manipulação prática das principais estruturas de dados da linguagem: **Listas**, **Tuplas**, **Conjuntos (Sets)** e **Dicionários**.

---

## 🚀 Funcionalidades

* **Cadastro de Alunos**: Registro de dados individuais (nome, idade, cidade).
* **Cadastro de Disciplinas e Notas**:
  * Utilização de **Conjuntos (`set`)** para evitar duplicidade de disciplinas.
  * Inclusão dinâmica de múltiplas notas em **Listas (`list`)**.
* **Cálculo de Desempenho**:
  * Média individual automática com status de **Aprovado** ou **Reprovado** (média mínima: 5.0).
* **Estrutura por Aluno**: Dados consolidados em **Dicionários (`dict`)** e agrupados em uma lista geral.
* **Relatório da Turma**:
  * Exibição de dados institucionais imutáveis via **Tuplas (`tuple`)**.
  * Listagem geral de alunos cadastrados e disciplinas ativas.
  * Cálculo da média geral da turma.

---

## 🛠️ Tecnologias e Estruturas Utilizadas

* **Linguagem**: Python 3.x
* **Estruturas de Dados**:
  * `list`: Armazenamento de alunos cadastrados e notas.
  * `tuple`: Dados imutáveis da turma (curso, ano, identificador).
  * `set`: Coleção de disciplinas únicas.
  * `dict`: Mapeamento das propriedades e status de cada aluno.


---

## 📁 Estrutura de Arquivos

```text
python-cadastro-alunos/
├── .gitignore         # Arquivos temporários e pastas ignoradas pelo Git
├── README.md          # Documentação completa do projeto
└── cadastro.py        # Código-fonte principal com a lógica do sistema