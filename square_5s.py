import random
from time import sleep

master_list = [15,25,35,45,55,65,75,85,95]
used_numbers = []
used_number_check = False
solved_problems = 0

while True:
  if (solved_problems != 9):
    list_number = random.randint(0,8)
    multiplier = master_list[list_number]
    used_number_check = multiplier in used_numbers

    if (used_number_check == False):
      #print(f" Used numbers: {used_numbers}")
      print(f" Solved: {solved_problems}")
      print(f" Q.{solved_problems + 1}")
      solution = multiplier * multiplier
      user_input = int(input(f" {multiplier} x {multiplier} = "))

      if (user_input == solution):
        print(" Correct!")
        solved_problems += 1
        used_numbers.append(multiplier)
      else:
        print(f" Incorrect, the answer is: {solution}")

      print("")
      sleep(1)

  elif (solved_problems >= 9):
    used_numbers = []
    solved_problems = 0


