### need to close

# some_file = open('./files/paragraph.txt')

# for line in some_file:
#   print('line: ', line)

# some_file.seek(0)

# print('some_file.readlines(): ', some_file.readlines())

# some_file.close()


### dont need to close
with open('./files/words.txt') as some_file:
  some_file.seek(10)
  read_from_10_to_100 = some_file.read(100)
  print('read_from_10_to_100: ', read_from_10_to_100)


def filter_none_I_line(line):
  return 'I' not in line

with open('./files/words.txt') as some_file:
  lines = some_file.readlines()
  # print('lines: ', lines)
  filtered_lines = list(filter(filter_none_I_line, lines))
  print('filtered_lines: ', filtered_lines)






