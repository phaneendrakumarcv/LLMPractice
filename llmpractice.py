from os import scandir

from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.twitter import scrape_user_tweets
from Agents import twitteragent



def ice_break_with(name:str) -> str:
    profile = twitteragent.lookup(name)
    tweet_data = scrape_user_tweets(profile)
    summary_template = """
        given the tweets {twitter_posts} about a person:
        1. Create a short summary of the tweets
        2. Interesting facts abouts the tweets
        3. Also identify total sentiment of the tweets positive, negative or neutral
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["twitter_posts"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"twitter_posts":tweet_data})

    print(res.content)





if __name__ == "__main__":
    print("Main method enter")
    ice_break_with("Elon Musk")




