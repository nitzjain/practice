'''
compress a string to display the count of characters.
Input: AAABBBBCCCCaaabbb
output: A3B4C4a3b3
'''

import collections

def compress_str(str1):
    a = collections.defaultdict(int)
    for i in str1:
        a[i] +=1
        #print(a[i])
    output = ''
    for j in a.keys():
        output = output + j + str(a.get(j))

    return output

#print(compress_str('AAAAABBBBCCCCaaabbb'))
print(compress_str('122333444455555'))
