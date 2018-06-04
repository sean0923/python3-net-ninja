strs = ['a', 'b', 'c', 'd']

# for loops

for char in strs:
  print(f'{char}')

print('-------------------')

for char in strs[0:2]:
  print(f'{char}')


print('-------------------')

# while loops

i = 0
while i < len(strs):
  print(i, strs[i])
  i+=1
