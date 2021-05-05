x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 11]]
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(0, len(x)):
    for j in range(0, len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for r in result:
    print(r)
