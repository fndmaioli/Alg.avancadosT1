n = int(input())
rainhas = [0] * n

def posicaoValida(x , y):
    global rainhas
    for i in range(x):
        if i == x or rainhas[i] == y:
            return False
        if i + rainhas[i] == x+y:
            return False
        if i-rainhas[i] == x-y or rainhas[i]-i == y-x:
            return False
    return True

def backtracking(rainha):
    global n
    global rainhas
    for i in range(n):

        if posicaoValida(rainha,i):
            if rainha == n-1:
                rainhas[rainha] = i
                print(rainhas)
                return True
            else:
                rainhas[rainha] = i
                backtracking(rainha+1)

backtracking(0)