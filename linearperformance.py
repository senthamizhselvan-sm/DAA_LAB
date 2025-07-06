import random
import time
import matplotlib.pyplot as plt

def linear_search(sequence, key):
    for i in range(len(sequence)):
        if sequence[i] == key:
            return i
    return -1

n = 10000
sequence = random.sample(range(1, n * 10), n)

best_case_key = sequence[0]
average_case_key = sequence[n // 2]
worst_case_key = -1

start = time.time()
linear_search(sequence, best_case_key)
end = time.time()
best_time = (end - start) * 1000

start = time.time()
linear_search(sequence, average_case_key)
end = time.time()
average_time = (end - start) * 1000

start = time.time()
linear_search(sequence, worst_case_key)
end = time.time()
worst_time = (end - start) * 1000

print(f"Best Case Time:    {best_time:.4f} ms")
print(f"Average Case Time: {average_time:.4f} ms")
print(f"Worst Case Time:   {worst_time:.4f} ms")

cases = ['Best Case', 'Average Case', 'Worst Case']
times = [best_time, average_time, worst_time]

plt.plot(cases, times, marker='o', linestyle='-', color='blue')
plt.xlabel("Case Type")
plt.ylabel("Time (ms)")
plt.title(f"Linear Search Time Analysis (n = {n})")
plt.grid(True)
plt.show()
