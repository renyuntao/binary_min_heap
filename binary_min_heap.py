#!/usr/bin/env python
import math
input_ = [int(num) for num in input().split()]    #the number that will insert into binary min-heap later
bin_heap = []
count = 0
for digit in input_:
    if digit != 0:      # non-zero value denote insert value into binary min-heap.0 denote remove root node from binary min-heap
        bin_heap.append(digit)
        count += 1
        child_i = count - 1
        parent_i = math.floor((child_i-1)/2)
        while True:
            if parent_i >= 0:   #exist parent
                if bin_heap[parent_i] > bin_heap[child_i]:   #need swap
                    t = bin_heap[parent_i]
                    bin_heap[parent_i] = bin_heap[child_i]
                    bin_heap[child_i] = t
                    child_i = parent_i
                    parent_i = math.floor((child_i-1)/2)
                else:
                    break
            else:
                break
    else:    #remove minimum element from bin_heap
        bin_heap[0] = bin_heap.pop()
        count -= 1
        parent_i = 0
        p = parent_i
        while True:
            l_child,r_child = parent_i*2+1,parent_i*2+2
            if l_child < count and bin_heap[parent_i] > bin_heap[l_child]:
                p = l_child
            if r_child < count and bin_heap[p] > bin_heap[r_child]:
                p = r_child
            if p != parent_i:    #need swap
                t = bin_heap[p]
                bin_heap[p] = bin_heap[parent_i]
                bin_heap[parent_i] = t
                parent_i = p
            else:
                break
print(*bin_heap)   # print binary min-heap
