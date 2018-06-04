diny = {
  'sean': 'green',
  'anna': 'green',
  'some': 'blue',
  'other': 'red',
  'person': 'black'
}

colors = list(diny.values())
sorted_colors = sorted(colors)
uniq_colors = set(colors)

print('colors:', colors)
print('sorted_color', sorted_colors)
print('uniq-colors', uniq_colors)


# inefficient but show what set does
for color in set(colors):
  print(f'{color} {colors.count(color)}')

  