#pylint: disable = W0312

import math
def add_vec2(lhs, rhs):
	temp = [0, 0]
	temp[0] = lhs[0] + rhs[0]
	temp[1] = lhs[1] + rhs[1]
	return temp
def subtract_vec2(lhs, rhs):
	temp = [0, 0]
	temp[0] = lhs[0] - rhs[0]
	temp[1] = lhs[1] - rhs[1]
	return temp
def multiply_vec2(lhs, rhs):
	temp = [0, 0]
	temp[0] = lhs[0] * rhs[0]
	temp[1] = lhs[1] * rhs[1]
	return temp
def is_equal_to(lhs, rhs):
	if lhs[0] == rhs[0] and lhs[1] == rhs[1]:
		return True
	else:
		return False
def dot(lhs, rhs):
	temp = lhs[0] * rhs[0] + lhs[1] * rhs[1]
	return temp
def magnitude(rhs):
	result = rhs[0] * rhs[0] + rhs[1] * rhs[1]
	mag = math.sqrt(result)
	return mag
def normalize(rhs):
	temp = [0, 0]
	temp[0] = rhs[0] / magnitude(rhs)
	temp[1] = rhs[1] / magnitude(rhs)
	return temp
vec_one = [15, 20]
vec_two = [15, 20]
print add_vec2(vec_one, vec_two)
print subtract_vec2(vec_one, vec_two)
print multiply_vec2(vec_one, vec_two)
print is_equal_to(vec_one, vec_two)
print dot(vec_one, vec_two)
print magnitude(vec_one)
print normalize(vec_one)
