from bisect import bisect_left

def insertion_sort(lst):
    sorted_seq = []
    for index, item_1 in enumerate(lst):
        coord = bisect_left(sorted_seq, item_1)
        sorted_seq.insert(coord, item_1)
        yield lst[index:] + sorted_seq
    yield sorted_seq