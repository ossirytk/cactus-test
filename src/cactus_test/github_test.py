import logging

from dotenv import find_dotenv, load_dotenv
from langchain.agents.agent_toolkits.github.toolkit import GitHubToolkit
from langchain.utilities.github import GitHubAPIWrapper

logging.basicConfig(format="%(message)s", encoding="utf-8", level=logging.DEBUG)
load_dotenv(find_dotenv())

github = GitHubAPIWrapper()
issues = github.get_issues()
logging.debug(issues)
toolkit = GitHubToolkit.from_github_api_wrapper(github)
tools = toolkit.get_tools()
logging.debug(type(tools))
logging.debug(len(tools))
