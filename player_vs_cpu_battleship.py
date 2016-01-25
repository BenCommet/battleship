from random import randint
import time
player_board = []
cpu_board = []
display_board = []
player_count = 0
computer_count = 5

for x in range(10):
	player_board.append(["O"] * 10)
	cpu_board.append(["O"] * 10)
	display_board.append(["O"] * 10)

def print_board(board1, board2):
    for row1, row2 in zip(board1,board2):
        print " ".join(row1) + "        " + " ".join(row2)

def player_miss():
	random = randint(0, 10)
	if random == 0:
		return "There wasn't a ship there... at all"
	if random == 1:
		return "Your missile got wet, first for everything I guess"
	if random == 2:
		return "Have you considered switching to a squirrel based guidance system?"
	if random == 3:
		return "You show that ocean what's up!"
	if random == 4:
		return "SPLOOOOOOOOOOOOOOOOOSH"
	if random == 5:
		return ".....ploop"
	if random == 6:
		return "You blew up...... the water haha"
	if random == 7:
		return "ha\nhaha\nhahahahahahahahah"
	if random == 8:
		return "Just steam, no smoke"
	if random == 9:
		return "You used Splash!\nIt did nothing"
	if random == 10:
		return "I would say I was dissapointed, but that would imply I had any expectations."

def player_hit():
	random = randint(0,5)
	if random == 0:
		return "Everyone gets lucky every once in a while"
	if random == 1:
		return "They had families you monster!"
	if random == 2:
		return "Congrats, now they all died :,("
	if random == 3:
		return "I bet that was toootaly not a random guess or anything right?"
	if random == 4:
		return "That ship cost billions!"
	if random == 5:
		return "You disgust me"

def computer_hit():
	random = randint(0,5)

print "Let's play bitches"
time.sleep(1)

print "Select 5 ship locations, acceptable locations are between 1 and 10"

def get_player_ships(board, player_count):
	for ship in range(5):
		while True:
			try:
				ship_row = int(raw_input("Ship Row:")) - 1
				ship_col = int(raw_input("Ship Column:")) - 1
			except ValueError:
				print("Use a number plz")
				continue
			else:
				break
		if ship_row > 9 or ship_col > 9 or ship_row < 0 or ship_col < 0:
			print "Good god you missed the ocean, one less ship for you."
		elif board[ship_row][ship_col] == "S":
			print "Sweet baby brockoli! What have you done?!?"
			print "There was already a ship there, they both went boom"
			board[ship_row][ship_col] = "O"
			player_count = player_count - 1
		else:
			player_count = player_count + 1
			board[ship_row][ship_col] = "S"
	return player_count

def get_cpu_ships(board):
	for ship in range(5):
		ship_row = randint(0, len(board) - 1)
		ship_col = randint(0, len(board) - 1)
		if board[ship_row][ship_col] == "S":
			ship_row = randint(0, len(board) - 1)
			ship_col = randint(0, len(board) - 1)
			if board[ship_row][ship_col] == "S":
				ship_row = randint(0, len(board) - 1)
				ship_col = randint(0, len(board) - 1)

		board[ship_row][ship_col] = "S"

def main_game(player, computer, display, player_count):
	if player_count == 0:
		"Haha you lost before you started!"
		return 0
	time.sleep(.5)
	print "Find the CPU's ships, remember the ocean's bounds from before"
	time.sleep(.5)
	print "The CPU totally doesn't cheat, promise."
	computer_count = 5
	while True:
		#human player's turn
		while True:
			try:
				ship_row = int(raw_input("Guess Row:")) - 1
				ship_col = int(raw_input("Guess Column:")) - 1
			except ValueError:
				print("Use a number plz")
				continue
			else:
				break
		if ship_row > 9 or ship_col > 9 or ship_row < 0 or ship_col < 0:
			print "You missed the ocean, you loose a turn"
		elif computer[ship_row][ship_col] == "X":
			print "You already blew that part of the ocean up, turn's over."
		elif computer[ship_row][ship_col] == "O":
			print player_miss()
			computer[ship_row][ship_col] = "X"
			display[ship_row][ship_col] = "X"
		else:
			print player_hit()
			computer_count = computer_count - 1
			computer[ship_row][ship_col] = "X"
			display[ship_row][ship_col] = "X"
		if computer_count == 0:
			print "You won!"
			break
		#print_board(display)
		#CPU player's turn
		time.sleep(.3)
		for i in range(6):
			print "."
			time.sleep(.1)
		while True:
			rand_row = randint(0, len(player) - 1)
			rand_col = randint(0, len(player) - 1)
			if player[rand_row][rand_col] == "O":
				print"CPU shot at %s:%s and missed!" %(rand_row, rand_col)
				print "You got lucky asshole."
				player[rand_row][rand_col] = "X"
				break
			elif player[rand_row][rand_col] == "S":
				print"CPU shot at %s:%s and hit!" %(rand_row, rand_col)
				print "HaHaHaHa Boom"
				player[rand_row][rand_col] = "X"
				player_count = player_count - 1
				break
		if player_count == 0:
			print "You lost!"
			break
		print" "
		print"You've shot here.          The CPU shot here."
		print"********************"
		print_board(display, player_board)
		print"********************\n"
		#print "This is what your board looks like."
		#print"********************"
		#print_board(player)
		#print"********************\n"




				
player_count = get_player_ships(player_board, player_count)
get_cpu_ships(cpu_board)
main_game(player_board, cpu_board, display_board, player_count)



