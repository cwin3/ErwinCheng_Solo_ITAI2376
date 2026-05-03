from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools import search_cars, price_analysis

# LLM
llm = ChatOpenAI(temperature=0)

# Tools
tools = [
    Tool(
        name="Car Search Tool",
        func=search_cars,
        description="Search for car listings based on user preferences like price, location, and type"
    ),
    Tool(
        name="Price Analysis Tool",
        func=price_analysis,
        description="Analyze if a car is a good deal based on price, mileage, and market trends"
    )
]

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Agent (ReAct style)
agent = initialize_agent(
    tools,
    llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)

def run_agent():
    print("🚗 Smart Car Buying Assistant")
    while True:
        query = input("\nEnter your request (or type 'exit'): ")
        if query.lower() == "exit":
            break
        response = agent.run(query)
        print("\nAgent:", response)
