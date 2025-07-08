# 🤖 LangGraph Reflection Agent

Projeto experimental de **Agente Reflexivo com LangGraph**, que simula um fluxo de iteração entre geração e reflexão usando LLMs, com controle por grafo de mensagens.

## 📌 Objetivo

Melhorar mensagens (ex: tweets, prompts, etc.) através de um fluxo iterativo de:
- Geração (`generate`)
- Reflexão (`reflect`)
- Parada condicional (baseada no número de mensagens)

Inspirado em técnicas de **self-refinement** e **multi-agent reasoning**.

---

## ⚙️ Tecnologias

- [Python 3.11+](https://www.python.org/)
- [LangChain](https://docs.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [OpenAI API](https://platform.openai.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🧠 Estrutura do fluxo

```mermaid
graph TD;
    Start --> Generate
    Generate -->|len(messages) > 6| End
    Generate -->|else| Reflect
    Reflect --> Generate
🗂️ Estrutura do Projeto
bash
Copiar
Editar
reflection-agent/
├── chains.py         # Define os chains de geração e reflexão
├── main.py           # Executa o fluxo LangGraph
├── env_test.py       # Validador de carregamento do .env
├── .env              # Armazena suas chaves de API (NÃO subir para o GitHub)
├── README.md         # Este documento
🚀 Como executar
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/langgraph-reflection-agent.git
cd langgraph-reflection-agent
Crie um ambiente virtual:

bash
Copiar
Editar
python -m venv .venv
source .venv/Scripts/activate  # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Crie seu .env com a chave da OpenAI:

ini
Copiar
Editar
OPENAI_API_KEY=sk-xxxxxx
Execute o agente:

bash
Copiar
Editar
python main.py
💡 Exemplo de uso
Entrada:

kotlin
Copiar
Editar
Make this tweet better:
@LangChainAI — newly Tool Calling feature is seriously underrated.
Saída esperada:

sql
Copiar
Editar
The new Tool Calling feature from @LangChainAI makes multi-agent orchestration incredibly easy — I covered it in my latest video 🔥
📈 Possíveis melhorias
Uso de memória de longo prazo entre iterações

Métricas de avaliação de melhoria (BLEU, ROUGE)

UI com Streamlit ou Gradio

Armazenamento em vetor com ChromaDB
