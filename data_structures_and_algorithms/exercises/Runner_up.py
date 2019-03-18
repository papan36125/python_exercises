if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum=arr[0]
    max_2 = arr[0]
    for item in arr:
        if item>maximum:
            max_2 = maximum
            maximum = item
    # for item in arr:
        if maximum == max_2 and item<maximum:
            max_2 = item
            continue
        if item>max_2 and item<maximum:
            max_2 = item
    print(max_2)
