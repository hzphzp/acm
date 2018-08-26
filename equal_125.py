# Complete the equal function below.
def equal(arr):
    arr_sort = sorted(arr)
    step_0 = 0
    step_1 = 0
    step_2 = 0
    for x in arr_sort:
        step_0 = step_0 + count(x - arr_sort[0])
    arr_sort[0] = arr_sort[0] - 1
    step_1 = step_1 + 1
    for x in arr_sort:
        step_1 = step_1 + count(x - arr_sort[0])
    arr_sort[0] = arr_sort[0] - 1
    step_2 = step_2 + 1
    for x in arr_sort:
        step_2 = step_2 + count(x - arr_sort[0])

    return min(step_0, step_1, step_2)
    


def count(surplus: int):
    count_5 = int(surplus/5)
    surplus = surplus - count_5 * 5
    count_2 = int(surplus/2)
    surplus = surplus - count_2 * 2
    count_1 = surplus
    return count_1 + count_2 + count_5


print(equal([1, 5, 5]))
