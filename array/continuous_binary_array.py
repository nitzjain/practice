# def cont_bin(a):
#     cnt = 0
#     max_j = 0
#     j=0
#     for i in a:
#         j +=1
#         if i == 0:
#             cnt -=1
#         elif i == 1:
#             cnt += 1
#         if cnt == 0:
#             max_j = max(j,max_j)
#     return max_j
#

#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1
#for a binary array, find the max subset that is a pair
def findMaxLength(nums):
    balance = 0
    balance_to_first_index = {0: -1}
    output = 0

    for i in range(len(nums)):
        print(i)
        balance += 1 if nums[i] else -1
        print(balance)
        index = balance_to_first_index.get(balance, i)
        print(index)
        output = max(output, i - index)
        print(output)
        balance_to_first_index.setdefault(balance, i)
        print(balance_to_first_index)

print(findMaxLength([0,0,1,0,0,0,1,1]))