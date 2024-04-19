
import time
import random

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def time_execution(algorithm, sizes):
    avg_times = []
    for size in sizes:
        total_time = 0
        for _ in range(10):  # Execute each algorithm 10 times and take the average
            arr = generate_random_array(size)
            start_time = time.time()
            algorithm(arr)
            end_time = time.time()
            total_time += (end_time - start_time)
        avg_time = total_time / 10
        avg_times.append(avg_time)
    return avg_times

def sqrtsort_quadratic(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


sizes = [10**4, 10**5, 10**6, 10**7, 10**8]
quadratic_times = time_execution(sqrtsort_quadratic, sizes)
heap_times = time_execution(sqrtsort_heap, sizes)

print("Tamanhos:", sizes)
print("Tempo (quadrático):", quadratic_times)
print("Tempo (heap):", heap_times)
