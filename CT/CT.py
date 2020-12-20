def read(file_name):
    inp = open(f'{file_name}', 'r')
    n = int(inp.readline().strip())
    data = {x: [] for x in range(1, n + 1)}
    for string in inp:
        string = string.strip().split()
        n1, n2 = int(string[0]), int(string[1])
        # print(n1, n2)
        data[n1].append(n2)
        data[n2].append(n1)
    inp.close()
    return data

def main(file_name):
    data = read(file_name)
    res = []
    # print(data)
    data1 = {**data}
    for n in data1:
        s = set(data[n])
        s.add(n)
        # print(s)
        k = True
        for i in range(len(res)):
            if not res[i].isdisjoint(s):
                res[i].update(s)
                k = False
        if k:
            res.append(s)
        # del data[n]
        # print(data)
    # print(res)
    print(len(res) - 1)
    out = open('CT_out.txt', 'w')
    out.write(f'{len(res) - 1}')
    out.close()
                


main('rosalind_tree.txt')
# a = set([1, 2, 3])
# b = set([3, 4, 5])
# c = set([4, 5, 6])
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))
# print(a)
# a = set(a)
# print(a)
# a.add(4)
# print(a)