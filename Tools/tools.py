from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url(name:str):
    """searches for twitter and linkedin profile page"""
    search = TavilySearchResults()
    res  = search.run(f"{name}")
    return res
