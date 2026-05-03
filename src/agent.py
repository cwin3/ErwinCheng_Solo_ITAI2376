from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama

from src.tools import search_cars, price_analysis

# Local LLM via Ollama
llm = ChatOllama(model="llama3")

# Tools
tools = [
    Tool(
        name="Car Search",
        func=search_cars,
        description="Search for car listings"
    ),
    Tool(
        name="Price Analysis",
        func=lambda x: str(price_analysis(search_cars(x))),
        description="Analyze car deals"
    )
]

# Memory
memory = ConversationBufferMemory(return_messages=True)

# Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    memory=memory,
    verbose=True
)
