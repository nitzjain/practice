'''

print(3+3)


a = "aaaa"
print(f"sssssdss{a}")

a = 'asasa'
print("hi%s%s%s"%(a,a,a))

my_list = [1,2,3]
print(my_list+my_list)
my_list.append(7)
print(my_list+my_list)
my_list.pop(1)
print(my_list+my_list)
my_list.sort()
print(my_list)



st = 'Print only the words that start with S in this sentence'
a = st.split()
for i in a:
    if (i[0]=='s') or (i[0] =='S'):
        print(i)


def sum(a,b=5):
    return a+b

x = sum(2)
print(x)




#sub string and replace
def check_v(char1):
    if char1[0].lower() in 'aeiou' :
        return char1+'ay'
    else:
        return char1[1:]+char1[0]+'ay'

x = check_v('adapple')
print (x)

#exception handling example:
import string as str
def try_exception_using_sqrt(x):
    try:
        if x < 0:
            raise IOError
        elif x in str.digits:
            return x ** (0.5)
    except ValueError as v:
        print('IO error:\n',v)
    finally:
        print(' in the end, it doesn;t even matter\n')

print(try_exception_using_sqrt(-100))

#fibonnaci series without generators:
def fib(a):
    x =1
    y =1
    list1 = []
    for z in range(a):
            list1.append(x)
            x = y
            y = x + y
    return list1

print(fib(13))

#fibonnaci series with generators

def fib(a):
    x =1
    y =1
    for z in range(a):
            yield x
            k = x + y
            x = y
            y = k

for x in fib(13):
    print(x)
OR(using tuple uncoupling):

def fib(a):
    x =1
    y =1
    for z in range(a):
            yield x
            x,y = y,x+y

for x in fib(13):
    print(x)


#using generators for 5 random numbers:
from random import randint

def test1(low,high,x):
    for z in range(x):
        yield randint(low,high)

for d in test1(1,100,5):
    print(d)

#generator example:
def gen(a):
    for x in range(a):
        yield x
g = gen(5)
print(next(g))
print(next(g))
print(next(g))
#to print the whole list use the below list function
print(list(gen(5)))

#convert list to string by concatenating each char
def myfunc(str):
    a = ''
    for i in str:
        x = i
        print(x)
        if str.index(i) % 2 == 0:
            print(str.index(i))
            a += x.upper()
        else:
            print(str.index(i))
            a += x.lower()
    return (a)

print(myfunc("abcdnhjddn"))



#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def mufunc(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        elif b < a:
            return b
        else:
            print('dont be smart with me even')
    else:
        if a < b:
            return b
        elif b < a:
            return a
        else:
            print('dont be smart with me odd')

a = mufunc(5,5)
print (a)


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def myfunc(str):
    return str[0].upper()+str[1:3]+str[3].upper()+str[4:]

print(myfunc("macdonald"))


#reverse a sentence
def master_yoda(str):
    x = str.split()
    z = ''
    y = len(x)
    for i in x:
        z += x[y-1] + ' '
        y = y -1
    return z



print(master_yoda('I am home'))


:or

a = 'I am home'
b = a.split()
c = b[::-1]
b.reverse()
#list to str
d = ' '.join(b)
print(c)
print(d)



#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(a):
    if (100 - a <= 10 and 100-a >= 0) or  a - 100 <= 10 or 200 - a <= 10 or  (a - 200 <= 10 and a- 200 >=0) :
        return True
    else:
        return False

print(almost_there(190))



#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def myfunc(a):
    z = 0
    for x in a:
        if z == 1 and x == 3:
            return True
        elif x == 3:
            z = 1
        else:
            z =0
    return False

print(myfunc([1,3,3]))


#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(str):
    z = ''
    for x in str:
        z += x * 3
    return z

print(paper_doll("HELLO"))



#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer(a):
    z =0
    su = 0
    for i in a:
        if i == 6:
            z =1
        elif z == 1 and i == 9:
            z = 0
        elif z == 1:
            continue
        else:
            su += i
    return su


print(summer([1,2,3,6,4,9,5]))



#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def prime_check(a):
    prim = [2]
    if a <=2:
        return 1
    for i in range(3,a+1):
        for j in prim:
            if i % j == 0:
                i +=2
                break
        else:
                prim.append(i)
                i +=2
    print(prim)
    su = len(prim)
    return su

print(prime_check(100))



#map function
def sum1(a,b):
    return a + b

a1 = [1,2,3]
b1 = [1,2,3]

print(list(map(sum1,a1,b1)))

#use of pi : 3.14
import math
def vol(radius):
    return (4/3) * math.pi * (radius ** 3)

print(vol(2))


#
def rang(a,b,c):
    return a in range(b,c+1)

print(rang(41,1,10))


#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
import string

def check_up_low(str):
    low = 0
    up = 0
    for x in str:
        if x in string.ascii_lowercase:
            low +=1
        elif x in string.ascii_uppercase:
            up +=1
    print('low {} \n high {}'.format(low,up))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
check_up_low(s)



#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def uniq(a):
    b = []
    if len(a) == 0:
        return False
    elif len(a) == 1:
        return a
    else:
        c = a[0]
        b.append(c)
        for x in range(2,len(a)):
            if a[x] == c:
                continue
            else:
                c = a[x]
                b.append(c)
    return b

print(uniq([1,1,1,1,2,2,3,3,3,3,4,5]))

 #another way to find unique lists:
def uniq(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

print(uniq([1,1,1,1,2,2,3,3,3,3,4,5]))

#dictionary example:
dict = {k:v for k,v in ('a1','b2')}
print(len(dict))
print(dict)
dict['a1'] = 1
dict['b2'] = 2
print(dict)

#palindrome:

str = ['aba','ccd']

print(list(map(lambda a: a[::] == a[::-1],str)))
print(list(filter(lambda a: a[::] == a[::-1],str)))

Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

import string

def check_pangram(str):
    alphabet = string.ascii_lowercase
    z = list(alphabet)
    for x in str.lower():
        if x in z:
            z.remove(x)
    if len(z) == 0:
        return True
    else:
        return False

print(check_pangram("The quick brown fo jumps over the lazy dog"))



#another way. to find unique, always convert to set.
import string
def chk_panagram(str, alpha = string.ascii_lowercase):
    x = set(alpha)
    print(x)
    print(set(str.lower()))
    return x <= set(str.lower())
print(chk_panagram("The quick brown fox jumps over the lazy dog"))



#tic tak toe problem
#print board, take user input, match and declare winner.

import string
def user_inp():
    a = ''
    p1 = p2 = ''
    while a != 'x' and a != 'o':
        a = input('player one enter your choice x or o: ')

    if a == 'x':
        p1 = 'x'
        p2 = 'o'
    else:
        p1 = 'o'
        p2 = 'x'
    return(p1,p2)

def print_board(a = [' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    print('{}|{}|{}'.format(a[6],a[7],a[8]))
    print('-|-|-')
    print('{}|{}|{}'.format(a[3],a[4],a[5]))
    print('-|-|-')
    print('{}|{}|{}'.format(a[0],a[1],a[2]))

def user_inp_rep():
    p = ''
    if p in string.digits:
        p = input('Enter valid input player : ')
        return int(p)
    else:
        user_inp_rep()


def check_win(player,p):
    if (player[0] == player[1] == player[2] == p) or (player[3] == player[4] == player[5] == p)  or (player[6] == player[7] == player[8] == p) or (player[0] == player[3] == player[6] == p) or (player[1] == player[4] == player[7] == p)  or (player[2] == player[5] == player[8] == p) or (player[0] == player[4] == player[8] == p) or (player[2] == player[4] == player[6] == p):
        return p

def main_call():
    p1 = p2   = counter = p = ''
    x = 0
    player = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    (p1,p2) = user_inp()
    print('Player 1 is: {} and Player 2 is: {}'.format(p1,p2))
    print_board()
    print ("\n" * 10)
    print('lets begin the game: \n')
    if p1 == 'x':
       counter = 0
    else:
        counter = 1
    while 1:
        if counter == 0:
            x = user_inp_rep()
            print(x)
            player[x-1]='x'
            print(player)
            print_board(player)
            if p1 == check_win(player,p1):
                print('Player 1 won')
                break
            else:
                counter = 1
        elif counter == 1:
            x = user_inp_rep()
            print(x)
            player[x-1]='o'
            print(player)
            print_board(player)
            if p2 == check_win(player, p2):
                print('Player 2 won')
                break
            else:
                counter = 0
    return True

main_call()





#all operator: if everything is True, then all() returns true.
arr = [1,0,1,0]
a = all(arr)
print(a)
s = sum(arr)
print(s)
if a or s:
    print(a or s)

#add elements to value(which is a list) in a dictionary
a = {1:[1,2,3]}
b=a.copy()
print(a)
print(b)
a[1].append(4)
print(a)
print(b)

#SORT EXAMPLE using a KEY
a = ["apples",'banana','orange',"tomato",'melons']
a.sort(key=lambda x:x[-5])
print(a)


#class example
#can use tuple unpacking such as x1,y1 = cor1
from math import sqrt as s
class Line:
    def __init__(self,cor1,cor2):
        self.cor1 = cor1
        self.cor2 = cor2

    def distance(self):
       return s(((self.cor2[1] - self.cor1[1]) ** 2) + ((self.cor2[0] - self.cor1[0]) ** 2))

    def slope(self):
       return  ((self.cor2[1] - self.cor1[1]))/((self.cor2[0] - self.cor1[0]))



coor1 = (3,2)
coor2 = (8,10)
myline = Line(coor1,coor2)
print(myline.distance())
print(myline.slope())


#class example #2
class Account:
    def __init__(self,owner='Nitesh',balance=100):
        self.owner = owner
        self.balance = balance

    def deposit(self,bal):
        self.balance += bal
        print("Deposit done")

    def withdraw(self,bal):
        self.balance -= bal
        if self.balance <0:
            print ('cannot withdraw more money than deposit balance')
            self.balance += bal
        else:
            print('Withdrawal done')

    def __str__(self):
        return (f'{self.owner} has a balance of {self.balance}\n')


myaccnt = Account()
print(myaccnt)
myaccnt.deposit(100)
myaccnt.withdraw(150)

myaccnt.withdraw(150)
print(myaccnt)




#exception handling
try:
    for i in ['a','b','c']:
        print (i ** 2)
except TypeError:
    print("not a correct input")


try:
    x = 5
    y = 0

    print(x/y)
except:
    print("Divide by zero error")
finally:
    print('finally')

while 1:
    try:
        a = int(input('enter number to be squared'))
        print( a ** 2)
    except:
        print('please enter integer\n')
        continue
    else:
        print('out of else')
        break



#super example:

class A():
    def __init__(self,val = 1):
        self.a = val

class B(A):
    def __init__(self,val):
        super().__init__(val)

ab = B(8)
print(ab.a)


#special function __str__ example
self.a <> a

a,b=0,0
class myClass():
    a,b =1,1
    print(a,b)
    def __init__(self):
        self.a = 2
        self.b = 2
        print(self.a,self.b)
    def __str__(self):
        print(a,b)
        return str(a+b)
m = myClass()
print(m)

#class is called first, then the function
output: cfim

def f(): print('f')

class C:
    print('c')
    def __init__(self): print('i')
    def m(self): print('m')

f()
C().m()

#eval function
def f(r):
    j = range(r)
    print(j)
    e = eval("*".join([str(i+2) for i in j]))
    return e
print(f(3))

#bitwise and operation
l = []
for i in range(17):
    l.append(i*3)
m = [x&1 for x in l]
print(m)


#NULL list special
L = [[]]*3
print(L)
L[0] +=  [[]]
print(L)

#open and write to a file
f = open('1.txt','w+')
f.write("helloo its me")
f.close()

#working with files and directories
import os
import shutil
print(os.listdir())
print(os.getcwd())
shutil.move()
os.unlink()
os.rmdir()
shutil.rmtree()
os.walk()

#datetime module
from datetime import datetime
x = datetime(2222,1,1)
print(x)
x = datetime.today()
y = x.date()
print(y)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

#regular expression example:
#remove numbers from a pattern and get the whole word. + gets the whole words. [] excludes from the pattern.
import re
test = 'the number 34 has 5 numbers inside 3 sentence'
x = re.findall(r'[^\d]+',test)
print(x)

#remove the space and spl characters and join the sentence back
import re
test = 'the number 34! has 5 numbers>? inside 3 sentence.'
x = re.findall(r'[^!?>. ]+',test)
print(' '.join(x))


#time a function
import timeit
stmt =  3 paranthetis
func(100)
3 closing paranthetis
setup = 3 paranthetis
def func(n):
    return list(map(str,range(n)))
3 closing paranthetis
setup1= 3 paranthetis
def func(n):
    return [str(x) for x in range(n)]
3 closing paranthetis
print(timeit.timeit(stmt,setup1,number= 1000))



#unzip a file. read the instructions. find the phone number from all folders/files
import zipfile
import os
import re
x = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
x.extractall("test")
y = os.listdir()
print(y)

z = os.getcwd() + '/' + 'extracted_content'
list1 = (os.listdir(z))
print(list1)
list2 = []
for i in list1:
    if not re.search(r'[.txt]+', i):
        list2.append(i)
print(list2)

for i in list2:
    path = z + '/' + i
    list3 = os.listdir(path)
    for j in list3:
        filepath = path + '/' + j
        f = open(filepath,'r')
        pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
        c = f.readline()
        #print(c)
        b = re.search(pattern, str(c))
        if(b):
            print(filepath)
            print(b.group( ))


#hex/binary representation of a number and some other small questions
print(hex(1024))
print(bin(1024))

print(round(5.232222,2))

s = 'hello how are you mary, are you feeling okay?'
print(s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1.union(set2))
print({k:k**3 for k in range(5)})

'''


