import time
import matplotlib.pyplot as plt
def insertion_sort(lst1):
    for i in range(1, len(lst1)):
        key = lst1[i]
        j = i - 1
        while j >= 0 and key < lst1[j]:
            lst1[j + 1] = lst1[j]
            j -= 1
        lst1[j + 1] = key

lst1 = [3, 2, 5, 4, 8]  #n = 5
#lst1 = [3, 2, 5, 4, 8, 6, 10, 9, 7, 1]   #n = 10
#lst1 = [13, 2, 15, 4, 8, 6, 1, 9, 7, 5, 11, 10, 12, 14, 3]  #n = 15
#lst1 = [13, 2, 15, 4, 8, 6, 1, 9, 7, 5, 11, 10, 12, 14, 3, 21, 24, 20 ,19 ,18 ]  #n = 20
input_size = [5, 10, 15, 20]
timetaken = [0.4053, 1.0729, 1.3113, 1.5972]


start = time.time()
insertion_sort(lst1)
end = time.time()

print(f"The sorted array: {lst1}")
print(f"It took {end - start:.10f} seconds for insertion sort")

plt.plot(input_sizes, timetaken, label='Insertion Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.show()

