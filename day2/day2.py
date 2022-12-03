'''
Day 2 of AoC2022
'''

from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'

WINS = {'A':'Y', 'B':'Z', 'C':'X'}
DRAWS = {'A':'X', 'B':'Y', 'C':'Z'}	
LOSSES = {'A':'Z', 'B':'X', 'C':'Y'}
POINTS = {'X':1, 'Y':2, 'Z':3}

DESIRED_RESULT = {'X':LOSSES, 'Y':DRAWS, 'Z':WINS}

def read_input():	

	with open(INPUT_FILE, 'r') as f:
		game_results = map(lambda x: tuple(x.strip().split(' ')), f.readlines())
	return game_results

def column_is_move(moves: list[str]) -> int:

	points = 0   
	for opponent, me in moves:
		#6 points for a win, 3 for a draw
		if WINS[opponent] == me:
			points += 6
		elif DRAWS[opponent] == me:
			points += 3 
		#Plus different points for different moves, as encoded in the POINTS dict
		points += POINTS[me]

	return points  

def column_is_result(moves: list[str]) -> int:
	
	points = 0
	#We need to infer the move to make in order to satisfy the strategy
	for opponent, me in moves:
		
		move = DESIRED_RESULT[me][opponent]
		#Knowing the move chosen, we know how many points we get
		points += POINTS[move] 
		#We also get 6 points for 'Z' (win) and 3 for 'Y' (draw)
		points += ((POINTS[me] + 2) % 3) * 3
	
	return points 

def main():
	
	moves = list(read_input())
	points = column_is_move(moves)
	print(f"Solution to part 1: {points}")
	points = column_is_result(moves)	
	print(f"Solution to part 2: {points}")

if __name__ == '__main__':
	main()
