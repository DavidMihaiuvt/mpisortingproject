import time
import random
import sys

sys.setrecursionlimit(10**7)

# Bubble Sort function
def sort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort function
def sort2(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort function
def sort3(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort function
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_helper(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort_helper(arr, l, m)
        merge_sort_helper(arr, m + 1, r)
        merge(arr, l, m, r)

def sort4(arr):
    merge_sort_helper(arr, 0, len(arr) - 1)

# Quick Sort function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def sort5(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

# Heap Sort function
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def sort6(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Counting Sort function
def sort7(arr):
    output = [0] * len(arr)
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

# Radix Sort function
def sort8(arr):
    def counting_sort(arr, exp):
        output = [0] * len(arr)
        count = [0] * 10
        for i in range(len(arr)):
            index = arr[i] // exp
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(len(arr)):
            arr[i] = output[i]

    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Bucket Sort function
def sort9(arr):
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            temp = bucket[i]
            j = i - 1
            while j >= 0 and temp < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = temp

    n = len(arr)
    bucket_size = 10
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for i in range(n):
        buckets[(arr[i] - min_val) // bucket_size].append(arr[i])
    for bucket in buckets:
        insertion_sort(bucket)
    k = 0
    for i in range(bucket_count):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Shell Sort function
def sort10(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


# Cocktail Shaker Sort function
def sort11(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1


# Comb Sort function
def sort12(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

# Timsort function
def sort13(arr):
    arr.sort()


def create_list_and_print_to_file(filename, list_size):

    num_list = [random.randint(1, 100) for _ in range(list_size)]

    with open(filename, 'w') as file:
        file.write(','.join(map(str, num_list)))

    print("List created and printed to", filename, ":")
    print(num_list)


def read_list_from_file(filename):
    num_list = []

    with open(filename, 'r') as file:
        content = file.read()

        num_list = list(map(int, content.split(',')))

    print("List read from", filename, ":")
    print(num_list)
    return num_list

# Function to measure time taken to sort a list using a given sorting function
def measure_sort_time(sort_func, sort_name):
    random_list = read_list_from_file("list.txt")

    start_time = time.perf_counter()


    sort_func(random_list)


    end_time = time.perf_counter()


    time_taken = end_time - start_time


    print("Sorted List (", sort_name, "):", random_list)
    print("Time taken (", sort_name, "): {:.9f} seconds".format(time_taken))

    with open("data.txt", 'a') as file:
        file.write(sort_name + ',{:.9f},seconds\n'.format(time_taken))





#create_list_and_print_to_file("list.txt",1000000)

measure_sort_time(sort1, "Bubble Sort")
measure_sort_time(sort2, "Selection Sort")
measure_sort_time(sort3, "Insertion Sort")
measure_sort_time(sort4, "Merge Sort")
measure_sort_time(sort5, "Quick Sort")
measure_sort_time(sort6, "Heap Sort")
measure_sort_time(sort7, "Counting Sort")
measure_sort_time(sort8, "Radix Sort")
measure_sort_time(sort9, "Bucket Sort")
measure_sort_time(sort10, "Shell Sort")
measure_sort_time(sort11, "Cocktail Shaker Sort")
measure_sort_time(sort12, "Comb Sort")
measure_sort_time(sort13, "Timsort")

