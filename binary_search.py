def binary_search(list, target):
    first = 0
    last = len(list) -1
 
    while first <= last:
        midpoint = (first + last) //2
        if list[midpoint] == target:
            return midpoint
        elif target < list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None

def verify(result):
    if result is not None:
        print("Target found at index:",result)
    else:
        print("Target not found in list")

numbers = [x for x in range(1, 11)]

result = binary_search(numbers, 10)
verify(result)