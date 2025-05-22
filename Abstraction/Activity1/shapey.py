from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass
    
	@abstractmethod
	def volume(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius
	
	def area(self):
		return 3.14 * self.radius ** 2
	
	def volume(self):
		return 3.14 * 4/3 * self.radius * self.radius * self.radius

class Rectangle(Shape):
	def __init__(self, width, height, length):
		self.width = width
		self.height = height
		self.length = length
		
	def perimeter(self):
		return 2 * (self.width + self.height)
	
	def area(self):
		return self.width * self.height
	
	def volume(self):
		return self.width * self.height * self.length

# Creating instances of concrete subclasses 
circle = Circle(5) 
rectangle = Rectangle(4, 6, 10)

# Using the same interface to compute perimeter 
print("Circle Perimeter:", circle.perimeter()) 
print("Rectangle Perimeter:", rectangle.perimeter()) 

# Output
#Circle Perimeter: 31 
#Rectangle Perimeter: 20