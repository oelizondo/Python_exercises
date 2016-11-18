'''
    In an array, like [3,1,2]
    The first swoop will grab the 3, and
    compare it to all the other elements.
    Since it's the biggest, it will be
    placed at the end.

'''
def bubblesort(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    print array


bubblesort([3,1,2,5,7,1,3,8,500,1,4,2,9,1,6,3,7,8])
