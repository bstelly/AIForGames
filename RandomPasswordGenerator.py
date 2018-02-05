#pylint: disable = W0312
from random import *

def weak_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num = randint(0, 29)
	password = words[rand_num]
	print password
def medium_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num_one = randint(31, 64)
	rand_num_two = randint(0, 29)
	password = words[rand_num_two]
	password.append(words[rand_num_one])
	print password
def strong_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num_one = randint(31, 64)
	rand_num_two = randint(0, 29)
	password = words[rand_num_two]
	password.append(words[rand_num_one])
	password.replace("a", "@", 30)
	password.replace("o", "0", 30)
	password.replace("l", "1", 30)
	print password
def main():
	print "Select a type of password or press 'Q' to exit\n"
	print "(1) Weak     (2) Medium     (3) Strong"
	user_input = input("Selection: ")
	if user_input is 1:
		weak_password()
	elif user_input is 2:
		medium_password()
	elif user_input is 3:
		strong_password
	elif user_input is 'Q' or user_input is 'q'
		return 0
main()
