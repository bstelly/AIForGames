#pylint: disable = W0312
import math

class Vector2:
	'''2D Vector class'''

    #Prototype: def __init__(self, xpos, ypos)
    #Arguments: Two intergers. One for x-position and one for y-position
    #Description: The Initializer function for creating an instance of the Vector2 class
    #Precondition: None
    #Postcondition: An instance of the Vector2 class is created
	def __init__(self, xpos, ypos):
		'''Constructor'''
		self.x_pos = xpos
		self.y_pos = ypos

    #Prototype: def __add__(self, other)
    #Arguments: An instance of Vector2
    #Description: Adds two instances of Vector2 together
    #Precondition: There must two instances of Vector2
    #Postcondition: The added result of the two Vector2s is returned
	def __add__(self, other):
	    	'''Function to add two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos + other.x_pos
		temp.y_pos = self.y_pos + other.y_pos
		return temp

    #Prototype: def __sub__(self, other)
    #Arguments: An instance of Vector2
    #Description: Subtracts the passed in Vector2 from the instance of Vector2 calling the function
    #Precondition: There must two instances of Vector2
    #Postcondition: The passed in Vector2 is subtracted and the result is returned
	def __sub__(self, other):
    		'''Function to subtract two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos - other.x_pos
		temp.y_pos = self.y_pos - other.y_pos
		return temp

    #Prototype: def __mul__(self, other)
    #Arguments: An instance of Vector2
    #Description: Multiplies two instances of Vector2 together
    #Precondition: There must be another instance of Vector2
    #Postcondition: The multiplied result of the two Vector2s is returned
	def __mul__(self, other):
    		'''Function to multiply two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos * other.x_pos
		temp.y_pos = self.y_pos * other.y_pos
		return temp

    #Prototype: def magnitude(self)
    #Arguments: None
    #Description: Calculates the magnitued of the Vector2
    #Precondition: There must be an instance of the Vector2 class
    #Postcondition: The magnitude is returned
	def magnitude(self):
    		'''Function that returns the magnitude of a Vector2'''
		result = self.x_pos * self.x_pos + self.y_pos * self.y_pos
		mag = math.sqrt(result)
		return mag

    #Prototype: def dot(self, other)
    #Arguments: Another instance of the Vector2 class
    #Description: Returns the dot product of two Vector2s
    #Precondition: There must two instances of Vector2
    #Postcondition: The Dot product is returned
	def dot(self, other):
			'''Function to return the dot product of two Vector2s'''
			temp = self.x_pos * other.x_pos + self.y_pos * other.y_pos
			return temp

    #Prototype: def normalize(self)
    #Arguments: None
    #Description: Returns a normalized Vector2
    #Precondition: There must be an instance of the Vector2 class
    #Postcondition: The normalized result of the Vector2 is returned
	def normalize(self):
    		'''Function to return a normalized Vector2'''
		temp = Vector2(0, 0)
		temp.x_pos = temp.x_pos / self.magnitude()
		temp.y_pos = temp.y_pos / self.magnitude()
		return temp

    #Prototype: def __eq__(self, other)
    #Arguments: Two instances of the Vector2 class
    #Description: Compares two Vector2s together and returns true or false
    #Precondition: There must be two instances of the Vector2 class
    #Postcondition: True or False is returned
	def __eq__(self, other):
		'''Function to compare two Vector2s'''
		if self.x_pos == other.x_pos and self.y_pos == other.y_pos:
			return True
		else:
			return False

    #Prototype: def distance(self, other)
    #Arguments: Another instance of the Vector2 class
    #Description: Calculates the distance between two Vector2s
    #Precondition: There must be two instances of the Vector2 class
    #Postcondition: The total distance is returned
	def distance(self, other):
		'''Function to calculate the distance between two Vector2s'''
		distance_x = abs(other.x_pos - self.x_pos)
		distance_y = abs(other.y_pos - self.y_pos)
		distance_total = distance_x + distance_y
		return distance_total

    #Prototype: def output(self)
    #Arguments: None
    #Description: outputs a Vector2 to the console
    #Precondition: There must be an instance of the Vector2 class
    #Postcondition: A Vector2 is printed to the conole
	def output(self):
		'''Function that prints a Vector2 to the console'''
		print str(self.x_pos) + "," + str(self.y_pos)

