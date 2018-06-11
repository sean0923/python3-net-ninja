class Person:

  # class level attribute
  isHuman = True

  def __init__(self, name, age):
    # instance attributes
    self.name = name
    self.age = age
  
  def eat_food(self, food):
    print(f'{self.name} is eating {food}')

  @classmethod
  def print_class_method(cls):
    print('print class method')

  @staticmethod
  def render_static_method():
    print('I am staticmethod and I do not need arguments')

person = Person('sean', 30)

print(f'name: {person.name}')

person.eat_food('meat')

# class level attribute
print(Person.isHuman)

Person.print_class_method()
person.print_class_method()

Person.render_static_method()
person.render_static_method()
