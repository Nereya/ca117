def partition(lst, lo, hi):
    #pivot = sorted(lst)[len(lst)//2] hey there
    #pivot_index = lst.index(pivot)
    #lst[pivot_index], lst[len(lst)//2] = lst[len(lst)//2], lst[pivot_index]
    pivot = hi      #this needs to be an index, not an element
    divider = lo

    for i in range(lo, hi+1):
        if lst[i] < lst[pivot]:
            lst[i], lst[divider] = lst[divider], lst[i]
            divider += 1
    if lo < hi:
        lst[pivot], lst[divider] = lst[divider], lst[pivot]
    return divider

def r_quick_sort(lst, lo, hi):

   if lo - hi > 0:
       pivot = partition(lst, lo, hi)
       r_quick_sort(lst,lo,pivot - 1)
       r_quick_sort(lst, pivot + 1, hi)

def quick_sort(lst):
    r_quick_sort(lst, 0, len(lst)-1)

lst = [4,1,9,0,4,5,11]
print lst
print(quick_sort(lst))
