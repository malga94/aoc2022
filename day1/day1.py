from pathlib import Path

def main():
	
	INPUT_FILE = Path(__file__).parent / 'input.txt'
		
	with open(INPUT_FILE, 'r') as f:
		calories = []
		accum = 0
		while line := f.readline():
			if line == '\n':
				#Finished scanning one elf's inventory
				calories.append(accum)
				accum = 0
			else: 
				accum += int(line.strip())
	
	print(f"Solution to part 1: {max(calories)}")
	top3 = sorted(calories)[-3:]
	print(f"Solution to part 2: {sum(top3)}")	
	
if __name__ == '__main__':
	main()		
