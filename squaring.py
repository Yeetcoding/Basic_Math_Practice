from space_func import space
from time import sleep
import random

space(1)

while True:
  restart_bool = False
  used_numbers = []
  print(' type "stop" to restart program')
  digit_input = int(input(' Would you like to square 2-digit, 3-digit, 4-digit, or 5-digit numbers? : '))
  limit_min = 10 ** (digit_input - 1)
  limit_max = 10 ** (digit_input)
  space(1)
  while restart_bool == False:
    square_number = random.randint(limit_min, limit_max)
    if not square_number in used_numbers:
      answer = square_number ** 2
      user_input = input(f' What is {square_number} squared? : ')
      if user_input == 'stop' or user_input == 'Stop':
        restart_bool = True
        space(1)
      elif user_input == str(answer):
        used_numbers.append(square_number)
        print(' Correct!')
        space(1)
        sleep(1)
      else:
        print(f' Incorrect, the answer was {answer}')
        space(1)
        sleep(1)
