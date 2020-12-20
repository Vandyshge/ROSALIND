import re

def main():
	inp = open('rosalind_prtm.txt', 'r')
	s = inp.read().strip()
	inp.close()
	alf_in = open('CPM_AL.txt', 'r')
	alf = {}
	for string in alf_in:
		string = string.strip().split()
		alf[string[0]] = float(string[1])
	alf_in.close()
	# print(alf)
	mass = 0
	for let in s:
		mass += alf[let]
	out = open('CPM_out.txt', 'w')
	out.write(f'{mass:.3f}')
	out.close()

main()