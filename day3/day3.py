import string
from pathlib import Path

POINTS = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))
GROUP_DIM = 3

def parse_input() -> str:

	INPUT_FILE = Path(__file__).parent / 'input.txt'
	common_items = '' #Holds items in common in a single backpack

	with open(INPUT_FILE, 'r') as f:
		data = [line.strip() for line in f]

	return data

def solve_part_1(data: list[str]) -> str:

	common_items = ''
	for line in data:
		common_items += get_common_item(line)
	return common_items

def get_common_item(line: str) -> str:
	
	halfway = len(line)//2
	s1, s2 = set(line[:halfway]), set(line[halfway:])
	common_letter = s1.intersection(s2)
	if len(common_letter) != 1:
		raise ValueError(f"Expected only one item in commom between the two backpack compartments, not {len(common_letter)}") 
	return common_letter.pop()	

def solve_part_2(data: list[str]) -> str:

	badges = ''
	
	for i in range(0,len(data),3):
		s1, s2, s3 = set(data[i]), set(data[i+1]), set(data[i+2])
		badge = s1.intersection(s2, s3)
		if len(badge) != 1:
			raise ValueError(f"Expected only one item in commom between the two backpack compartments, not {len(badge)}") 
		badges += badge.pop()

	return badges

def main():
	data = parse_input()
	common_items = solve_part_1(data)
	points = sum(map(POINTS.get, common_items))
	print(f"The solution to part 1 is {points}")

	badges = solve_part_2(data)
	points = sum(map(POINTS.get, badges))
	print(f"The solution to part 2 is {points}")

if __name__ == '__main__':
	main()
