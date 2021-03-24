#nums = [1,2,3,4,5,6,7], k = 3
#rotate the array k times
#output: [5,6,7,1,2,3,4]

def rotate_array(nums,k):
    if k == 0:
        return nums
    out_nums=[]
#    print(range(len(nums)))
    for i in  range(len(nums)):

        out_nums.append(nums[i - k])
        #print(out_nums[i])
    return out_nums

print(rotate_array([1,2,3,4,5,6,7],3))
#rotate_array([1,2,3,4,5,6,7],3)

