
"""

1. Parameters

1. standard/ normal parameter  
2. default parameter           
3. positional only parameter  
4. keword only parameter      
5. variable-length positional parameter 
6. variable-length keyword parameter  

################################################

2. Definition

def -> function definition
x   -> function name
()  -> parameter list

################################################

3. positional arguments Vs keyword arguments

def x(a, b, c):
    print(a, b, c)
    
x(1, 2, 3)
x(3, 2, 1)
x(a=1, b=2, c=3)
x(c=3, b=2, a=1)


Output

1 2 3
3 2 1
1 2 3
1 2 3

################################################

4. Simple is better than complex.

def add(a, b, /):
    pass

################################################

5. Complex is better than complicated.

def info(*, name, age, country, ph, id, height, weight, education):
    print()

################################################

*   ->  all values

a = ()
a = (1, 2)
a = (1, 2, 3, 4, 5)


def f(*a):
    print(a)


f()
f(1, 2)
f(1, 2, 3, 4, 5)

################################################

**   ->  all items(key and value)

a = {}
a = {'a': 1, 'b': 2}
a = {'a': 1, 'b': 2, 'c': 3, 'age': 20}

def info(**a):
    print(a)

info(name="Mg Mg", age=20)

################################################

6. Using strange function.1

help(print)


def print(*args, sep=' ', end='\n', file=None, flush=False):
    pass
    
parameter -> 5
- *args     ->   No.5
- sep       ->   No.2
- end       ->   No.2
- file      ->   No.2
- flush     ->   No.2 


print(1, 2, 3)
- args      ->   (1, 2, 3)
- sep       ->   ' '
- end       ->   '\n'  (select the next line)
- file      ->   None
- flush     ->   False 


print("Parameters", 1, 2, 3, "apple", sep="\n- ")

- args      ->   ("Parameters", 1, 2, 3, "apple")
- sep       ->   "\n- "
- end       ->   '\n'  
- file      ->   None
- flush     ->   False 

################################################

Using strange function.2

def input(prompt='', /):
    pass
    

parameter -> 1
- prompt     ->   No.2, No.3

################################################

Using strange function.3

tk.Button(x, foreground="Blue", borderwidth=20, height=10, width=20)

parameter list -> (self, master=None, cnf={}, **kw)
self     -> x
master   -> None, 
cnf      -> {}
kw       -> {
              'foreground': "Blue", 
              'borderwidth': 20, 
              'height': 10, 
              'width': 20
             ) 

################################################

7. Quick analysis 

(a, b, c, /, d, e, f, *, g, h, i, j)
 - a, b, c          (p only)
 - d, e, f          (standard)
 - g, h, i, j       (n only)

def f(a, b, c, /, d, e, f, *, g, h, i, j):
    print(a, b, c, d, e, f, g, h, i, j)


f(1, 2, 3, 4, 5, 6, g=7, h=8, i=9, j=10)
f(1, 2, 3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
f(1, 2, 3, 4, 5, f=6, g=7, h=8, i=9, j=10)
f(1, 2, 3, 4, e=5, f=6, g=7, h=8, i=9, j=10)

################################################

8. Exercises

Our parameters(6)

(n1, n2, n3, name, age, grade)

Our desire
- n1, n2, n3  ( p )
- name, age, grade ( n )
Answer --->  (n1, n2, n3, /, *, name, age, grade)

We want to add 3 parameters.
- a, b, c  (p, n, p+n)
Answer --->  (n1, n2, n3, /, a, b, c, *, name, age, grade)

################################################

9. Summary

1. (a, b, c)
2. (celsius=0)
3. ---/
4. *---
5. *args
6. **kw, **kwargs

################################################################################################



"""

