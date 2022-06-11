# a b c
#
# 0 1 1 2 3 5 8 13 21 34 55
# Fibonacci Series
n =int(input(" Enter the limit for Fibonacci series "))
a=0
b=1
print(a, " ", b,end=" ")
ctr=3
while ctr<=n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    ctr=ctr+1
