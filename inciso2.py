from random import randint, uniform
from time import time
import pandas as pd

def averageTimeSuma(N: int, digitos: int = 1):
    if digitos<1: return None
    limite_inf = 10**(digitos-1) 
    limite_sup = 10**(digitos)-1
    a = randint(limite_inf, limite_sup)
    b = randint(limite_inf, limite_sup)
    start = time()
    for i in range(1, N): a+b
    return (time()-start)/N

def averageTimeDivision(N: int, digitos: int = 1):
    if digitos<1: return None
    limite_inf = 10**(digitos-1) 
    limite_sup = 10**(digitos)-1
    a = randint(limite_inf, limite_sup)
    b = randint(limite_inf, limite_sup)
    start = time()
    for i in range(1, N): a/b
    return (time()-start)/N

def averageTimeSumaF(N: int, digitos: int = 1):
    if digitos<1: return None
    limite_inf = 10**(digitos-1) 
    limite_sup = 10**(digitos)-1
    a = uniform(limite_inf, limite_sup)
    b = uniform(limite_inf, limite_sup)
    start = time()
    for i in range(1, N): a+b
    return (time()-start)/N

repeatedExperimentSuma = lambda  k, N, digitos: [averageTimeSuma(N, digitos) for i in range(k)]      
repeatedExperimentSumaF = lambda  k, N, digitos: [averageTimeSumaF(N, digitos) for i in range(k)]      
repeatedExperimentDivision = lambda  k, N, digitos: [averageTimeDivision(N, digitos) for i in range(k)]      

list_digitos = [1, 5, 10, 15]
df_suma = {f'Suma Digitos Int {digitos}': repeatedExperimentSuma(k = 10 , N = 10**5, digitos = digitos) for digitos in list_digitos}
df_suma_f = {f'Suma Digitos Flaot {digitos}': repeatedExperimentSumaF(k = 10 , N = 10**5, digitos = digitos) for digitos in list_digitos}
df_division = {f'Division Digitos Int {digitos}': repeatedExperimentDivision(k = 10 , N = 10**5, digitos = digitos) for digitos in list_digitos}
df_final = df_division | df_suma | df_suma_f
pd.DataFrame.from_dict(df_final).to_excel('Resultados.xlsx')