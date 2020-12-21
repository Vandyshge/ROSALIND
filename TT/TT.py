def hemming(s1, s2):
    transit = 0
    transver = 0
    for i in range(len(s1)):
        if set([s1[i], s2[i]]) == set(['A', 'G']) or set([s1[i], s2[i]]) == set(['C', 'T']):
            transit += 1
        elif s1[i] != s2[i]:
            transver += 1
    return transit / transver

# GC A GC C A C T GG A T T TG A T AA G CA CAACCCA T
# TT T TG A G G C AC G A C GC G C CG A TG TCCTTTG G
# 2122221211212122112111112211112
# 31
# 14
# 17

def read_fasta(file_name):
    inp = open(f'{file_name}', 'r')
    data = []
    s_head = ''
    s = ''
    for string in inp:
        string = string.strip()
        if string[0] == '>':
            if s_head == '':
                s_head = string
            else:
                data.append((s_head, s))
                s = ''
                s_head = string
        else:
            s += string
    data.append((s_head, s))
    inp.close()
    return data

def main(file_name):
    data = read_fasta(file_name)
    
    res = hemming(data[0][1], data[1][1])

    print(f'{res:.11f}\n')

    out = open('TT_out.txt', 'w')
    out.write(f'{res:.11f}\n')
    out.close()


main('rosalind_tran.txt')