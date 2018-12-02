
n = int(input())
rainhas = [0,0,0,0]

def posicaoValida(x , y):
    global rainhas
    for i in range(x):

        if i == x or rainhas[i] == y:
            #print(x,",",y)
            #print(i,",",rainhas[i])
            return False
        
        if i + rainhas[i] == x+y:
            #print(x,",",y)
            #print(i,",",rainhas[i])
            return False

        if i-rainhas[i] == x-y or rainhas[i]-i == y-x:
            #print(x,",",y)
            #print(i,",",rainhas[i])
            return False

    return True

def backtracking(rainha):
    global n
    global rainhas
    print(rainha)
    for i in range(n):

        if posicaoValida(rainha,i):
            if rainha == n-1:
                #print(rainha)
                #print(rainhas)
                print("POR QUE")
                rainhas[rainha] = i
                print(rainhas)
                exit()
            else:
                #print(rainha)
                #print(rainhas)
                rainhas[rainha] = i
                backtracking(rainha+1)


if backtracking(0):
    print("DEU CERTO")
print(rainhas)
            
