n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(0, len(matrix) - 1):
    for j in range(0, len(row) - i - 1):
        sum1 += matrix[i][j]
for i in range(0, len(matrix)):
    for j in range(n - i , len(row)):
        sum2 += matrix[i][j]
if k >= abs(sum1 - sum2):
    print("YES")
    print(abs(sum1 - sum2))
else:
    print("NO")
    print(abs(sum1 - sum2))
