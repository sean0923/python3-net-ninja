file_path = './files/new_file.txt'

with open(file_path, 'w') as write_file:
  write_file.write('yeah\n')




with open(file_path, 'a') as write_file:
  write_file.write('yeah2\n')

some_list = ['aaa\n', 'bbb\n', 'ccc\n']

with open(file_path, 'a') as write_file:
  write_file.writelines(some_list)


