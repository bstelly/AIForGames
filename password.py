#pylint: disable = W0312
from random import *

def weak_password():
	
def main():
	file = open('password.txt', 'r')
	words = []
	for line in file:
    		word = line.replace("\n", "")
		words.append(word)
	print words
	rand_num = randint(0, 5)
	password = words[4]
	print password
	print password.replace("e", "b", 1)
main()
