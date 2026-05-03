# Optional CLI version
from src.agent import agent

while True:
    q = input("Ask: ")
    print(agent.run(q))
