def main():
	inp = open('rosalind_revp.txt', 'r')
	s_i = inp.readline()
	s_i = inp.readline().strip()
	s = ''
	res = []
	while s_i != '':
		s += s_i
		s_i = inp.readline().strip()
	print(s)
	for i in range(len(s)):
		if (len(s) - i) < 12:
			s_i = s[i:]
			# print(f'1 --- {s_i} --- {len(s_i)}')
		else:
			s_i = s[i:i + 12]
			# print(f'0 --- {s_i} --- {len(s_i)}')
		lenth = search(s_i)
		for elem in lenth:
			res.append((i + 1, elem))
	inp.close()
	return res

def search(s):
	lenth = []
	for i in range(4, len(s) + 1):
		s_i = s[:i]
		# print(s_i)
		if prove(s_i):
			# print(1)
			lenth.append(i)
	return lenth

def change(s):
	s = s.replace('A', 'x').replace('T', 'A').replace('x', 'T')
	s = s.replace('C', 'x').replace('G', 'C').replace('x', 'G')
	return s

def revers(s):
	return s[::-1]

def obr(s):
	return revers(change(s))

def prove(s):
	if s == obr(s):
		return True
	else:
		return False

def output(s):
	res = main()
	out = open('LRS_out.txt', 'w')
	for i, n in res:
		out.write(f'{i} {n}\n')
	out.close()



s = 'GCATGC'
# s = 'CATG'
# print(f'{s} ---> {obr(s)}, it\'s meaning {prove(s)}')
output(s)
# print(search(s))
