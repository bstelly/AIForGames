import os
def add(lhs, rhs):
	return lhs + rhs
def subtract(lhs, rhs):
	return lhs - rhs
def multiply(lhs, rhs):
	return lhs * rhs
def divide(lhs, rhs):
	return lhs/rhs
user_input = 0
while user_input != 5:
	print "What would you like to do? Input number.\n"
	print "1. Add    2.Subtract    3.Multiply    4.Divide    5. EXIT\n"
	user_input = input("Input Selection\n")
	os.system('cls')
	if user_input != 5:
		lhs = input("Input a number\n")
		rhs = input("Input another number \n")
		os.system('cls')
		if user_input is 1:
			print add(lhs, rhs)
		elif user_input is 2:
			print subtract(lhs, rhs)
		elif user_input is 3:
			print multiply(lhs, rhs)
		elif user_input is 4:
			print divide(lhs, rhs)
		os.system('pause')
	os.system('cls')