from random import randint



class SelectionSort:
    @staticmethod
    def find_smallest(arr) -> int:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

    def selection_sort(self, arr):
        new_arr = []
        for i in range(len(arr)):
            smallest = self.find_smallest(arr)
            new_arr.append(arr.pop(smallest))
        return new_arr


LEN = 10
MIN = 0
MAX = 100


sorter = SelectionSort()

unsorted_list = [randint(MIN, MAX) for _ in range(LEN)]
for index, value in enumerate(unsorted_list):
    print(f'Index: {index} Value: {value}')
print()
print(f'The complete list is {unsorted_list}')

print()

sorted_list = sorter.selection_sort(unsorted_list)
for index_1, value_1 in enumerate(sorted_list):
    print(f'Index: {index_1} Value: {value_1}')
print()
print(f'The complete sorted list is {sorted_list}')

