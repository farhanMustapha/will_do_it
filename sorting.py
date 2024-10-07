arr=[50, 3, 600, 200, 10]
def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
           smallest = arr[i]
           smallest_index = i
    return smallest_index

print(findSmallest)


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        a=arr.pop(smallest) # supprimer 
        newArr.append(a)   # ajouter
    return newArr

print(selectionSort(arr))

