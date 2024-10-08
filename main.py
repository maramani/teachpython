# teach python basic

def check(what):
  ans = input(what)
  if ans.lower in ('yes','y'):
    return True
  else:
    return False
  
if check("Do you know how to get input from user at runtime?"):
  if check("Do you know how to print to sys outpit device?"):
    print("good")
  else:
    print("learn using help(\"print\")")
else:
  print("learn using help(\"input\")")
      
