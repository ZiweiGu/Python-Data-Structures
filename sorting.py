# An experiment on the performance of various sorting algorithms
import heapq
import random
import timeit


def suck_sort(lst):
    """
    A most naive sorting algorithm.
    Everyone should be able to implement one in half a minute.
    """
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst


def heap_sort(lst):
    """
    Use the powerful heap data structure to sort (kind of trivial).
    """
    heapq.heapify(lst)
    length = len(lst)
    return [heapq.heappop(lst) for _ in range(length)]


def merge_sort(lst):
    def merge_sort_recur(lst, l, r):
        if l < r:
            mid = (l + r) // 2
            lst = merge_sort_recur(lst, l, mid)
            lst = merge_sort_recur(lst, mid + 1, r)
            merge(lst, l, mid, r)
        return lst

    # def merge_sort_iter(lst):


    def merge(lst, l, mid, r):
        tmp = [None] * (r - l + 1)
        i = l
        j = mid + 1
        k = 0
        while i <= mid and j <= r:
            if lst[i] <= lst[j]:
                tmp[k] = lst[i]
                i += 1
            else:
                tmp[k] = lst[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = lst[i]
            i += 1
            k += 1
        while j <= r:
            tmp[k] = lst[j]
            j += 1
            k += 1
        for i in range(k):
            lst[l + i] = tmp[i]
        return lst

    return merge_sort_recur(lst, 0, len(lst) - 1)


def quick_sort(lst, random=False):
    def quick_sort_recur(lst, l, r):
        if l < r:
            mid = partition(lst, l, r)
            lst = quick_sort_recur(lst, l, mid - 1)
            lst = quick_sort_recur(lst, mid + 1, r)
        return lst

    def partition(lst, l, r):
        pivot = lst[l]
        i = l + 1
        j = r
        while True:
            while i <= j and lst[i] < pivot:
                i += 1
            while j >= i and lst[j] >= pivot:
                j -= 1
            if i > j:
                break
            lst[i], lst[j] = lst[j], lst[i]
        lst[l], lst[j] = lst[j], lst[l]
        return j

    def random_partition(lst, l, r):
        i = random.randint(l, r)
        lst[i], lst[l] = lst[l], slt[i]
        return partition(lst, l, r)

    return quick_sort_recur(lst, 0, len(lst) - 1)


#==================Testing functions===================#

def generate_random_list(n):
    return [random.randrange(-100, 100) for _ in range(n)]


if __name__ == '__main__':
    sort_functions = [suck_sort, heap_sort, merge_sort, quick_sort]
    sort_function_names = ['suck_sort', 'heap_sort', 'merge_sort', 'quick_sort']
    print('Testing correctness - ')
    test_list = generate_random_list(200)
    ans = sorted(test_list)
    for i in range(len(sort_functions)):
        print('Testing {}...'.format(sort_function_names[i]))
        if ans == sort_functions[i](test_list[:]):
            print(sort_function_names[i] + ' seems to be correct!')
        else:
            print(sort_function_names[i] + ' is incorrect!')
    print('Testing performance - ')
    print('Sorting random list of size 10000:')
    print('suck_sort: ' + str(timeit.timeit('suck_sort(lst)', setup='from __main__ import suck_sort, generate_random_list; lst=generate_random_list(10000)', number=1)) + ' s.')
    print('heap_sort: ' + str(timeit.timeit('heap_sort(lst)', setup='from __main__ import heap_sort, generate_random_list; lst=generate_random_list(10000)', number=1)) + ' s.')
    print('merge_sort: ' + str(timeit.timeit('merge_sort(lst)', setup='from __main__ import merge_sort, generate_random_list; lst=generate_random_list(10000)', number=1)) + ' s.')
    print('quick_sort: ' + str(timeit.timeit('quick_sort(lst)', setup='from __main__ import quick_sort, generate_random_list; lst=generate_random_list(10000)', number=1)) + ' s.')
    print('Sorting random list of size 100000:')
    print('heap_sort: ' + str(timeit.timeit('heap_sort(lst)', setup='from __main__ import heap_sort, generate_random_list; lst=generate_random_list(100000)', number=1)) + ' s.')
    print('merge_sort: ' + str(timeit.timeit('merge_sort(lst)', setup='from __main__ import merge_sort, generate_random_list; lst=generate_random_list(100000)', number=1)) + ' s.')
    print('quick_sort: ' + str(timeit.timeit('quick_sort(lst)', setup='from __main__ import quick_sort, generate_random_list; lst=generate_random_list(100000)', number=1)) + ' s.')
    print('Experiment complete.')






