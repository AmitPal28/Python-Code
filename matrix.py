
#Find the sum of minimum value of each rows in a metrix.
def find_min_sum(matrix):
    min_sum = 0
    for row in matrix:
        min_value = min(row)
        min_sum += min_value
    return min_sum

# Input
M, N = map(int, input().split())
matrix = []

for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Output
result = find_min_sum(matrix)
print(result)