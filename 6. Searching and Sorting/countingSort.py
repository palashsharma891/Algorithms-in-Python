def countingSort(array):
    size = len(array)
    output = [0] * size
    
    count = [0] * 10
    
    for i in range(size):
        count[array[i]] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        
    for i in range(size):
        array[i] = output[i]
        
data = [8, 7, 2, 1, 0, 9, 6]
countingSort(data)
print('Sorted Array is:')
print(data)
