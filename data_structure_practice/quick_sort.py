def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        smaller = [i for i in arr if i <=  pivot]

        greater = [i for i in arr if i > pivot]

        return quickSort(smaller) + pivot + quickSort(greater)
    

[56,25,68,51,25,48]