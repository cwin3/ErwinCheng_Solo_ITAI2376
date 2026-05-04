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

### 1. Transformer-Based AI (Hybrid Approach)

The AI assistant in this system is inspired by Transformer-based models like GPT. The application uses a hybrid approach:

- Simple queries are handled locally (Ollama)
- More complex queries are handled by a cloud-based model (OpenAI)
- A fallback response ensures the system always remains stable

This setup reflects how real-world AI systems often balance performance, cost, and reliability by combining local and cloud models.

Transformer models are powerful because they can:
- understand natural language
- compare multiple options
- generate helpful recommendations

In this project, the AI assistant simulates these capabilities by guiding users in selecting the best car based on their needs.

---

### 2. Feature-Based Scoring (Model-Like Behavior)

The system includes a deal scoring function that evaluates each car using features such as:

- price
- mileage
- listing type (normal, overpriced, suspicious)

Cars with lower price and mileage receive higher scores, while suspicious listings are penalized.

This approach is similar to how machine learning models use multiple features to make predictions or recommendations. In a real implementation, this could be replaced with a trained neural network or regression model that predicts fair market value.

---

### 3. Anomaly Detection (Fraud Detection)

The app flags suspicious listings using rule-based logic that mimics anomaly detection.

In real AI systems, anomaly detection is often handled using:
- autoencoders
- isolation forests
- classification models trained on fraud data

Although simplified, this feature demonstrates how AI can help users avoid risky or fraudulent options.

---

### 4. Real-World AI System Design

This project reflects key ideas used in real AI systems:

- combining multiple models (local + cloud)
- using structured data for decision-making
- supporting users with intelligent recommendations

Even though the implementation is simplified, it shows how deep learning concepts can be applied to a practical problem like car buying.

---

### Summary

Overall, this project demonstrates how AI can enhance user decision-making by combining filtering, scoring, and language-based guidance. The hybrid AI approach makes the system both realistic and reliable, while still reflecting how modern deep learning systems operate.

---


### Final Project Structure
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
