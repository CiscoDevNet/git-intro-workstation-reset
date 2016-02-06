import os
import sys
import shutil
from os.path import expanduser
from sys import version_info
import git


py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2


class ResetLL():

    _directories = ""
    _home = expanduser("~")

    def __init__(self, directories):

        self._directories = directories

        print("starting")
        print("Initialized with directories: ")
        print(self._directories)

    def reset_git_config(self):
        print("reset config")
        gitconfig = Gitconfig(_home + "/.gitconfig",True)
        user = gitconfig.user.password
        print(user)

    def check_directory(self):

        print("Checking directories")

        for dir in self._directories:
            if (os.path.exists(dir)):
                print("Found directory:" + dir)
                if py3:
                  response = input("Delete directory? ")
                else:
                  response = raw_input("Delete directory? ")

                if response == "yes":
                    print("Deleting: " + dir)
                    shutil.rmtree(dir)
                else:
                    print("Aborting")
                    sys.exit("Aborted!")


if __name__ == '__main__':

    home = expanduser("~")
    directories = ['/src/git-intro', home + '/src/git-intro']

    reset = ResetLL(directories)
    #dir_result = reset.check_directory()
    cofig_result = reset.reset_git_config()
