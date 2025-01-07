from time import sleep
import random

used_numbers = []

print('')

while True:
  random_number = random.randint(0,100)
  if not random_number in used_numbers:
    used_numbers.append(random_number)
    answer = 100 - random_number
    user_input = int(input(f' What is the complement to {random_number}? : '))
    if user_input == answer:
      print(' Correct!')
      print('')
    else:
      print(f' Incorrect, the answer is {answer}')
      print('')
    sleep(1)
