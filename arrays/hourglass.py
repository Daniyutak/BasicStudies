arr =[[1, 2, 3, 4, 5, 6],
      [7,8,9,10,11,12],
      [13,14,15,16,17,18],
      [19,20,21,22,23,24],
      [25,26,27,28,29,30],
      [31,32,33,34,35,36]]

#for j in range (4):
#        for i in range (4):
#            print (f"i: {i}, j: {j}, arr:  {arr[i+2][j+2]}")
#            print("---")

def hourglassSum(arr):
    soma = []
    for j in range (4):
        for i in range (4):
            soma.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    print(soma)


hourglassSum(arr)
