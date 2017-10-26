# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:13:28 2016

@author: moyuyu
"""

def quick_sort(lists, low, high):
    #快速排序
    i = low
    j = high
    if i >= j:
        return lists
    key = lists[i]
    while i < j:
        while i < j and lists[j] >= key:
            j = j-1
        lists[i] = lists[j]
        while i < j and lists[i] <= key:
            i = i+1
        lists[j] = lists[i]
    lists[i] = key
    quick_sort(lists, low, i-1)
    quick_sort(lists, j+1, high)
    return lists



def insert_sort(lists):
    #插入排序
    count = len(lists)
    for i in range(1, count):       
        j = i - 1
        key = lists[i]
        while j >= 0:
            if lists[j] > key:            
                lists[j+1], lists[j] = lists[j], key
            j -= 1
    return lists



def shell_sort(lists):
    #希尔排序
    count = len(lists) 
    group = count // 2
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group], lists[k] = lists[k], key
                    k -= group
                j += group
        group //= 2
    return lists
        
 
 
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
 
 
 
 def select_sort(lists):
     count = len(lists)
     for i in range(0, count):
         min = i
         for j in range(i + 1, count):
             if lists[min] > lists[j]:
                 min = j
         lists[min], lists[i] = lists[i], lists[min]
     return lists

#堆排序
#选出最大的数
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size // 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i], = lists[i], lists[max]
            adjust_heap(lists, max, size)

#建立堆           
def build_heap(lists, size):
    for i in range(0,(size//2))[::-1]:
        adjust_heap(lists, i, size)

#将最大的值放在最后      
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0,size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
        

#归并排序
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

#直接调用heapq.merge函数实现归并排序
import heapq

def merge_sort(seq):
 if len(seq) <= 1:
     return seq 
 middle = len(seq)//2
 left = merge_sort(seq[:middle])
 right = merge_sort(seq[middle:])
 return list(heapq.merge(left, right))
 



       