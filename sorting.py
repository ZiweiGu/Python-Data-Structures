# An experiment on the performance of various sorting algorithms
import heapq

def suck_sort(lst):
	"""
	A most naive sorting algorithm.
	Everyone should be able to implement one in a minute.
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
	ans = []
	while lst:
		ans.append(heapq.heappop(lst))
	return ans


def merge_sort(lst):
	pass



if __name__ == '__main__':
	print(heap_sort([1,3,5,4,2,7,8,8,6,8,5,3,1,9]))