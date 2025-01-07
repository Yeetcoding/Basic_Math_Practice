## use < from useful_funcs import --function-- >  to import these functions (don't use the dashes)

def space(lines):
  times = 1
  while times <= lines:
    print('')
    times += 1

def commazation (num):
  raw_list = list(str(num))
  list_leng = len(raw_list)
  com_pos = -3
  num_of_comms = int((list_leng - 1) / 3)
  writ_comms = 1

  while writ_comms <= num_of_comms:
    com_pos = -((4 * writ_comms) - 1)
    raw_list.insert(com_pos, ',')
    writ_comms += 1

  final_str = ''.join(raw_list)
  return final_str

