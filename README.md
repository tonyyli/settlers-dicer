# settlers-dicer
==============

Dice-rolling command-line program for playing the board game "Settlers of Catan" with friends.  Cycles through all possible dice rolls in random order.  Each roll must occur exactly once before re-randomizing and repeating.  This makes rolling the dice more like flipping through a shuffled deck of 36 cards, so that the frequency with which a given combination appears more accurately reflects the probability of rolling it.

## Usage

1. At the command line, run script with the command:

```
	$ python settlers_dicer.py
```

2. When prompted, enter the number of players for the current game.  E.g.:

```
	Enter number of players: 4
```

3. When prompted, enter the names of the players **in the correct order** (i.e. going clockwise or counterclockwise around the table, depending on players' preference).  E.g.:

```
	Enter player 1's name: Alice
	Enter player 2's name: Bob
	Enter player 3's name: Charlie
	Enter player 4's name: Delilah
```

4. When prompted, specify whether you would like to randomize the starting player.  Type "yes" or "y" to pick a random starting player, while keeping the same direction of play (CW or CCW).  Type "no" or "n" to keep the same starting player you specified in step 3.  E.g.:

```
	Randomly pick starting player? y
	Player order is now: Bob, Charlie, Delilah, Alice
```

5. Lay out your starting settlements and roads as usual.  When ready, hit Return/Enter to roll.  Repeat roll until game ends.
