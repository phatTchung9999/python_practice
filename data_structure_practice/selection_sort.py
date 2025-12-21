d = {'A': 230, 'B': 100, 'C': 500}

listOfValues = list(d.values())

def lookForMin(arr):
    min = arr[0]
    index = 1
    while index < len(arr):
        if min > arr[index]:
            min = arr[index]
        index += 1
    return min



def lookForMax(arr):
    max_val = arr[0]
    index = 1
    while index < len(arr):
        if max_val < arr[index]:
            max_val = arr[index]
        index += 1 
    return max_val
    

if __name__ == '__main__':
    min_value = lookForMin(listOfValues)
    print(min_value)
    max_value = lookForMax(listOfValues)
    print(max_value)