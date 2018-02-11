#pylint: disable = W0312
from random import *
import os

def weak_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num = randint(0, 99)
	password = words[rand_num]
	os.system('cls')
	print password
	print "\n"
	os.system('pause')
def medium_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num_one = randint(101, 207)
	rand_num_two = randint(0, 99)
	password = words[rand_num_one]
	password = str(password)
	password = password.capitalize()
	second_word = str(words[rand_num_two])
	second_word = second_word.capitalize()
	password += second_word
	os.system('cls')
	rand_interger = randint(100, 999)
	password += str(rand_interger)
	print password
	print "\n"
	os.system('pause')
def strong_password():
	file = open('words_adjectives.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	rand_num_one = randint(101, 207)
	rand_num_two = randint(0, 99)
	password = str(words[rand_num_one])
	password = password.capitalize()
	second_word = str(words[rand_num_two])
	second_word = second_word.capitalize()
	password += second_word
	password = password.replace("a", "@", 10)
	password = password.replace("o", "0", 10)
	password = password.replace("l", "1", 10)
	os.system('cls')
	rand_interger = randint(100, 999)
	password += str(rand_interger)
	print password
	print "\n"
	os.system('pause')
def main():
    	user_input = 0
	while user_input !=  4:
		os.system('cls')
		print "Select a type of password or press (4) to exit\n"
		print "(1) Weak     (2) Medium     (3) Strong"
		#user_input = input('Selection: ')
		user_input = raw_input("Selection: ")
		user_input = int(user_input)
		if user_input is 1:
			weak_password()
		elif user_input is 2:
			medium_password()
		elif user_input is 3:
			strong_password()
		elif user_input is 4:
			return 0
main()
