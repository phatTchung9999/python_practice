def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        elif arr[mid] < item:
            low = mid + 1

def main():
    myList = [1,2,3,4,5,6,7,8,9,10]
    indexOfItem = binary_search(myList, 9)
    if indexOfItem is not None:
        print(indexOfItem)
    else:
        print('The item you looking for is not in the list')


if __name__ == '__main__':
    main()