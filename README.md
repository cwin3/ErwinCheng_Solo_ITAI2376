# ErwinCheng_Solo_ITAI2376

# Smart Car Buying Assistant

AI-powered car marketplace simulation using a local LLM (Ollama).

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

This project simulates an AI agent using decision scoring inspired by machine learning models.
## Deep Learning Connection

This project is designed to simulate how AI systems help people make better decisions when buying a car.

Even though the deployed version uses a simplified AI response for stability, the structure of the system is inspired by real deep learning models, especially Transformer-based models like ChatGPT.

---

### AI Assistant (LLM Simulation)

The AI assistant in this app represents how a real large language model (LLM) would work. In a real system, the model would understand user questions like:

“Which car is the best deal?”

and then:
- analyze the listings
- compare options
- explain its reasoning

In this project, the responses are simulated, but the idea is the same — helping users make smarter choices using AI-style reasoning.

---

### Deal Scoring (Like a Learned Model)

The app includes a scoring system that evaluates each car based on things like:
- price
- mileage
- listing type (normal, overpriced, suspicious)

Lower price and mileage increase the score, while suspicious listings decrease it.

This is similar to how a machine learning model would weigh different features to predict value or recommend the best option.

---

### Fraud Detection (Anomaly Detection Idea)

The app also flags suspicious listings. This is inspired by anomaly detection, which is commonly used in AI to detect unusual or risky data.

In a real system, this could be powered by trained models, but here it’s implemented using simple rules to simulate the idea.

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
