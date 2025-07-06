import random
import matplotlib.pyplot as plt

def linear_search_with_count(sequence, key):
    comparisons = 0
    for item in sequence:
        comparisons += 1
        if item == key:
            return comparisons
    return comparisons

input_sizes = [100, 500, 1000, 5000, 10000]
best_comparisons = []
average_comparisons = []
worst_comparisons = []

for n in input_sizes:
    sequence = random.sample(range(1, n * 10), n)

    best_case_key = sequence[0]
    average_case_key = sequence[n // 2]
    worst_case_key = -1

    best_comparisons.append(linear_search_with_count(sequence, best_case_key))
    average_comparisons.append(linear_search_with_count(sequence, average_case_key))
    worst_comparisons.append(linear_search_with_count(sequence, worst_case_key))

print(f"{'Input Size':<10} {'Best Case':<12} {'Average Case':<14} {'Worst Case':<12}")
for i in range(len(input_sizes)):
    print(f"{input_sizes[i]:<10} {best_comparisons[i]:<12} {average_comparisons[i]:<14} {worst_comparisons[i]:<12}")

plt.plot(input_sizes, best_comparisons, marker='o', label='Best Case (O(1))', color='green')
plt.plot(input_sizes, average_comparisons, marker='o', label='Average Case (O(n/2))', color='orange')
plt.plot(input_sizes, worst_comparisons, marker='o', label='Worst Case (O(n))', color='red')
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons")
plt.title("Linear Search: Number of Comparisons vs Input Size")
plt.legend()
plt.grid(True)
plt.show()
