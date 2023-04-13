# Test.py
class Foo: 
   def __init__(self, q): 
      self.name = q 
   def hi(self): 
      print(self.name,"!") 
a = Foo("zoo") 
b = Foo("bar") 
c = Foo("goo")
b.hi()