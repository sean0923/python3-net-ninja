from random import shuffle

fruits = ['apples', 'oragne', 'banana']

def mix_word(word):
  chars = list(word)
  shuffle(chars)
  return ''.join(chars)


# map(function, data)

mixed_words = list(map(mix_word, fruits))
print('mixed_words: ', mixed_words)

