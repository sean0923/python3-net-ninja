class Person:

  def __init__(self):
    self.name = 'sean'
    self.age = 30
  
  def eat_food(self, food):
    print(f'{self.name} is eating {food}')


person = Person()

print(f'name: {person.name}')

person.eat_food('meat')