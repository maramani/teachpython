# teach python basic

import pyttsx3
import pydoc

engine = pyttsx3.init()

def communicate(what,msg):
    return what(msg)

def askquestion(msg):
  ans = input("Are you thorough with "+ msg + " statement")
  if ans.lower() in ('yes','y'):
    return True
  else:
    return False

def respond(msg):
  print(msg)
  engine.say(msg)
  engine.runAndWait()

if communicate(askquestion, "input"):
  communicate(respond, "Very good")
else:
  communicate(respond, "Go to python consol and learn using help(\"input\"), "
                     "this time I get it for you. See below. Happy learning!")
  pydoc.pager(pydoc.render_doc(input))

m = ("\nAmend this program to ask user how thorough he/she is with output statement(print), "
     "control statements(if, for, while)")
print('-' * len(m))
print(m)
