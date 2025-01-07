# Divide a three-digit number by either a one or two-digit number based on user choice

from time import sleep
import random
from useful_funcs import space

used_number_combos = []

while True:
  digit_set = int(input(' Would you like to divide by 1 or 2 digits? : '))
  print(' Type "stop" to restart program')
  space(1)
  restart_bool = False
  while restart_bool == False:
    if digit_set == 1:
      divisor = random.randint(2,10)
    elif digit_set == 2:
      divisor = random.randint(10,100)
    dividend = random.randint(100,1000)
    number_combo = str(f'{dividend}{divisor}')

    if not number_combo in used_number_combos:
      user_input = input(f' What is {dividend} divided by {divisor} (to the first decimal place)? : ')
      raw_answer = dividend / divisor

      if str(raw_answer)[2] == '.':
        if str(raw_answer)[3] == 0:
          answer = int(raw_answer)
        else:
          answer = str(raw_answer)[0:4]
      elif str(raw_answer)[3] == '.':
        if str(raw_answer)[4] == '0':
          answer = int(raw_answer)
        else:
          answer = str(raw_answer)[0:5]

      if user_input == 'stop' or user_input == 'Stop':
        restart_bool = True
        space(1)
      elif user_input == str(answer):
        used_number_combos.append(number_combo)
        print(' Correct!')
        space(1)
        sleep(1)
      else:
        print(f' Incorrect, the answer was {answer}')
        space(1)
        sleep(1)
