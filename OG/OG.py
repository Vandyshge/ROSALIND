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
                data.append((s_head[1:], s))
                s = ''
                s_head = string
        else:
            s += string
    data.append((s_head[1:], s))
    return data

def main(file_name):
    data = read_fasta(file_name)
    print(data)
    res = {x[0]: [] for x in data}
    print(res)
    for head, string in data:
        for head_i, string_i in data:
            # print(string[-3:])
            if head != head_i and string[-3:] == string_i[:3]:
                # print(f'{string[-3:]} === {string_i[:3]}')
                # print()
                res[head].append(head_i)
    out = open('OG_out.txt', 'w')
    for head in res:
        for head_i in res[head]:
            print(f'{head} {head_i}')
            out.write(f'{head} {head_i}\n')
    out.close()


main('rosalind_grph.txt')
