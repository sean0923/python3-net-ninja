# python3 basic

### class
There are instance & class level attribute and methos

### 19 Modules & Packages
- Packages: collections of modules
- Just having __init__.py undef folder tells python it's package ?

### 20 Bar Tab Calculator (Grocery Calculator)

### 21 List Comprehensions
If you want to change item in list (similar to .map in js)
Not something that you have to use but sometime nice to use

### 22 Maps
map(function, list) return some sort of obj
so need to wrap with list()

### 23 Filters
again
list(filter(function, list))

### 24 Lambdas
dont need to define function
you can just use lambda as inline function

lambda => inline anonymous function

ex) some_var = list(map(lambda a: a * 2, [1, 2, 3]))

### 25 Decorators
Can decorate any function with decorator

### 26 Reading Files
- one way require open and close file
- 2nd way - don't have to close file (with ... as <filename>)

once file is read need to move cursor back to 0 --> <filename>.seek(0)

### 27 Writing Files 
'w' for write --> with open(file_path, 'w') as write_file:
'a' for append --> with open(file_path, 'a') as write_file:

### 28 Lorem Ipsum Generator
