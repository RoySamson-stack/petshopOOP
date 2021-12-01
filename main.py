import json
import os.path

class Inventory:
    pets = {}


    def __init__(self):
        self.load()


    def add(self, key, qty): 
      q = 0
      if key in self.pets:
        v = self.pets[key]
        q = v + qty
      else:
         q = qty
         self.pets[key] = q 
         print(f'Added {qty} {key}: total = {self.pts[key]}')

      
    def remove(self, key, qty):
      q = 0
      if key in self.pets:
        v = self.pets[key]
        q = v - qty

      self.pets[key] = q 
      print(f'Removed {qty} {key}: total = {self.pts[key]}')



    def display(self, key, qty):
      for key, value  in self.pets.items():
        print(f'{key}: {value}') 

    def save(self):
      pass  

    def load(self):
      pass  