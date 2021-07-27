# --- FUNCTIONS --- #

import functions as function

# --- VARIABLES --- #

runned = False

# --- SYSTEMS --- #

try:
  maincmd = int(input('''
  Enter 1 for Game
  Enter 2 to Test System
  >>> '''))
except ValueError:
  print("ValueError | Enter a Valid Input!")
else:
  if maincmd == 1:
    print()
    function.game()
  elif maincmd == 2:
    print()
    function.test()
  else:
    print("Invalid Request. Try again!")
  
# --------------- #