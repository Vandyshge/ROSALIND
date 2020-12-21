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

def read_al():
    al_inp = open('RNAS_AL.txt', 'r')
    al = {}
    for elem in al_inp:
        elem = elem.strip().split()
        for i in range(0, len(elem), 2):
            al[elem[i]] = elem[i + 1]
    print(al)
    al_inp.close()
    return al

def change_prot(string, al):
    s = ''
    for i in range(0, len(string), 3):
        if al[string[i:i + 3]] != 'Stop':
            s += al[string[i:i + 3]]
    return s

def change_RNA(string):
    return string.replace('T', 'U')

def main(file_name):
    data = read_fasta(file_name)
    al = read_al()
    string = data[0][1]
    data1 = []
    for i in range(1, len(data)):
        data1.append(data[i][1])

    # string = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCC'

    for elem in data1:
        string = string.replace(elem, '')
    string_RNA = change_RNA(string)
    s = change_prot(string_RNA, al)
    print(s)

    out = open('RNAS_out.txt', 'w')
    out.write(f'{s}\n')
    out.close()


main('rosalind_splc.txt')