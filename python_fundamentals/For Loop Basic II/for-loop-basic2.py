# 1 
def biggie(arr):
    for count in range(len(arr)):
        if arr[count] >0:
            arr[count] = 'Big'
    return arr
print(biggie([-1,3,5,-5]))

# 2 
def positive(arr):
    total = 0
    for count in range(len(arr)):
        if arr[count] > 0:
            total += 1
    arr[len(arr)-1] = total
    return arr

# 3
def sumtotal(arr):
    sum = 0
    for count in range(len(arr)):
        sum += arr[count]
    return sum
print(sumtotal([1,2,3,4]))

# 4
def average(arr):
    avg = 0
    for count in range(len(arr)):
        avg += arr[count]
    return avg/len(arr)
print(average([1,2,3,4]))

# 5 
def length(arr):
    return len(arr)

# 6 
def min(arr):
    minimum = arr[0]
    if len(arr) < 1:
        return false
    for count in range(len(arr)):
        if arr[count] < minimum:
            minimum = arr[count]
    return minimum
print(min([3,2,1,4]))

# 7
def max(arr):
    maximum = arr[0]
    if len(arr) < 1:
        return false
    for count in range(len(arr)):
        if arr[count] > maximum:
            maximum = arr[count]
    return maximum
print(max([3,2,1,4]))

# 8 
def ult(arr):
    dict = {'sumtotal':0, 'average':0, 'max':arr[0], 'min':arr[0], 'length':len(arr)}
    for count in range(len(arr)):
        dict['sumtotal'] += arr[count]
        if arr[count] > dict['max']:
            dict['max'] = arr[count]
        if arr[count] < dict['min']:
            dict['min'] = arr[count]
    dict['average'] = dict['sumtotal']/len(arr)
    return dict
print(ult([82, 1, -4, 7,12]))

# 9
def reverse(arr):
    for count in range(round(len(arr)/2)):
        x = arr[count]
        arr[count] = arr[len(arr)-1-count]
        arr[len(arr)-1-count] = x
    return arr
print(reverse([1,2,3,4,5]))


