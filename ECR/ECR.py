def hemming(s1, s2):
    hemm = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hemm += 1
    return hemm

def change(s):
    s = s.replace('A', 'x').replace('T', 'A').replace('x', 'T')
    s = s.replace('C', 'x').replace('G', 'C').replace('x', 'G')
    return s

def revers(s):
    return s[::-1]

def obr(s):
    return revers(change(s))

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
    main_strings = []
    data1 = []
    for head, string in data:
        if string not in main_strings and obr(string) not in main_strings:
            for head_i, string_i in data:
                if head != head_i and string_i not in main_strings and obr(string_i) not in main_strings:
                    # print(f'{string} --- {string_i} or {obr(string_i)}')
                    if string == string_i or string == obr(string_i):
                        main_strings.append(string)
                        # print(main_strings)
                        break
                    # print(2)
            # print('-----------------------------------------------------------------------------------')
    for head, string in data:
        if string not in main_strings and obr(string) not in main_strings:
            data1.append(string)

    # print(data1)
    # print(main_strings)

    out = open('ECR_out.txt', 'w')
    for main_string in main_strings:
        for string in data1:
            if hemming(main_string, string) == 1:
                print(f'{string}->{main_string}')
                out.write(f'{string}->{main_string}\n')
            elif hemming(obr(main_string), string) == 1:
                print(f'{string}->{obr(main_string)}')
                out.write(f'{string}->{obr(main_string)}\n')
    out.close()


main('rosalind_corr (1).txt')