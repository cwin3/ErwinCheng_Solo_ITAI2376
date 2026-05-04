# Reflection

## What Worked Well

The main parts of the project worked really well. The app can load data, filter cars based on user preferences, and show results in a clean and simple way. The deal scoring system was especially useful because it helped highlight which cars are actually good deals instead of just showing a list.

The filters (brand, model, price, fuel) made the app feel more like a real car marketplace, and the overall flow is easy to understand.

---

## What Didn’t Work at First

There were definitely some issues along the way.

The biggest problems were:
- images breaking the app
- trying to use Ollama (local AI) on Streamlit Cloud
- deployment errors that didn’t show clear messages

These things caused a lot of debugging and forced me to simplify parts of the project.

---

## Biggest Challenge

The hardest part was making everything work in the cloud.

At first, I tried to use dynamic images and a real local AI model, but both caused crashes when deploying. I had to step back and rethink the design to make it more stable.

In the end, I:
- switched to simple, reliable images
- replaced the real AI with a simulated version

That made the app much more stable and easier to run.

---

## Changes from My Original Plan

Originally, I planned to use a real AI model (like Ollama) for responses. But since it doesn’t work in Streamlit Cloud, I had to switch to a simulated AI assistant.

Even though it’s simulated, the system still follows the same idea:
- user gives input
- system processes data
- system gives helpful output

So the core concept stayed the same.

---

## What I Would Improve Next

If I had more time, I would:

- connect to real car listing APIs (like Auto.dev or MarketCheck) but need to invest some money into this. no more free data available
- use a real AI model (OpenAI or similar) also need to invest money into this.
- improve the scoring system using machine learning
- add personalized recommendations

---

## Final Thoughts

This project helped me understand how AI concepts can actually be used in a real application. It’s one thing to learn about AI, but building something that simulates decision-making makes it much clearer.

Even though the system is simplified, it shows how AI can help users make better choices, especially in this scenario like buying a car.

Overall, I’m happy with how it turned out, especially after fixing all the deployment issues.
