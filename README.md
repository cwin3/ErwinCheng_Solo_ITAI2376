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
