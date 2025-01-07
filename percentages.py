import random
from time import sleep

used_number_combos = []
specific_percent_bool = False
used_number_combo_check = False

specific_percent = input("Any specific percentage to practice? (y/n): ")
if (specific_percent == 'y' or specific_percent == 'Y' or specific_percent == 'yes' or specific_percent == 'Yes'):
  specific_percent_bool = True
  percent = int(input("What percent? : "))
else:
  specific_percent_bool = False

print("")

while True:
  if (specific_percent_bool == False):
    percent = random.randint(0,100)

  number = random.randint(10,200)
  number_combo = str(f"{percent}{number}")
  used_number_check = int(number_combo) in used_number_combos

  if (used_number_check == False):
    raw_answer = (percent * 0.01) * number
    last_digits = raw_answer - int(raw_answer)

    if (last_digits >= 0.5):
      rounded_answer = int((raw_answer + 1) - last_digits)
    else:
      rounded_answer = int(raw_answer)

    user_input = input(f" What is {percent}% of {number} to the nearest percent? : ")

    if (user_input == str(rounded_answer)):
      used_number_combos.append(int(number_combo))
      print(" Correct!")
      print("")
      sleep(1)
    elif (user_input == "gay"):
      print(" no u ")
      print("")
    else:
      print(f" Incorrect, the answer is {rounded_answer}%")
      print("")

