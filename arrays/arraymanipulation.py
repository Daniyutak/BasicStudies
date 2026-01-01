#n = tamanho do array
#m = numero de queries
#k é o valor a ser colocado em cada posicao do array
#a e b são as posiçoes iniciais e finais a serem somadas com k

def arrayManipulation(n, queries):
    arr = []
    for i in range(n):
        arr.append(0)
    
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range(a-1, b):
            arr[j] += k
        

    return max(arr)


queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100], [3, 4, 100]]
n = 5
m = 3

res = arrayManipulation(n, queries)
print (res)