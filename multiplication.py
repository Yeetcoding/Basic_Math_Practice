from time import sleep
from random import randint
from useful_funcs import space
from useful_funcs import commazation

while True:
  space(1)
  multiply_input = int(input(' Would you like 1, 2, 3, 4, or 5-digit numbers to multiply? : '))
  multiplier_input = int(input(' Would you like to multiply by a 1, 2, 3, 4, or 5-digit number? : '))
  stop_bool = False
  used_number_combos = []
  space(1)

  while stop_bool == False:
    lmt_min_multiply = 10 ** (multiply_input - 1)
    lmt_max_multiply = 10 ** multiply_input
    number_one = randint(lmt_min_multiply, lmt_max_multiply)

    lmt_min_plier = 10 ** (multiplier_input - 1)
    lmt_max_plier = 10 ** multiplier_input
    number_two = randint(lmt_min_plier, lmt_max_plier)

    number_combo = str(f'{number_one}{number_two}')

    if not number_combo in used_number_combos:
      user_input = input(f' What is {commazation(number_one)} x {commazation(number_two)}? : ')
      answer = number_one * number_two

      if user_input == 'stop' or user_input == 'Stop':
        stop_bool = True

      elif user_input == str(answer) or user_input == str(commazation(answer)):
        print(' Correct!')
        used_number_combos.append(number_combo)
        space(1)
        sleep(1)

      else:
        print(f' Incorrect, the answer was {answer}')
        space(1)
        sleep(1)
