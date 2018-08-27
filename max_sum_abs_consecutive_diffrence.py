# Complete the cost function below.
def cost(B):
    last_low = abs(B[0] - 1)
    last_high = abs(B[1] - 1)
    for i in range(2, len(B)):
        this_low = max(last_high + B[i - 1] - 1, last_low)   
        this_high = max(last_high + abs(B[i - 1] - B[i]), last_low + B[i] - 1)
        last_low = this_low
        last_high = this_high
    return max(this_high, this_low)


"""def recersion(B, index, value):
    if (index == 1):
        return max(abs(value - B[0]), value - 1)
    if (index <= 0):
        return 0
    result = max(
        recersion(B, index - 1, 1) + abs(value - 1),
        recersion(B, index - 1, B[index - 1]) + abs(value - B[index - 1]))
    return result
"""

print(cost([4, 7, 9]))
test = "69 19 15 81 93 100 35 18 81 16 65 20 4 45 81 83 90 14 82 85 43 7 64 76 33 47 95 12 78 93 14 22 97 36 65 66 36 26 59 81 81 82 44 79 89 94 32 94 22 33 19 46 46 62 19 47 70 91 97 62 17 43 11 25 74 73 64 98 73 7 40 8 2 96 89 81 80 17 88 13 31 44 64".split(" ")
test = [int(x) for x in test]
print(cost(test))
