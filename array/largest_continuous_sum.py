#Given an array of +ve and -ve integers, find the largest continuous sum.
#large_sum([1,2,-1,3,5,10,10,-10,-1])
#output: 30
#2 arrays, one is current sum and other is max sum. add 2 elements and take max out of it.then take max of current sum and max sum array

def large_sum(arr1):
    if len(arr1) == 0:
        return 0

    #define 2 arrays, assign 1st element as sum
    max_sum = current_sum = arr1[0]
    #start the array from 2nd element
    for num in arr1[1:]:

        current_sum = max(current_sum+ num,num)
        max_sum = max(current_sum,max_sum)

    return max_sum

print(large_sum([1,2,-1,3,5,10,-10,-10,-1]))