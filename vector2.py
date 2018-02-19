#pylint: disable = W0312
import math

class Vector2:
	'''2D Vector class'''
	def __init__(self, xpos, ypos):
		'''Constructor'''
		self.x_pos = xpos
		self.y_pos = ypos
	def __add__(self, other):
	    	'''Function to add two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos + other.x_pos
		temp.y_pos = self.y_pos + other.y_pos
		return temp
	def __sub__(self, other):
    		'''Function to subtract two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos - other.x_pos
		temp.y_pos = self.y_pos - other.y_pos
		return temp
	def __mul__(self, other):
    		'''Function to multiply two Vector2s'''
		temp = Vector2(0, 0)
		temp.x_pos = self.x_pos * other.x_pos
		temp.y_pos = self.y_pos * other.y_pos
		return temp
	def magnitude(self):
    		'''Function that returns the magnitude of a Vector2'''
		result = self.x_pos * self.x_pos + self.y_pos * self.y_pos
		mag = math.sqrt(result)
		return mag
	def dot(self, other):
			'''Function to return the dot product of two Vector2s'''
			temp = self.x_pos * other.x_pos + self.y_pos * other.y_pos
			return temp
	def normalize(self):
    		'''Function to return a normalized Vector2'''
		temp = Vector2(0, 0)
		temp.x_pos = temp.x_pos / self.magnitude()
		temp.y_pos = temp.y_pos / self.magnitude()
		return temp
	def __eq__(self, other):
		'''Function to compare two Vector2s'''
		if self.x_pos == other.x_pos and self.y_pos == other.y_pos:
			return True
		else:
			return False
	def distance(self, other):
		'''Function to calculate the distance between two Vector2s'''
		distance_x = other.x_pos - self.x_pos
		distance_y = other.y_pos - self.y_pos
		temp = Vector2(distance_x, distance_y)
		return temp
	def output(self):
		'''Function that prints a Vector2 to the console'''
		print str(self.x_pos) + "," + str(self.y_pos)

