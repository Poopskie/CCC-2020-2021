# tryna make a quick sort
# variables: list, pivot, left_pos, right_pos

def quickSort(lists):
    pivot_pos = len(lists)//2
    pivot = lists[pivot_pos]
    lists[pivot_pos], lists[-1] = lists[-1], lists[pivot_pos]
    # swap the two
    for i in range(len(lists)):
        if lists[i] < pivot:
            left = lists[i]
            break
    for i in range(len(lists)):
        if lists[i] > pivot:
            right = lists[i]





if __name__ == '__main__':
    needs_sort = []
    quickSort(needs_sort)


