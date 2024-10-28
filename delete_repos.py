import os
from github import Github
from dotenv import load_dotenv

def delete_repos():
    load_dotenv()
    token = os.getenv('smithj09_github_token')
    g = Github(token)

    org = g.get_organization('moco-learn-git')
    repos = org.get_repos()

    for repo in repos:
        if (repo.name != 'learn-git'):
            print(f'{repo.name} has now been deleted.')
            repo.delete()
