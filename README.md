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

# 🤖 LangGraph Reflection Agent

Projeto baseado no curso:

> 📚 **LangGraph — Develop LLM powered AI agents with LangGraph**  
> Curso da [Udemy](https://www.udemy.com/course/langgraph-develop-llm-powered-ai-agents-with-langgraph/)  
> ★★★★★ 4.66 (1976 avaliações)  
> Aprenda LangGraph construindo um agente de IA com LLMs em Python

---

## 📌 Objetivo

Melhorar mensagens (ex: tweets) por meio de um fluxo iterativo com LLMs, combinando:
- Geração (`generate`)
- Reflexão (`reflect`)
- Parada condicional inteligente

Inspirado em técnicas de **self-refinement**, **auto-crítica** e **multi-agent systems**.

---

## 🧠 Estrutura do fluxo


graph TD;
    Start --> Generate
    Generate -->|len(messages) > 6| End
    Generate -->|else| Reflect
    Reflect --> Generate
