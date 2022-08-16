def bubble_sort(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                yield lst
