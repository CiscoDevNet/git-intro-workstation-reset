#!/usr/bin/env python

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
        print("|**************************************************|")
        print("|Welcome to the Cisco DevNet git-intro reset script|")
        print("|**************************************************|")
        print("Configuration:")
        print("\nDir to seek and destroy: ".join(self._directories))

    def reset_git_config(self):

        message = "Remove user info? "

        print("STEP 2: reset config ...")
        globalconfig = git.GitConfigParser(os.path.normpath(os.path.expanduser("~/.gitconfig")), read_only=False)

        print("*********************************")
        print("Current git global config values:")
        print("*********************************")
        print("\t" + globalconfig.get_value("user", "name"))
        print("\t" + globalconfig.get_value("user", "email"))

        if py3:
          response = input(message)
        else:
          response = raw_input(message)

        if response == "yes":
            print("Resetting user...")
            globalconfig.set_value("user", "name", "John Doe")
            globalconfig.set_value("user", "email", "jdoe@doe.com")
        else:
            print("No changes made. Continuing...")

    def check_directory(self):

        print("STEP 1: checking directories ...")

        message = "Delete directory? "

        for dir in self._directories:
            if (os.path.exists(dir)):
                print("*********************************")
                print("Found directory: ")
                print("*********************************")
                print("\t" + dir)
                if py3:
                  response = input(message)
                else:
                  response = raw_input(message)

                if response == "yes":
                    print("Deleting: " + dir)
                    shutil.rmtree(dir)
                else:
                    print("No changes made. Continuing...")


if __name__ == '__main__':

    home = expanduser("~")
    directories = ['/src/git-intro',
        home + '/src/git-intro',
        '/src/upgraded-guacamole',
        home + '/src/upgraded-guacamole']

    reset = ResetLL(directories)
    dir_result = reset.check_directory()
    cofig_result = reset.reset_git_config()
    print("NO MORE STEPS: Finished workstation cleanup!")
