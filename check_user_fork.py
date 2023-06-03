from github import Github
from dotenv import load_dotenv
import os

def check_user_fork(username, repo_name):
    load_dotenv()
    token = os.getenv('smithj09_github_token')
    g = Github(token)

    try:
        g.get_repo('{}/{}'.format(username, repo_name))
        return True
    except:
        return False
