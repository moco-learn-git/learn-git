# from ghapi.all import GhApi
# import git
# import wonderwords
# import os

import json
from github import Github
from git import Actor
import wonderwords
import tempfile
import shutil
import git
import os

def create_repo():
    token = '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'
    g = Github(token)

    r = wonderwords.RandomWord()
    noun = r.word(include_parts_of_speech=['noun'])
    adjective = r.word(include_parts_of_speech=['adjective'])
    repo_name = adjective + '-' + noun

    org = g.get_organization('moco-learn-git')
    repo = org.create_repo(repo_name, 'Practice the Github Workflow')

    t = tempfile.TemporaryDirectory()
    repo_dir = os.path.join(t.name, repo_name)
    origin_url = 'https://github.com/moco-learn-git/{}.git'.format(repo_name)
    r = git.Repo.clone_from(origin_url, repo_dir)

    src = 'README_start_version.md'
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
    r.remote('origin').push('main')

    return {
        'statusCode': 200,
        'body': json.dumps({'repo_name': repo.name,
                            'repo_url': 'https://github.com/moco-learn-git/{}.git'.format(repo_name)}),
    }

    # token = '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'

    # api = GhApi(token=token)

    # r = wonderwords.RandomWord()
    # noun = r.word(include_parts_of_speech=['noun'])
    # adjective = r.word(include_parts_of_speech=['adjective'])
    # name = adjective + '-' + noun

    # api.repos.create_in_org(org='moco-learn-git', name=name)

    # repo = git.Repo.clone_from(url='https://www.github.com/moco-learn-git/' + name, to_path='/create_repo/' + name)
    # os.chdir('/create_repo/' + name)
    # with open('README.md', 'w') as file:
    #     print('A repo used during the skill test on the Github workflow.\n\nDuring this skill test, a student will have to:'
    #         '\n- Fork the project\n- Clone the project\n- Make a change to the project\n- Merge changes from upstream'
    #         '\n- Commit and Push to your fork\n- Create a Pull Request', file=file)
    # index = repo.index
    # index.add(['README.md'])
    # index.commit('Added README.md file')

    # repo.remote('origin').push()

    # return {"repo_name": name}
