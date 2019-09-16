#Extra Credit Homework Assignment, Merge Sort
#VARGAS, BRANDON
#April 24, 2017

#Iterative:
def merge_sort_iterative(l, m):
    result = []
    i = j = 0
    total = len(l) + len(m)
    while len(result) != total:
        if len(l) == i:
            result = result + m[j:]
            break
        elif len(m) == j:
            result = result + l[i:]
            break
        elif l[i] < m[j]:
            result.append(l[i])
            i = i + 1
        else:
            result.append(m[j])
            j = j + 1
    return result

#Recursive:



# call this function first to Merge two arrays and get Merged Array
def merge(array1,array2):
    merged_array=[]
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array

#Then call this function with the merged_array to sort the list
def mergeSort(merged_array):
    n  = len(merged_array)
    if n <= 1:
        return merged_array
    left = merged_array[:n/2]
    right = merged_array[n/2:]
    return merge(mergeSort(left),mergeSort(right))


