#IN : Número inteiro positivo, n
#OUT: Verdadeiro se n for um quadrado perfeito e falso do contrário
#OBS: Não utilizar operadores ou funções que retornem números reais

def quadperf(n, i):
        if i * i == n :
            return True
        elif i * i > n:
            return False
        else:
            return quadperf(n, i+1)

def exeQuadPerf(n):
    return quadperf(n, 1)

print(exeQuadPerf(12))
print(exeQuadPerf(16))
print(exeQuadPerf(25))
print(exeQuadPerf(5))