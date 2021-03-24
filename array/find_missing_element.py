'''
#find the missing element in the 1st array that is missing in the 2nd array
#solution with NlogN complexity is to sort both the arrays and check each element at same index in both the arrays.
#stop when both the values dont match and return the value from the 1st array
#possible 5 solutions
def find_element(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return arr1[i]

print(find_element([1,2,3,4,5,6,7],[7,6,4,3,2,1]))

or use the zip/sort method


def finder(arr1,arr2):
    #need to sort
    arr1.sort()
    arr2.sort()
    for n1,n2 in zip(arr1,arr2):
        if n1!=n2:
            return n1
print(finder([1,2,3,4,5,6,7],[7,6,4,3,2,1]))

or use a hashtable and default dictionary. add each element to a hash table with a count.
then remove the keys using the 2nd array. If the count for a key == 0, thats your answer

Clever trick: sum(arr1) - sum(arr2). Thats the missing element in arr1.
issues can be with long arrays or decimal array. May run into outofbounds issue.


import collections

def finder(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] +=1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1

print(finder([1,2,3,4,5,6,7],[1,2,3,5,6,7]))
print(finder([5,5,7,7],[5,7,7]))

Using XOR method
'''
def finder(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result^=num
        print(result)

    return result
print(finder([1,2,3,4,5,6,7],[1,2,3,5,6,7]))
#print(finder([5,5,7,7],[5,7,7]))
