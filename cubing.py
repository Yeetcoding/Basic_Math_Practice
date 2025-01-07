from time import sleep
import random
from useful_funcs import space

used_numbers = []

while True:
  restart_bool = False
  print(' Type "stop" to restart program')
  digit_set = int(input(' Would you like 1-digit or 2-digit numbers? : '))
  while restart_bool == False:
    if digit_set == 1:
      cube_number = random.randint(0,10)
    elif digit_set == 2:
      cube_number = random.randint(10,100)
    if not cube_number in used_numbers:
      user_input = input(f' What is {cube_number} cubed? : ')
      answer = cube_number ** 3
      if user_input == 'stop' or user_input == 'Stop':
        restart_bool = True
        space(1)
      elif user_input == str(answer):
        used_numbers.append(cube_number)
        print(' Correct!')
        space(1)
        sleep(1)
      else:
        print(f' Incorrect, the answer was {answer}')
        space(1)
        sleep(1)

