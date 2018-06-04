# some = dict({'a': 'b'})
# print(some)

def printDictionary(din):
  for key, val in din.items():
    print(key, val)


nameNum = {}

while True:
  name = input('name: ')
  favColor = input('favorite color: ')
  nameNum[name] = favColor

  more = input('more? (y/N)')

  if more == 'y':
    continue
  else:
    break

printDictionary(nameNum)





