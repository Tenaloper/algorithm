n = int(input())
res = n

for _ in range(n):
    w = input()
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            pass
        elif w[i] in w[i+2:]:
            res -= 1
            break
print(res)