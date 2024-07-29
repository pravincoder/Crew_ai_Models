from crewai import Agent, Task, Crew
from custom_agent import CustomAgent # You need to build and extend your own agent logic with the CrewAI BaseAgent class then import it here.
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model = "crewai_llama3:latest",
    base_url = "http://localhost:11434"
)

langchain_tools = load_tools(["google-serper"], llm=llm)

agent1 = CustomAgent(
    role="backstory agent",
    goal="who is {input}?",
    backstory="agent backstory",
    verbose=True,
)

task1 = Task(
    expected_output="a short biography of {input}",
    description="a short biography of {input}",
    agent=agent1,
)

agent2 = Agent(
    role="bio agent",
    goal="summarize the short bio for {input} and if needed do more research",
    backstory="agent backstory",
    verbose=True,
)

task2 = Task(
    description="a tldr summary of the short biography",
    expected_output="5 bullet point summary of the biography",
    agent=agent2,
    context=[task1],
)

my_crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew = my_crew.kickoff(inputs={"input": "Mark Twain"})