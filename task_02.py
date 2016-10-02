def sort_array(data, x, y, row_len):
    work_array = [0] * row_len
    new_array = []
    i = 0
    while i < row_len:
        if data[x][i] != 0:
            work_array[data[x][i]-1] = data[y][i]
        i += 1

    i = 0
    while i < row_len:
        if work_array[i] != 0:
            new_array.append(work_array[i])
        i += 1
    return new_array


def merge(movie_set, begin, mid, end, sorted_set, is_uno):
    n = begin
    m = mid
    inversions = 0

    while n < end:
        if begin < mid and (m >= end or ((is_uno and movie_set[begin] <= movie_set[m]) or (not is_uno and movie_set[begin][1] <= movie_set[m][1]))):
            sorted_set[n] = movie_set[begin]
            begin += 1
        else:
            # if is_uno and movie_set[m] != 0:
            inversions += (mid - begin)
            sorted_set[n] = movie_set[m]
            m += 1

        n += 1

    return inversions


def merge_sort(user_set, begin, end, sorted_set, is_uno):
    if (end - begin) < 2:
        return 0
    inversions = 0
    mid = int((begin + end) / 2)
    inversions += merge_sort(sorted_set, begin, mid, user_set, is_uno)
    inversions += merge_sort(sorted_set, mid, end, user_set, is_uno)
    inversions += merge(user_set, begin, mid, end, sorted_set, is_uno)

    return inversions


def count_inversions(data, x):
    i = 0
    inversions = []
    while i < len(data):
        if i != x:
            sorted_array = sort_array(data, x, i, len(data[0]))
            inversions.append([i, merge_sort(sorted_array, 0, len(sorted_array), sorted_array.copy(), True)])
        i += 1

    merge_sort(inversions.copy(), 0, len(inversions), inversions, False)

    return inversions
