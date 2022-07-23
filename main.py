from git import Repo
import os
repo = Repo.init(os.getcwd())
repo.index.add([os.getcwd()+"/*"])
repo.index.commit("initial commit")
#repo.create_remote("origin", url="https://github.com/jagg3127/GITPYTHON.git")
print(repo.branches)
#repo.remote("origin").push()
