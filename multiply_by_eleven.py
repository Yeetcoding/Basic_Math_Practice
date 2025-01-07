import random
from time import sleep

used_numbers = []
used_number_check = False
solved_problems = 0

while True:
  if (solved_problems != 89):
    multiplier = random.randint(10,99)
    used_number_check = multiplier in used_numbers

    if (used_number_check == False):
      #print(f" Used numbers: {used_numbers}")
      print(f" Solved: {solved_problems}")
      print(f" Q.{solved_problems + 1}")
      solution = multiplier * 11
      user_input = int(input(f" {multiplier} x 11 = "))

      if (user_input == solution):
        print(" Correct!")
        solved_problems += 1
        used_numbers.append(multiplier)
      else:
        print(f" Incorrect, the answer is: {solution}")

      print("")
      sleep(1)

  elif (solved_problems >= 89):
    used_numbers = []
    solved_problems = 0
