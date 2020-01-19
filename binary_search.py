# O(log(n)) because half of the search space is eliminated on each iteration
# Array must be sorted


def binarySearch(array, target):
    return _binarySearch(array, target, 0, len(array) - 1)


def _binarySearch(array, target, lower, upper):
    _range = upper - lower
    if(_range < 0):
        raise Exception('Limits reversed')
    elif(_range == 0 & array[lower] != target):
        raise Exception("Element not in array")
    if(array[lower] > array[upper]):
        raise Exception("Array not sorted")
    center = int(_range/2) + lower
    if(target == array[center]):
        return center
    elif(target < array[center]):
        return _binarySearch(array, target, lower, center-1)
    else:
        return _binarySearch(array, target, center + 1, upper)


print(binarySearch([2, 3, 4, 7, 34, 56, 67, 88, 99, 3094, 344543], 67))

# Iterative version is more optimal


def iterBinarySearch(array, target):
    lower = 0
    upper = len(array)-1
    if(lower > upper):
        raise Exception("Limits reverse")
    while(True):
        _range = upper-lower
        if(_range == 0 & array[lower] != target):
            raise Exception("Element is not in array")
        if(array[lower] > array[upper]):
            raise Exception("Array not sorted")
        center = int(_range/2) + lower
        if(target == array[center]):
            return center
        elif (target < array[center]):
            upper = center - 1
        else:
            lower = center + 1


print(iterBinarySearch([2, 3, 4, 7, 34, 56, 67, 88, 99, 3094, 344543], 67))
