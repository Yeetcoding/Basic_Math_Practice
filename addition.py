import random
from time import sleep
from useful_funcs import space
from useful_funcs import commazation

exit_bool = False

while True:
  if exit_bool == False:
    used_number_combos = []
    stop_bool = False

    space(1)
    digits = int(input(" Would you like problems with 2, 3, or 4 digits? : "))

    if (digits == 4):
      print(" Feeling nerdy today, aren't we?")
      space(1)
      sleep(1)

    print(" Type 'stop' to restart")
    space(1)

    while stop_bool == False:
      if (digits == 2):
        first_number = random.randint(10,99)
        second_number = random.randint(10,99)
      elif (digits == 3):
        first_number = random.randint(100,999)
        second_number = random.randint(100,999)
      elif (digits == 4):
        first_number = random.randint(1000,9999)
        second_number = random.randint(10,999)

      number_combo = str(f"{first_number}{second_number}")
      used_number_check = int(number_combo) in used_number_combos

      if (used_number_check == False):
        answer = first_number + second_number
        user_input = input(f" What is {first_number} + {second_number}? : ")
        if (user_input == "stop" or user_input == "Stop"):
          stop_bool = True
        elif (str(user_input) == str(answer)):
          used_number_combos.append(int(number_combo))
          print(" Correct!")
          sleep(1)
        else:
          print(f" Incorrect, the answer is {answer}")
          sleep(1)
        space(1)
