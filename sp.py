import time

arr = [5, 8, 16, 10, 3, 1, 4]

# ---------------- Sorting Algorithms ----------------

def bubble_sort(a):
    a = a.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(a):
    a = a.copy()
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return left + middle + right

# ---------------- Time Measurement ----------------

def run_sort(sort_func):
    start = time.perf_counter()
    sorted_arr = sort_func(arr)
    end = time.perf_counter()
    print(f"{sort_func.__name__}: {sorted_arr} | Time: {end - start:.6f} seconds")

# ---------------- Run All ----------------

print("Original Array:", arr)
print("-" * 55)

for sort in [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]:
    run_sort(sort)
