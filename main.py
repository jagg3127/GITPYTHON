from git import Repo
import os
repo = Repo.init(os.getcwd())
repo.git.add(update=True)
repo.index.commit("python")
try:
  origin = repo.create_remote(name='origin', url='https://github.com/jagg3127/GITPYTHON')
except:
  origin = repo.remote(name='origin')
origin.push()
