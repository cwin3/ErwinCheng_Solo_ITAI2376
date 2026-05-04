# Reflection

## What Worked Well

The core functionality of the Smart Car Finder worked really well. The app can filter cars based on user preferences like brand, model, price, and fuel type, and it presents results in a clean and easy-to-understand format.

One of the strongest parts of the project is the deal scoring system. It helps users quickly identify which cars are good deals and which ones might be overpriced or risky. The fraud detection feature also adds realism by flagging suspicious listings.

Another thing that worked well is the hybrid AI system. The app is designed to handle simple queries locally while using a more advanced cloud model for complex questions. This makes the system both efficient and flexible.

---

## What Didn’t Work at First

There were several challenges during development.

At first, image handling caused frequent crashes because of inconsistent data formats. Also, trying to use Ollama alone did not work in Streamlit Cloud since it requires a local environment. Deployment issues were difficult because error messages were not always clear.

These problems forced me to simplify parts of the design and make the system more robust.

---

## Biggest Technical Challenge

The biggest challenge was building an AI system that works both locally and in the cloud.

Initially, I tried to rely only on a local model (Ollama), but it failed in deployment. To solve this, I redesigned the system into a hybrid approach:

- OpenAI handles more complex queries
- Ollama handles simple queries locally
- A fallback response ensures the app never crashes

This approach made the system much more reliable and closer to how real-world AI systems are designed.

---

## Changes from My Original Plan

In my original plan, I intended to use a single AI model for all tasks. However, due to deployment limitations, I changed the design to a hybrid system.

Even though the implementation changed, the core idea stayed the same:
- user input → processing → intelligent output

The new hybrid system actually improved the project by making it more realistic and robust.

---

## What I Would Improve Next

If I continued working on this project, I would:

- Use real car listing APIs (Auto.dev, MarketCheck)
- Train a machine learning model for pricing instead of using rules
- Improve the AI assistant to give more personalized recommendations
- Add user accounts and saved preferences
- Enhance the UI to look closer to real marketplaces like CarMax

---

## Final Thoughts

This project helped me understand how AI concepts can be applied in a practical way. Instead of just learning theory, I was able to build something that simulates real decision-making.

The hybrid AI approach was a big learning moment because it showed how real systems balance performance, cost, and reliability.

Overall, the project demonstrates how AI can help users make better decisions when buying a car, even with a simplified implementation.
