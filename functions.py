#functions
#arguments
#1.position,2.keyword,3.default,4.variable length

##def great () :
##    print('good morning')
##    print('welcome to python class')
##great()




##def add(x,y) :#formal arguments
##    print('x',x)
##    print('y',y)
##    c=x+y
##    print(c)
##add(4,6)#actual arguments





##def human(name,age):
##    print (name)
##    print(age)
##human('sathwik',18)



##def add(x,*y):
##    c=x
##    for i in y:
##        c+=i
##    print(c)
##add(100.200,300,400,500,600)



##def add(x,y):
##    c=x+y
##    print(c)
##result=add(10,20)
##
##def sub():
##
##    a=result-10
##    print(a)
##sub()





###nearest prime:
##from math import sqrt
##def is_prime(n):
##    s=int(sqrt(n))
##    for i in range(2,s+1):
##        if n%i==0:
##            return False
##        return True
##    def right_prime(n):
##        i=n+1
##        while 1:
##            if is_prime(i):
##                return i
##            i+=1
##    def left_prime(n):
##        j=n-1
##        while 1:
##            if is_prime(j):
##                return j
##            j=j-1
##def near_prime(n):
##    if is_prime(n):
##        return n
##    else:
##        x=right_prime(n)
##        y=left_prime(n)
##        if abs(n-x)<abs(n-y):
##            print(x)
##        elif abs(n-x)>abs(n-y):
##                print(y)
##        else:
##                    print(x,y)
##n=10
##near_primr(n)



##def is_even(n):
##    if n%2==0:
##        print('even')
##    else:
##        print('odd')
##n=10
##is_even_odd(n)



##def pattern:
##    n=int(input('enter a number'))
##    for i in range(1,n+1):
##        print((n-i)*'',end=' ')
##        for j in range(1,i+1):
##            print('*',end=' ')
##            
##print()
##
##pattern()
##
##print('example')
##
##pattern()


##def add(a,b):     #formal parameters
##    c=a+b
##    print(c)
##
##a=int(input())
##b=int(input())
##
##add(a,b)          #actual parameters/arguments
##
##add(23,25)


##def add(a,b):     #formal parameters
##    c=a+b
##    return(c)           #return can help to use the code in another program
##
##a=int(input())
##b=int(input())
##
##print(add(a,b))          #actual parameters/arguments
##
##print(add(50,50))


##a=10                    #global variable
##print('start',a)
##def example():
##    b=11                #local variable
##    print('inside',b)
##
##
##example()
##print('end',a)



##a=10
##print('start',a)
##
##def example():
##    global b
##    b=11
##    print('inside',b)
##
##example()
##print('end',b)



##def add(a,b):
##    print(add(a,b))
##def sub(a,b):
##    print(sub(a,b))
##def mul(a,b):
##    print(mul(a,b))
##def div(a,b):
##    print(div(a,b))
    












































