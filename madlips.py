# primeiro fiz strings simples usando o format e concatenação
#youtuber = "MarcosCrispim"

#print("Se nscreva no" + youtuber)
#print("Se nscreva no {}".format(youtuber))
#print(f"Se nscreva no{youtuber}")

import random

def play():
	user = input("What's your choice? 'r' for rock, 'p' for papper or 's'for scissors\n")
	computer = random.choice(['s','r','p'])#\n new line

	if user == computer:
		return 'tie'
	# r > s, s > p and p > r
	if is_win(user,computer):
		return 'You won'

	return 'You Lost!'

def is_win(player, opponent):
	#return true if player wins
	# r > s, s > p and p > r
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
		or (player == 'p' and opponent == 'r'):
		return True

print (play())