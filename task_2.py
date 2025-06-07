def binary_search_upper_rate(arr, target):
    low = 0
    high = len(arr) - 1 
    count = 0 
    upper_rate = None
  
    while low <= high:
        count += 1
        mid = (high + low) // 2
        if arr[mid] >= target:
            upper_rate = arr[mid]
            high = mid -1 
        else:
            low = mid + 1                  
        
    return (count, upper_rate)

print(binary_search_upper_rate([3.2, 5.7, 32.1], 4.7))

# "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

