'''
#Given an integer array, output all the unique pairs that sum up to a specific value k
#input_sum([1,2,3,2],4)
#output : (2,2) and (1,3)

def input_sum(arr,k):
    a = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == k:
                b = (arr[i],arr[j])
                a.append(b)

    return a

print(input_sum([1,2,3,2],4))

or using sets
'''

def input_sum(arr,k):
    #if length of array < 2, then return False.
    if len(arr) < 2:
        return
    #define 2 sets for tracking
    seen = set()
    output = set()
    #for each number in the array, target = k - that number.
    #once we have that number, we can scan if that target number in the remaining arr.
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((num,target))
    return output

print(input_sum([1,3,2,2,0,1,4,4],4))