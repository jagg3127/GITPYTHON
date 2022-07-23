from git import Repo
import os
repo = Repo.init(os.getcwd())
repo.git.add(update=True)
repo.index.commit("python")
origin = repo.remote(name='origin', url='https://github.com/jagg3127/GITPYTHON')
origin.push()
