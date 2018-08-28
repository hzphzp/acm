# Complete the countArray function below.
def countArray(n, k, x):
    if (n % 2) == 1:
        count = (x == 1)
        add = k - 2
    if (n % 2) == 0:
        count = (x != 1)
        add = (k - 2) * (k - 1)
    for i in range((n - 3) // 2 + 1):
        count += add
        add *= (k - 1) * (k - 1)
        add = add % 1000000007
        count = count % 1000000007
    return count % 1000000007


print(countArray(17048, 14319, 1))
