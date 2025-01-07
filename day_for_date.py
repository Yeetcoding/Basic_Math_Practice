from time import sleep
from useful_funcs import space
from random import randint

day_list = [
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
  'Sunday'
]

month_list = [
  'January',
  'Feburary',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
]

day_codes = {
  0: 'Sunday',
  1: 'Monday',
  2: 'Tuesday',
  3: 'Wednesday',
  4: 'Thrusday',
  5: 'Friday',
  6: 'Saturday'
}

month_codes = {
  'January': 6,
  'Feburary': 2,
  'March': 2,
  'April': 5,
  'May': 0,
  'June': 3,
  'July': 5,
  'August': 1,
  'September': 4,
  'October': 6,
  'November': 2,
  'December': 4
}

leap_years = []
leap_year_loop = 1796
while leap_year_loop < 2200:
  leap_year_loop += 4
  leap_years.append(leap_year_loop)

def red7(num):
  while num >= 7:
    num -= 7
  return num

while True:
  restart_bool = False
  mode_set = input(' Do you want to practice codes or find days? (type "codes" or "days") : ')
  print(' Type "stop" to restart program')
  space(1)

  while restart_bool == False:
    if mode_set == 'days' or mode_set == 'Days':
      year = randint(2000,2100)
      end_of_year = int(year - 2000)
      year_code = end_of_year + int(end_of_year / 4)
      year_code = red7(year_code)

      month = month_list[randint(0,11)]
      month_code = month_codes[month]
      if (year in leap_years) and (month == 'January' or month == 'Feburary'):
        month_code -= 1

      day = randint(1,29)

      code_answer = month_code + day + year_code
      code_answer = red7(code_answer)
      day_answer = day_codes[code_answer]

      user_input = input(f' What day of the week was/will it be on {month} {day}, {year}?: ')
      if user_input == 'stop' or user_input == 'Stop':
        restart_bool = True
      elif user_input == day_answer:
        print(' Correct!')
        sleep(1)
      else:
        print(f' Incorrect, the answer is {day_answer}({code_answer})')
        print(f' ( {month_code} + {day} + {year_code} )')
        sleep(1)
      space(1)

    elif mode_set == 'codes' or mode_set == 'Codes':
      day_month_set = input(' Would you like to memorize days or months? : ')
      space(1)
      while restart_bool == False:
        if day_month_set == 'days' or day_month_set == 'Days':
          day_code = randint(0,6)
          day = day_codes[day_code]
          user_input = input(f' What is the number code for {day}? : ')
          if user_input == 'stop' or user_input == 'Stop':
            restart_bool = True
          elif user_input == str(day_code):
            print(' Correct!')
            sleep(1)
          else:
            print(f' Incorrect, the answer was {day_code}')
            sleep(1)
          space(1)
        elif day_month_set == 'months' or day_month_set == 'Months':
          month = month_list[randint(0,11)]
          month_code= month_codes[month]
          user_input = input(f' What is the code for {month}? : ')
          if user_input == 'stop' or user_input == 'Stop':
            restart_bool = True
          elif user_input == str(month_code):
            print(' Correct!')
            sleep(1)
          else:
            print(f' Incorrect, the answer was {month_code}')
            sleep(1)
          space(1)



