def hemming(s1, s2):
    hemm = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hemm += 1
    return hemm / len(s1)

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
    res = [[-1 for _ in range(len(data))] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            if res[i][j] == -1:
                res[i][j] = hemming(data[i][1], data[j][1])
                res[j][i] = hemming(data[i][1], data[j][1])


    for string in res:
        for elem in string:
            print(f'{elem:.5f}', end=' ')
        print()

    out = open('CMD_out.txt', 'w')
    for string in res:
        for elem in string:
            out.write(f'{elem:.5f} ')
        out.write('\n')
    out.close()


main('rosalind_pdst (1).txt')