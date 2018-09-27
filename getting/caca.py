'''
Created on 26/09/2018

@author: ernesto
'''

# XXX: http://codeforces.com/contest/991/problem/B

if __name__ == '__main__':
    tope = 5
    n = int(input())
    a = [int(x) for x in input().strip().split(" ")]
    a_tam = len(a)
    assert a_tam == n
    
    min_necesario = 4.5 * a_tam
    suma_actual = sum(a)
    faltante = min_necesario - min(min_necesario, suma_actual)
    r = 0
    a = list(sorted(a))
    while faltante:
        assert r < a_tam
        faltante -= min(faltante, tope - a[r])
        r += 1

    print("{}".format(r)) 
