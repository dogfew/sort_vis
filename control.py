import pygame

from sorts.quicksort import quick_sort
from sorts.heap_sort import heap_sort
from sorts.insertion_sort import insertion_sort
from sorts.bubble_sort import bubble_sort
from sorts.radix_sort import radix_sort
from sorts.radix_shuffle import radix_shuffle

func = {pygame.K_w: quick_sort,
        pygame.K_a: insertion_sort,
        pygame.K_d: heap_sort,
        pygame.K_e: radix_sort,
        pygame.K_x: bubble_sort,
        pygame.K_z: radix_shuffle}
default_func = lambda x: iter([x])
