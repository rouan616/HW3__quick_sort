def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_index = start
    pivot_value = array[pivot_index]
    left = start
    right = end

    print(f"\n此輪排序的子陣列為：{array[start:end+1]}，基準點為 {pivot_value}")

    while left != right:
        while left < right and array[right] >= pivot_value:
            right -= 1
        while left < right and array[left] <= pivot_value:
            left += 1
        if left < right:
            array[left], array[right] = array[right], array[left]
            print(f"交換元素：array[{left}] 和 array[{right}] → {array}")

    array[pivot_index], array[left] = array[left], array[pivot_index]
    print(f"交換基準點和指標：array[{pivot_index}] 和 array[{left}] → {array}")
    print(f"完成此輪：{array[start:end+1]}（pivot={array[left]} 定位）")

    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)

data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("原始陣列：", data)
quick_sort(data, 0, len(data) - 1)
print("\n排序後結果：", data)