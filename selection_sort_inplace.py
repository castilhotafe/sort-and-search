from random import randint

class SelectionSortIn:
    @staticmethod
    def find_smallest_from_index(arr, start_index) -> int:
        smallest = arr[start_index]
        smallest_index = start_index
        for current_index in range(start_index + 1, len(arr)):
            if arr[current_index] < smallest:
                smallest = arr[current_index]
                smallest_index = current_index
        return smallest_index

    def selection_sort(self, arr):
        for current_index in range(len(arr)):

            smallest_index = self.find_smallest_from_index(arr, current_index)

            temp = arr[current_index]
            arr[current_index] = arr[smallest_index]
            arr[smallest_index] = temp

        return arr




LEN = 10
MIN = 0
MAX = 100

sorter = SelectionSortIn()

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