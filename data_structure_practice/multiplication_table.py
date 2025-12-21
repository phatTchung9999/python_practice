def multiplication_table(arr):
    index = 0
    my_list = []
    while index < len(arr):
        row = []
        for n in arr:
            n *= arr[index]
            row.append(n)
        index += 1
        my_list.append(row)

    return my_list


def main():
    my_list = multiplication_table([2,3,7,8,10])
    for n in my_list:
        print(n)


if __name__ == '__main__':
    main()