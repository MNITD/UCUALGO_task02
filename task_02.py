def sort_matrix(matrix, x, row_len):
    i = 0
    while i < row_len:

        if matrix[x][i] != (i + 1):

            u = 0
            c = matrix[x][i] - 1
            while u < len(matrix):
                temp = matrix[u][c]
                matrix[u][c] = matrix[u][i]
                matrix[u][i] = temp
                u += 1
        else:
            i += 1

def merge(movie_set, begin, mid, end, sorted_set, is_uno):
    n = begin
    m = mid
    inversions = 0

    while n < end:
        if begin < mid and (m >= end or ((is_uno and movie_set[begin] <= movie_set[m]) or(not is_uno and movie_set[begin][1] <= movie_set[m][1] ))):
            sorted_set[n] = movie_set[begin]
            begin += 1
        else:
            sorted_set[n] = movie_set[m]
            m += 1
            inversions += (mid - begin)
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
    sort_matrix(data, x, len(data[0]))
    i = 0
    inversions = []
    while i < len(data):
        if i != x:
            inversions.append([i, merge_sort(data[i].copy(), 0, len(data[i]), data[i].copy(), True)])
        i += 1

    merge_sort(inversions.copy(), 0, len(inversions), inversions, False)
    # i = 1
    # while i < len(inversions):
    #     temp = inversions[i]
    #     j = i
    #     while j > 0 and inversions[j - 1][1] > temp[1]:
    #         inversions[j] = inversions[j - 1]
    #         j -= 1
    #     inversions[j] = temp
    #     i += 1

    return inversions

print(count_inversions([[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
  [2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
  [2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
  [3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
  [7, 3, 8, 6, 5, 4, 10, 1, 2, 9]],1))

print(count_inversions([[1,2,3,4,5,6,7,8,9,10],
                        [1,2,3,4,5,6,7,8,9,10],
                        [1,2,3,4,5,6,7,8,9,10],
                        [1,2,3,4,5,6,7,8,9,10],
                        [1,2,3,4,5,6,7,8,9,10]],0))