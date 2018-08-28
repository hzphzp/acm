def bijective(B):
    f = True
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            if B[i] == B[j]:
                f = False
    return f


n = input()
B = input()
B = B.split(" ")
B = [int(x) for x in B]
print(bijective(B))
