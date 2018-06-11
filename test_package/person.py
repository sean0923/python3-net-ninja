class Person:

  # class level attribute
  isHuman = True

  def __init__(self, name, age, weight):
    # instance attributes
    self.name = name
    self.age = age
    self.weight = weight

  def eat_food(self, food):
    print(f'{self.name} is eating {food}')

  @classmethod
  def print_class_method(cls):
    print('print class method')

  @staticmethod
  def render_static_method():
    print('I am staticmethod and I do not need arguments')
