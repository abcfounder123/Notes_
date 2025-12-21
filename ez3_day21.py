
"""

1. Effect and result
2. Type of function
3. Pure function
4. Using strange function
5. Flag
6. Checking successful iteration (for + else)

################################################

Effect and result

################################################

difference_update
effect = remove
result = -

difference
effect = -
result = return the difference of two or more sets as a new set => set

pop
effect = remove
result = removed element

################################################

Type of function
1. (effect only) function        ( eg.difference_update )
2. (result only) function        ( eg.difference )
3. (effect and result) function  ( eg.pop )

################################################

Pure function
- no side effect

################################################

Using strange function

step.1 
- read documentation before use  (help, __doc__)
- determine effect and result.

step.2
- test doc

step.3
- test as you like

step.4
- rewrite by yourself

################################################

input
effect ---> None
result ---> return user input

lower
effect --->   None
result --->   Return a copy of the string converted to lowercase.

upper
effect --->   None
result --->   Return a copy of the string converted to uppercase.


len(obj, /)
    Return the number of items in a container.

################################################


def lower(s):
    ans = ''
    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ans += chr(ord(c) + 32)
        else:
            ans += c
    return ans
    
    
def lower(s):
    ans = ''
    for c in s:
        if ord(c) in list(range(65, 91)):
            ans += chr(ord(c) + 32)
        else:
            ans += c
    return ans
    

################################################


len(obj, /)
    Return the number of items in a container.


def mylen(obj, /):
    n = 0
    for _ in obj:
        n += 1
    return n


################################################################################################

Flag


def difference(s1, *args):
    ans = []
    flag = False
    for i in s1: # 2
        for s in args: # s2, s3, s4
            if i not in s:
                flag = True
            else:
                flag = False
                break
        if flag:
            ans.append(i)
    return set(ans)
    
    
################################################################################################

Checking successful iteration (for + else)


def difference(s1, *args):
    ans = []
    for i in s1: # 1 2 3 4
        for s in args: # s2  s3  s4  empty => False
            if i in s:
                break
        else:
            ans.append(i)

    return set(ans)
    

################################################


def difference(l, *args):
    ans = []
    for i in l: 
        for s in args: 
            if i in s:
                break
        else:
            ans.append(i)
    return ans


l1 = [1, 2, 3, 4, "apple", "banana"]
l2 = [2, 4, 5, 6]
l3 = [1, 7, 9]
l4 = (6, 8, 10, 4, "apple")

d = difference(l1, l2, l3, l4)

print(d)  

################################################################################################

"""
