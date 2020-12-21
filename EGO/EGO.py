import numpy

def rec(use, n, s):
    for j in range(1, n + 1):
        if j not in use:
            use.append(j)
            if len(use) == n and f'{s}{j}' not in res:
                res.append(''.join(map(str, use)))
            else:
                rec(use, n, f'{s}{j}')
            use.remove(j)
    

def main(file_name):
    inp = open(f'{file_name}', 'r')
    n = int(inp.readline().strip())
    inp.close()
    n1 = numpy.math.factorial(n)
    print(n1)

    use = []
    s = ''
    global res
    res = []
    for i in range(1, n + 1):
        use.append(i)
        rec(use, n, s)
        use.remove(i)
    print(res)
    print(len(set(res)))

    out = open('EGO_out.txt', 'w')
    out.write(f'{n1}\n')
    for elem in res:
        out.write(f'{" ".join(elem)}\n')
    out.close()


main('rosalind_perm (1).txt')