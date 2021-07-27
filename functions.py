from random import choice
import sys

def game():
  colour_file = open("colour.txt", "r+")
  input_file = open("input.txt", "r+")
  counter = 0
  colours = ["Green", "Red", "Purple", "Light Blue", "Yellow", "Black"]
  comp = choice(colours)
  colour_contents = colour_file.read()
  if colour_contents == 0:
    pass
  else:
    colour_file.truncate(100)
    colour_file.write(comp)
  guessed = False
  while not guessed:
    if counter >= 3:
      print("You ran out of guesses!")
      print(f"The correct colour was {str(comp.title())}!")
      sys.exit("Game ended.")
    else:
      ui = input("Enter Color: ")
      counter += 1
      input_contents = input_file.read()
      if input_contents == ui:
        continue
      else:
        input_file.truncate(1)
        input_file.write(ui)
      if comp == ui:
        print("Congratulations! You guessed the right colour!")
        if counter == 1:
          print(f"You took {str(counter)} try to guess the correct colour!")
          guessed = True
        else:
          print(f"You took {str(counter)} tries to guess the correct colour!")
          guessed = True
      else:
        print("Wrong! Try again!")
  else:
    sys.exit("Game Ended.")

def test():
  print("Loading Test Configurations...")
  try:
    import os
  except ImportError:
    print("Test configurations cannot be loaded.")
    print("Exiting Test Function...")
    sys.exit("Test Execution Failure.")
  else:
    print("Test Configuration Upload Complete.")
    print("Checking File Existance...")
    colour_file_e = os.path.isfile("colour.txt")
    input_file_e = os.path.isfile("input.txt")
    if colour_file_e and input_file_e is True:
      print("File Existance Check Complete.")
    elif colour_file_e is True and input_file_e is False:
      print("1 File Not Detected.")
      print("Creating File (input.txt)...")
      input_file = open("input.txt", "x")
      input_file.close()
    elif colour_file_e is False and input_file_e is True:
      print("1 File Not Detected.")
      print("Creating File (colour.txt)...")
      colour_file = open("colour.txt", "x")
      colour_file.close()
    elif colour_file_e and input_file_e is False:
      print("No files detected.")
      print("Creating Files (colour.txt), (input.txt)")
      input_file = open("input.txt", "x")
      colour_file = open("colour.txt", "x")
      input_file.close()
      colour_file.close()
    else:
      print("Test Execution Error.")

'''
def reset_files():
  input_file = open("input.txt")
  input_contents = input_file.read()
  if input_contents == "":
    colour_file = open("colour.txt")
    colour_contents = colour_file.read()
    if colour_contents == "":
      colour_file.close()
      input_file.close()
      print("Files Resetted.")
    else:
'''
