import random
import timeit

def insertion_sort(data):
    for i in range(1, (len(data))):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

if __name__ == '__main__':

    input_sizes =[10,25,50,60, 70, 75, 80, 90,100]
    merge_sort_times = []
    insertion_sort_times = []

    for n in input_sizes:
        arr = [random.randint(0, 1000) for _ in range(n)]

        merge_sort_time = round(timeit.timeit(lambda: merge_sort(arr.copy()), number=1000), 5)
        merge_sort_times.append(merge_sort_time)

        insertion_sort_time = round(timeit.timeit(lambda: insertion_sort(arr.copy()), number=1000), 5)
        insertion_sort_times.append(insertion_sort_time)

    print("Merge Sort Times: ", merge_sort_times)
    print("Insertion Sort Times: ", insertion_sort_times)