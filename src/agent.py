from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from src.tools import search_cars, price_analysis

# LLM
llm = ChatOpenAI(temperature=0)

# Tools
tools = [
    Tool(
        name="Car Search",
        func=search_cars,
        description="Search for car listings based on user query"
    ),
    Tool(
        name="Price Analysis",
        func=lambda x: str(price_analysis(search_cars(x))),
        description="Analyze if a car is a good deal"
    )
]

# Memory
memory = ConversationBufferMemory(return_messages=True)

# Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)
