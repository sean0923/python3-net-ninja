# double the value in nums
nums = [1, 2, 3, 4, 5]

doubNum = []
for num in nums: 
  doubNum.append(num * 2)

print(doubNum)

# comprehension method
doubNum = [ num*2 for num in nums]
print(doubNum)


## squire even nums
square_even_in_nums = []
for num in nums:
  if num % 2 == 0:
    square_even_in_nums.append(num**2)


print('square_even_in_nums: ', square_even_in_nums)

comp_ver_even_square = [ num ** 2 for num in nums if num%2 == 0 ]
print('comp_ver_even_square: ', comp_ver_even_square)



