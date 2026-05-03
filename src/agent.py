from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from src.tools import search_cars, price_analysis

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(
        name="Car Search",
        func=search_cars,
        description="Search car listings"
    ),
    Tool(
        name="Price Analysis",
        func=lambda x: str(price_analysis(search_cars(x))),
        description="Analyze deals"
    )
]

memory = ConversationBufferMemory()

agent = initialize_agent(
    tools,
    llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)
