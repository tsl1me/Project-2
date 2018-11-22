import Local
import os

while(True):
	tops = list()
	print(Local.INPUT_NAMES_OF_TOPS)
	for top in input().split(" "):
		if top in tops:
			print(top + " " + Local.THIS_TOP_ALREADY_EXISTS)
			continue
		tops.append(top)
	break

TREE = { top : list() for top in tops}
TREE_wheight = { top : 0 for top in tops}
end_case = Local.END_CASE

print(Local.INPUT_DESCENDANTS % (end_case))
while(True):
	str_to_parse = input()
	if str_to_parse == end_case:
		break
	key, descendant = map(str, str_to_parse.split(" "))
	if descendant not in TREE:
		print(Local.THIS_TOP_DOESNT_EXISTS)
		continue
	TREE[key].append(descendant)


while(True):
	start = input(str(Local.INPUT_START))
	if start not in TREE:
		print(Local.THIS_TOP_DOESNT_EXISTS)
		continue
	end = input(str(Local.INPUT_END))
	if end not in TREE:
		print(Local.THIS_TOP_DOESNT_EXISTS)
		continue
	break

current_start = start
previous_start = start
while(True):
	try:
		for element in TREE[current_start]:
			TREE_wheight[element] += 1
		if len(TREE[current_start]) == 0:
			current_start = previous_start
		previous_start = current_start
		current_start = TREE[current_start].pop(0)
	except(IndexError):
		break

print(Local.COUNT_OF_WAYS % (start, end) + " " + str(TREE_wheight[end]))
os.system('PAUSE')
