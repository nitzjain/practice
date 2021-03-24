'''
#given a string, reverse it
#input: This is the best
#output: best the is this

def reversal(str1):
    str2 = str1.split()
    str3 = ' '.join(str2[::-1])
    return str3

print(reversal("this is the best"))
#or use the manual method
this is the brute force way. based on spaces, split the sentence into array words. Once done, join the list backwards.
" ".join(reversed(word_list))

'''

