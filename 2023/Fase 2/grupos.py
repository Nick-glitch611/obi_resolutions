E, M, D = map(int, input().split())

restricoes = 0
duplas_juntas = []
duplas_separadas = []
grupos = {}

for i in range(M):
    dupla = list(map(int, input().split()))
    duplas_juntas.append(dupla)
for i in range(D):
    dupla = list(map(int, input().split()))
    duplas_separadas.append(dupla)

for i in range(E // 3):
    I, J, K = map(int, input().split())
    grupos[I] = i
    grupos[J] = i
    grupos[K] = i

for i in range(len(duplas_separadas)):
    if grupos[duplas_separadas[i][0]] == grupos[duplas_separadas[i][1]]:
        restricoes += 1
    else:
        pass

for i in range(len(duplas_juntas)): 
    if grupos[duplas_juntas[i][0]] != grupos[duplas_juntas[i][1]]:
        restricoes += 1
    else:
        pass

print(restricoes)
