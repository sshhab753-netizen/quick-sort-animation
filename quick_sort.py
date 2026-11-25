def quick_sort(a):
    sort(a, 0, len(a) - 1)

def sort(a, lo, hi):
    if lo >= hi:
        return
    p = partition(a, lo, hi)
    sort(a, lo, p - 1)
    sort(a, p + 1, hi)

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
