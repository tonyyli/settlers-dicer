import random
import itertools
import os

def settlers_dicer():
	"""Main program.  This runs when the script is run"""
	players = get_players()
	if want_to_randomize():
		players = randomize_starting_player(players)
	wait_to_roll()
	roll_no_replacement(players)

def generate_pairs():
	"""
	Generate all possible pairs from two six-sided dice.
	Returns a list of pairs.  Each pair is a list of two integers.
	"""
	d1 = [1,2,3,4,5,6]
	d2 = [1,2,3,4,5,6]
	pairs = []
	for i in d1:
		for j in d2:
			pairs.append([i,j])
	return pairs

def roll_no_replacement(players):
	players_cycle = itertools.cycle(players)

	while True:
		# Create and shuffle dice pairs
		pairs = generate_pairs()
		random.shuffle(pairs)
	
		# Loop through dice roll + player pairs
		npairs = len(pairs)
		for i, (pr, pl) in enumerate(zip(pairs, players_cycle)):
			os.system('cls' if os.name=='nt' else 'clear') # Clear screen
			tot = pr[0]+pr[1]
			print " %2d rolled by %s    (%d + %d, %d rolls left)" % (tot, pl.upper(), pr[0], pr[1], npairs-(i+1))

			# Special case: 7 (robber)
			if tot==7: print "ROBBER TIME!"
			wait_to_roll()

		# Start over dice roll. Remember player order and position
		print "***** RESTARTING CYCLE *****"
		next_idx = players.index(pl)+1
		players_prime = players[next_idx:]+players[:next_idx] 
		players_cycle = itertools.cycle(players_prime)
	
#def roll_with_replacement(): # OBSOLETE
#	pairs = generate_pairs()
#	randpair = random.choice(pairs)
#	tot = randpair[0] + randpair[1]
#	print "ROLL: %2d         (%d + %d)" % (tot, randpair[0], randpair[1])

def get_players():
	"""
	Get player names in order, modulo starting player

	Returns a list of player names (strings), provided by user in console
	"""
	players = []
	n = int(raw_input("Enter number of players: "))
	for i in range(n):
		p = raw_input("Enter player %d's name: " % (i+1))
		players.append(p)
	return players

def randomize_starting_player(players):
	"""Given a list of players, return a new list with a random starting player (keeping the same order"""
	idx = random.randrange(len(players))
	players_new = players[idx:]+players[:idx]
	print "Player order is now: %s" % ( ', '.join(players_new) )
	return players_new

def want_to_randomize():
	"""
	Ask user if s/he wants to randomize starting player

	Returns True if yes, False if no
	"""
	s = raw_input("Randomly pick starting player? ")
	s = s.lower() # convert response to lowercase to avoid lower/uppercase ambiguity

	yes_strings = ['y', 'yes']
	no_string = ['n', 'no']

	if s in yes_strings:
		return True
	elif s in no_strings:
		return False
	else:
		print "Not 'y' or 'n', proceeding without randomizing..."
		return False

def wait_to_roll():
	raw_input("Press any key to roll: ")

if __name__=='__main__':
	settlers_dicer()
