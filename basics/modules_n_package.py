from test_package.person import Person
from test_package.mothods import weight_minus_age, weight_plus_age

person = Person('sean', 30, 170)

print(f'weight - age: {weight_minus_age(person.weight, person.age)}')
print(f'weight + age: {weight_plus_age(person.weight, person.age)}')
