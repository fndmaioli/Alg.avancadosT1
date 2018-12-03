s = input().strip().split(' ')
f = input().strip().split(' ')

def guloso(s,f,n):
    i = 0
    s.insert(0,float('-inf'))
    f.insert(0,float('-inf'))
    n = n + 1
    res = []
    for k in range(1,n):
        if float(s[k]) > float(f[i]):
            res.append((s[k],f[k]))
            i = k
    return res

res = guloso(s,f,len(s))
print(res)