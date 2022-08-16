def partition(lst, stack, left, right, index, max_index):
    zeros, ones = [], []
    for element in lst[left:right]:
        string = bin(element)[2:].zfill(max_index)
        if string[index] == '0':
            zeros.append(element)
        else:
            ones.append(element)
    lst[left:right] = zeros + ones
    if zeros:
        stack.append((left, left + len(zeros), index - 1))
    if ones:
        stack.append((left + len(zeros), right, index - 1))


def radix_shuffle(lst):
    left, right, max_index = 0, len(lst), len(bin(max(lst))) - 2
    stack = [(left, right, max_index - 1)]
    while stack:
        left, right, index = stack.pop(-1)
        if index >= 0:
            partition(lst, stack, left, right, index, max_index)
            yield lst
