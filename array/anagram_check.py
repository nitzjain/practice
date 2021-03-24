'''
use the sorting method


def anafram_check(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return sorted(s1) == sorted(s2)

print(anafram_check('sss ','sss'))
'''

def anagram(s1,s2):

    if len(s1) != len(s2):
        return False

    a = list(s1)
    #print(a)
    for j in range(len(s2)):
        if s2[j] in a:
          #  print(s2[j])
            a.remove(s2[j])
   # print(a)
    if len(a) == 0:
        return True
    else:
        return False

print(anagram('ab','a'))
print(anagram('god','ogd'))
print(anagram('god is great','ogd retagsi '))







