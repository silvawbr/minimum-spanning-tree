# Seminário 1 — Projeto e Análise de Algoritmos (PROCC0083 - UFS)

## 🎓 Tema: Árvore Geradora Mínima (AGM) aplicada à Análise de Redes Criminosas

Este repositório contém os materiais apresentados por **Wagner Silva** e **Wagner Lucena** no **Seminário 1 da disciplina PROCC0083 - Projeto e Análise de Algoritmos**, ministrada pelo professor **Leonardo Nogueira Matos** no Programa de Pós-Graduação em Ciência da Computação da **Universidade Federal de Sergipe (UFS)**.

---

## 📌 Descrição

Neste seminário, abordamos a aplicação do problema clássico de **Árvore Geradora Mínima (AGM)** para modelagem e análise de uma rede social criminosa real, inspirada na **Operação Darknet**, conduzida pela Polícia Federal.

Utilizando o **algoritmo de Kruskal**, propomos uma forma de extrair a "espinha dorsal" da rede — isto é, um subconjunto mínimo de conexões que mantém a conectividade entre os principais atores (compartilhadores de conteúdo), removendo os nós periféricos e redundantes (visualizadores passivos).

---

## 📁 Estrutura do Projeto

```

📦 minimum-spanning-tree/
├── 📂 src/
│   ├── 📄 kruskal_example.py         # Exemplo de uso da AGM
│   └── 📂 minimum_spanning_tree/
│       ├── 📄 kruskal.py             # Implementação do algoritmo de Kruskal
│       ├── 📄 **init**.py
│       └── 📄 py.typed
├── 📂 tests/                         # Testes automatizados (pytest)
├── 📄 slides.pdf                     # Slides da apresentação
├── 📄 README.md                      # Este arquivo
├── 📄 pyproject.toml                 # Configuração com dependências via uv
└── 📄 uv.lock                        # Lockfile de dependências

````

---

## 🧠 Problema Abordado

- A rede analisada é densa, desassortativa e altamente resiliente, dificultando intervenções tradicionais.
- A extração da AGM sobre o núcleo da rede (766 nós ativos) permite visualizar **conexões essenciais** e otimizar a ação investigativa.
- O peso das arestas foi definido como o **inverso da força da ligação**, permitindo que as conexões mais fortes sejam priorizadas na formação da AGM.

---

## 📊 Algoritmo Utilizado

- **Kruskal (Union-Find)**: implementado em Python com estrutura eficiente de conjuntos disjuntos para evitar ciclos e garantir conectividade.
- Complexidade: \( \mathcal{O}(E \log V) \)

---

## ▶️ Vídeo da Apresentação

📺 [Assista ao seminário no YouTube](https://youtu.be/tfbg836RCNg)

---

## 💻 Como Executar o Projeto

### 1. Instale as dependências usando `uv`:

```bash
uv venv
uv sync --all-groups
````

> Certifique-se de que o comando `uv` esteja instalado. Veja: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---

### 2. Execute o exemplo de AGM (algoritmo de Kruskal)

```bash
uv run python src/kruskal_example.py
```

---

## 📚 Referências

* DUARTE, G. L.; CAMPOS, C. M.; COSTA, C. F.
  *Structural analysis of a large online child exploitation community*.
  Social Network Analysis and Mining, v. 10, n. 1, 2020.
  DOI: [10.1007/s13278-020-00647-z](https://doi.org/10.1007/s13278-020-00647-z)

* DUARTE, G. L.; ALMEIDA, J. G.; CAMPOS, C. M.
  *Spine extraction and structural impact analysis in the Darknet social network*.
  IEEE ISI 2022.
  DOI: [10.1109/ISI55195.2022.9827096](https://doi.org/10.1109/ISI55195.2022.9827096)

---

## 👥 Autores

* Wagner Silva – [@silvawbr](https://github.com/silvawbr)
* Wagner Lucena

---

## 📝 Licença

Este projeto é de caráter acadêmico e está licenciado sob os termos da **MIT License**.