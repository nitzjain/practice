'''
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or
 numbers. As a reminder, balanced parentheses require every opening parenthesis to be
 closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
#using sets and tuple packing
def balance_parm_check(str):

    if len(str)% 2 != 0:
        return False
    check_list = []
    open_parm = set('({[')
    parm_set = set(('{','}'),('[',']'),('(',')'))
    for p in str:
        if p in open_parm:
            check_list.append(p)
        else:
            if len(check_list) == 0:
                return False

            last_pop = check_list.pop()

            if (last_pop,p) not in parm_set:
                return False

    return len(check_list) == 0


'''

def balance_check(str):
    if len(str) % 2 != 0:
        return False
    check_list = []
    open_parm = set('({[')
    close_parm = set(')}]')
    for p in str:
        if p in open_parm:
            check_list.append(p)
        elif p in close_parm:
            if len(check_list) == 0:
                return False

            check_list.pop()

    return len(check_list) == 0

print(balance_check('{{{{}}}{}[]((()))}'))
