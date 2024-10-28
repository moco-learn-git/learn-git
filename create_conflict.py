import git
from github import Github
from git import Actor
import os
import tempfile
import shutil
from dotenv import load_dotenv

def create_conflict(repo_name):
    load_dotenv()
    token = os.getenv('smithj09_github_token')
    g = Github(token)

    t = tempfile.TemporaryDirectory()
    repo_dir = os.path.join(t.name, repo_name)
    origin_url = 'https://github.com/moco-learn-git/{}.git'.format(repo_name)
    r = git.Repo.clone_from(origin_url, repo_dir)

    src = 'README_conflict_version.md'
    dst = os.path.join(repo_dir, "README.md")
    shutil.copy(src, dst)

    origin = r.remote('origin')
    # adding access token to remote for authentication
    with origin.config_writer as cw:
        cw.set("url", "https://{}@github.com/moco-learn-git/{}.git".format(token, repo_name))

    author = Actor("Ben Coleman", "coleman@cs.moravian.edu")

    index = r.index
    index.add(['README.md'])
    index.commit('Change to an enumerated list', author=author, committer=author)
    r.remote('origin').push()

    return {'statusCode': 200}