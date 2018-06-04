class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def eat_food(self, food):
    print(f'{self.name} is eating {food}')


person = Person('sean', 30)

print(f'name: {person.name}')

person.eat_food('meat')