class GroceryCalculator:

  grocery_items = {
    'apple': 3,
    'orange': 4,
    'grape': 5,
    'drink': 4,
    'banana': 2
  }

  def __init__(self):
    self.total = 0
    self.items = []

  def add_item(self, item_name):
    self.items.append(item_name)
    self.total += self.grocery_items[item_name]

  def print_bill(self):
    
    print('-----------------')
    for item_name in self.items:
      print(f'{item_name}: {self.grocery_items[item_name]}')
    print('-----------------')
    print(f'total: {self.total}')


grocery_calculator = GroceryCalculator()

grocery_calculator.add_item('apple')
grocery_calculator.add_item('orange')

grocery_calculator.print_bill()
  
