def deco(func):

  def wrapper():
    print('--------------------')
    func()
    print('--------------------')

  return wrapper




@deco
def normal_func(): 
  print('i am normal function')

@deco
def will_i_be_wrapped():
  print('will i be wrapped ?')


normal_func()
will_i_be_wrapped()
