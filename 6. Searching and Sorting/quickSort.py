def partition(array, p, r):
    
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    
    (array[i+1], array[r]) = (array[r], array[i+1])
    
    return i + 1

def quickSort(array, p, r):
    
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)
        
data = [8, 7, 2, 1, 0, 9, 6]
quickSort(data, 0, len(data)-1)
print('Sorted Array is:')
print(data)
