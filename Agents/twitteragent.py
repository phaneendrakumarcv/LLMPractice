from dotenv import load_dotenv
from langchain.chains.summarize.refine_prompts import prompt_template

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from Tools.tools import get_profile_url


def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model = "gpt-3.5-turbo"
    )

    template = """
    Given the name of the person {full_name} I want you to find their twitter profile page,
    In your final answer include only username of their twitter profile
    """
    prompt_template = PromptTemplate(
        template= template,input_variables=["full_name"]
    )

    tools_for_agent = [
        Tool(
            name = "Crawl google to find twitter user profile",
            func=get_profile_url,
            description = "useful for when you need to get twitter profile page url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)
    result = agent_executor.invoke(input = {"input" : prompt_template.format_prompt(full_name=name)})

    url = result["output"]
    return url

if __name__=="__main__":
    url = lookup("Elon Musk")
    print(url)

