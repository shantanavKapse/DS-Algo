arr = [12, 34, 10, 6, 40]

def bubbleSort(a):
    n = len(a)
    
    for i in range(1, n):
        for j in range(0, n-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubbleSort(arr))