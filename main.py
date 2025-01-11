import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Array Size': [10000, 20000, 30000, 40000, 70000, 100000],
    'Selection Sort': [17.98, 79.95, 176.75, 330.53, 766.60, 1686.01],
    'Insertion Sort': [20.44, 82.47, 181.10, 326.04, 880.81, 1927.40],
    'Bubble Sort': [54.10, 238.98, 517.91, 929.24, 2701.27, 5283.52],
    'Heap Sort': [0.12, 0.28, 0.45, 0.54, 1.09, 1.47],
    'Merge Sort': [0.12, 0.30, 0.49, 0.63, 1.35, 1.81],
    'Quick Sort': [0.12, 0.26, 0.43, 0.52, 0.95, 1.35],
    'Tree Sort': [0.02, 0.048, 0.08, 0.08, 0.43, 0.40]
}

data_frame = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 10))

for algorithm in data_frame.columns[1:]:
    plt.plot(data_frame['Array Size'], data_frame[algorithm], marker='o', label=algorithm)

# Chart Formatting
plt.ylabel('Time (s)')
plt.xlabel('Array Size')
plt.title('Performance of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
