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

def prove(s1, s2):
    n = min(len(s1), len(s2))
    s = ''
    for i in range(n//2, n + 1):
        # print(s1[-i:], s2[:i])
        if s1[-i:] == s2[:i]:
            # print(True)
            s = s1[:-i] + s1[-i:] + s2[i:]
            # print(s)
            # print()
    # print(f'this is {s}')
    return s

def main(file_name):
    data = read_fasta(file_name)
    # prove('ATTAGATTAG ', 'AGACCTGCCG')
    res = []
    dstr = {string: [] for head, string in data}
    for head, string in data:
        for head_i, string_i in data:
            if head != head_i and prove(string, string_i) != '':
                dstr[string].append(string_i)
    print(dstr)
    for head, string in data:
        s = '' + string
        use = set()
        use.add(string)
        for i in range(len(data)):
            if len(dstr[string]) != 0:
                string_i = dstr[string][0]
                s = prove(s, string_i)
                use.add(string_i)
                string = string_i
                print(s)
            else:
                break
        if len(use) == len(data):
            res.append(s)
    print(res)
    res = sorted(res, key=lambda x: len(x))[-1]
    print(res)
    out = open('GASS_out.txt', 'w')
    out.write(f'{res}')
    out.close()


main('rosalind_long.txt')
# print(sorted(['res', 'qwer', 'qw', 'ertyyu'], key=lambda x: len(x)))
