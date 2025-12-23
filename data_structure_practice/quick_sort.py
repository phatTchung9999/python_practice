def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        smaller = [i for i in arr[1:] if i <=  pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(smaller) + [pivot] + quickSort(greater)
    

def main():
    print(quickSort([100,45,90,55,23,1,67]))


if __name__ == '__main__':
    main()
