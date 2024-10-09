# teach python basic

import pyttsx3
import io
import sys

engine = pyttsx3.init()


def askquestion(syn):
    respond("Are you thorough with Python " + syn + " statement?")
    ans = input()
    if ans.lower() in ('yes', 'y'):
        respond("Very good")
    else:
        respond(f"No worries, go to python consol and learn using help(\"{syntax}\"), This time I get it for you. See below. Happy learning!")
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        help(syntax)
        sys.stdout = old_stdout
        print(new_stdout.getvalue())


def respond(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()


askquestion("input")
