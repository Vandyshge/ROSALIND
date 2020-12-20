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
    dic = {}
    al = ['A', 'C', 'G', 'T']
    n = len(data[0][1])
    for let in al:
        dic[let] = [0 for _ in range(n)]
    for i in range(n):
        for j in range(len(data)):
            dic[data[j][1][i]][i] += 1
    string = ''
    for i in range(n):
        s_i = ''
        n_max = 0
        for let in al:
            if dic[let][i] >= n_max:
                s_i = let
                n_max = dic[let][i]
        string += s_i

    print(string)
    for let in al:
        print(f'{let}: {" ".join(map(str, [x for x in dic[let]]))}')
        # print(" ".join(map(str, [0, 1, 2])))

    out = open('CP_out.txt', 'w')
    out.write(f'{string}\n')
    for let in al:
        out.write(f'{let}: {" ".join(map(str, [x for x in dic[let]]))}\n')


main('rosalind_cons.txt')