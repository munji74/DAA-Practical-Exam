import time
import matplotlib.pyplot as plt
def selection_sort(lst1):
    for i in range(len(lst1)):
        min_index = i
        for j in range(i + 1, len(lst1)):
            if lst1[j] < lst1[min_index]:
                min_index = j
        lst1[i], lst1[min_index] = lst1[min_index], lst1[i]

lst1 = [3, 2, 5, 4, 8]  #n = 5
#lst1 = [3, 2, 5, 4, 8, 6, 10, 9, 7, 1]   #n = 10
#lst1 = [13, 2, 15, 4, 8, 6, 1, 9, 7, 5, 11, 10, 12, 14, 3]  #n = 15
#lst1 = [13, 2, 15, 4, 8, 6, 1, 9, 7, 5, 11, 10, 12, 14, 3, 21, 24, 20 ,19 ,18 ]  #n = 20

input_size = [5, 10, 15, 20]
timetaken = [0.90599, 1.3828, 1.5974, 2.0505]

start = time.time()
selection_sort(lst1)
end = time.time()

print(f"The sorted array: {lst1}")
print(f"It took {end - start:.10f} seconds for selection sort")



