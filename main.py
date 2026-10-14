# ─────────────────────────────────────────────────────────────
# SDE Store Inventory
#
# This file grows across SDE lessons 11–13 and is polished in L14.
#   L11  OOP Intro + Product class  — define Product (product_type,
#                                     price, total) with __init__
#   L12  Store CRUD basics          — add / list / update / remove
#                                     products in an inventory dict
#   L13  Error handling + features  — try/except, validation,
#                                     low-stock alerts, etc.
#   L14  Polish & Stretch           — new fields, sorting, search,
#                                     total value, file save/load
#
# Save often — your work persists between lessons.
# ─────────────────────────────────────────────────────────────
import random

class Product():
    # TODO (L11): define __init__ with product_type, price, total
    #   (we avoid the name `type` — it shadows a Python built-in)
    def __init__(self, product_type, brand, color, size, price, total):
      self.product_type = product_type
      self.brand = brand
      self.color = color
      self.size = size
      self.price = price
      self.total = total
      self.prod_id = random.randint(1000, 5000)
    def features(self):
      return {
        'Product': self.product_type,
        'Brand': self.brand,
        'Color': self.color,
        'Size': self.size,
        'Price': self.price,
        'ID': self.prod_id,
        'Total': self.total
      }

def add_product(inventory):
  product_type = input("What is the product/product type? ")
  brand = input("What is the brand? ")
  try:
    color = str(input("What is the color? "))
  except ValueError:
    print("That isn't a color...")
    color = 'Unknown'
  size = (input("What is the size? "))
  try:
    price = float(input("Price? "))
  except ValueError:
    print("That can't be right!")
    price = 0.0
  try:
    total = int(input("Total/Quanity? "))
  except ValueError:
    print("That can't be right!")
    total = 1
  new_product = Product(product_type, brand, color, size, price, total)
  inventory[new_product.prod_id] = new_product
  print(f"Added {product_type} with id {new_product.prod_id}.")

def remove_product(inventory):
  display_inventory(inventory)
  try:
    target = int(input("Which id to remove? "))
  except ValueError:
    print("That isn't an valid ID.")
    return
  if target in inventory:
      del inventory[target]
      print(f"Removed {target}.")
  else:
      print("ID not found.")

def display_inventory(inventory):
  if not inventory:
    print('Add an item before viewing')
    return
  for id, item in inventory.items():
    print(item.features())

def display_menu():
  print('1. View Inventory')
  print('2. Add Product')
  print('3. Search for Product')
  print('4. Remove Product')
  print('5. Exit')

def user_selection():
  display_menu()
  choice = int(input("Choose: "))
  if choice == 1:
    display_inventory(inventory)
    return True
  elif choice == 2:
    add_product(inventory)
    return True
  elif choice == 3:
    if not inventory:
      print('No products in inventory')
    else:
      counter = 0
      search = input("What is the product name? ")
      for i, product in inventory.items():
        if search.lower() in product.product_type.lower():
            print(f'Item found, {product.product_type}')
# Not every product_type has the same features so⬇️
            print(f'Features: {product.features()}')
            counter += 1
      if counter == 0:#search.lower() not in product.product_type.lower():
          print("Product not found")
    return True
  elif choice == 4:
    remove_product(inventory)
    return True
  elif choice == 5:
    print('Goodbye.')
    return False
  else:
    print('Pick a number 1-5.')
    return True

inventory = {}
# TODO (L12): add functions to add, list, update, and remove products.
print("Store inventory ready.")

program_loop = True
while program_loop:
  program_loop = user_selection()
