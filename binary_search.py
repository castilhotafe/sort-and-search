class BinarySearch:


    @classmethod
    def binary_search(cls, sorted_array, item)-> int | None:
        #if the item is the array, the function returns its position
        low = 0
        high = len(sorted_array) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = sorted_array[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None


my_list = [1, 3, 5 , 7 , 9]

print(BinarySearch.binary_search(my_list, 3))

