N = int(input())
palavra1 = input()

M = int(input())
palavra2 = input()

prefixo_comum = ""
indice = 0

if N > M:
    for letra in palavra2:
        if letra == palavra1[indice]:
            prefixo_comum += letra
            indice += 1
        else:
            break
    
else:
    for letra in palavra1:
        if letra == palavra2[indice]:
            prefixo_comum += letra
            indice += 1
        else:
            break

print(len(prefixo_comum))    