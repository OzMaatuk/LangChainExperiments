from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

agent = create_csv_agent(
    OpenAI(openai_api_key="", temperature=0),
    "annual-enterprise-survey-2021-financial-year-provisional-csv.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent.run("how many rows are there?")