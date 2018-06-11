from random import randint


tools = ['pen', 'pencil']

with open('./files/fruits.txt') as read_file:
  fruits = read_file.read().split()

  with open('./files/fruit_tools.txt', 'a') as write_file:

    for tool in tools: 
      randFruitIdx = randint(0, len(fruits) - 1)
      write_file.write(f'{fruits[randFruitIdx]} {tool}\n')


    
