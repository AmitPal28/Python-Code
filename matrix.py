'''
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
'''


'''
#Find the sum of maximum value of each rows in a metrix.
def find_max_sum(matrix):
    max_sum = 0
    for row in matrix:
        max_value = max(row)
        max_sum += min_value
    return max_sum

# Input
m, n = map(int, input().split())
matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Output
result = find_max_sum(matrix)
print(result)
'''