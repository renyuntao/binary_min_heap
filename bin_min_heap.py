#!/usr/bin/env python
import math
def heap_insert(heap,value):
	heap.append(value)
	length = len(heap)
	child_i = length - 1
	parent_i = math.floor((child_i-1)/2)
	while True:
		if parent_i >= 0:    #exist parent
			if heap[parent_i] > heap[child_i]:    #need swap
				t = heap[parent_i]
				heap[parent_i] = heap[child_i]
				heap[child_i] = t
				child_i = parent_i
				parent_i = math.floor((child_i-1)/2)
			else:
				break
		else:
			break
def heap_remove(heap):
	if len(heap) > 1:
		heap[0] = heap.pop()
	elif len(heap) == 1:
		heap.pop()
	else:
		print('heap is empty!')
	parent_i = 0
	p = parent_i
	length = len(heap)
	while True:
		l_child,r_child = parent_i*2+1,parent_i*2+2
		if l_child < length and heap[parent_i] > heap[l_child]:
			p = l_child
		if r_child < length and heap[p] > heap[r_child]:
			p = r_child
		if p != parent_i:    #need swap
			t = heap[p]
			heap[p] = heap[parent_i]
			heap[parent_i] = t
			parent_i = p
		else:
			break

