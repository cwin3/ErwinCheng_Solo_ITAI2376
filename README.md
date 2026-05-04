# ErwinCheng_Solo_ITAI2376

# Smart Car Buying Assistant

## Objective

The objective of this project is to design and develop an AI-powered car buying assistant that helps users find the best vehicle options based on their preferences. The system filters and analyzes car listings, highlights good deals, and flags potentially risky listings to support smarter decision-making. This project also demonstrates how AI concepts can be applied to a real-world problem in a simple and practical way.

---

## Features
- 10,000 realistic car listings
- VIN, dealer, fraud detection
- Filtering + sorting
- Favorites + comparison
- AI assistant (Ollama)

## Run

python generated_dataset.py
ollama run llama3
streamlit run app.py


## Deep Learning Connection

This project is designed to simulate how AI systems help people make better decisions when buying a car.

Even though the deployed version uses a simplified AI response for stability, the structure of the system is inspired by real deep learning models, especially Transformer-based models like ChatGPT.

---

How to choose Agent Framework.pdf
PDF
ITAI_2376_Midterm_Final_Project_Specs.pdf
PDF
OVERVIEW

Your midterm is a design document — a blueprint for the AI agent you will build for the final. You are not building anything yet. You are planning, researching, and showing me that you understand how the deep learning concepts we have covered connect to real-world AI agent applications.

This blueprint becomes the foundation for your Final Project (due May 3).


CHOOSE YOUR PATH

• Option A — Single AI Agent: Plan one agent that uses deep learning to perceive, reason, and act on a real-world task.


Declare which option you are choosing and explain why.


WHAT TO INCLUDE IN YOUR BLUEPRINT (3–6 pages)

1. Problem Statement — What real-world problem does your agent solve? Who benefits?
2. Option Choice — Which option (A ) and why.
3. Agent Architecture — A diagram showing inputs, reasoning, actions, and tools. Label everything.
4. Deep Learning Connection — Identify at least 2 course modules (CNNs, RNNs, Transformers, VAEs, GANs, etc.) and explain how they fit into your agent.
5. Agent Framework — Which framework you plan to use (LangChain, CrewAI, AutoGen, smolagents, or other) and why.
6. Tools & Data — What tools, APIs, and data sources will your agent need?
7. Build Plan — A week-by-week timeline from midterm to final due date.
8. Anticipated Challenges — What could go wrong and how will you handle it?

---

### Big Picture

Overall, this project shows how AI concepts like:
- decision-making
- feature evaluation
- anomaly detection
- and language-based guidance

can be applied to a real-world problem like buying a car.

Even though the AI is simplified, the structure reflects how real AI systems are designed.


Final Project Structure
ErwinCheng_Solo_ITAI2376/
│
├── app.py
├── generated_dataset.py
├── requirements.txt
├── README.md
├── REFLECTION.md
│
├── data/
│   └── cars.csv   (optional, auto-generated if missing)
│
├── src/
│   ├── tools.py
│   └── ollama_agent.py
