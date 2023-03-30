
def IsSymmetric(A):
    "Симметричность, делали на семинаре, получила балл за этот семинар"
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[i][j] != A[j][i]:
                return "NO"
    return "YES"
