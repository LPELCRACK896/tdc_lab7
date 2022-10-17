from random import randint
import pandas as pd
n = {}

def getGrafica(n):
    op = 0
    for k in range(1, n+1):
        op += 1
        for i in range(k+1, n+1):
            op += 3
            for j in range(k, n+1):
                op += 5
    return op

x =  [k for k in range(1, 40)]
y =  [getGrafica(k) for k in range(1, 40)]

d = {'n': x, 'f(n)': y}
pd.DataFrame(d).from_dict(d).to_excel('Inciso3.xlsx')