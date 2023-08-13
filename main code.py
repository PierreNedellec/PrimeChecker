"""
Created on Sun Aug 13 13:38:14 2023

Author: Pierre Nedellec
"""
def dec2bin(num):
    b = bin(num)
    b = str(b[2:])
    return b

def modexp(a,b,n): #computes a^b mod n
    (p,j,r) = (a,b,1)
    while j != 0:
        if j%2 == 0:
            (p,j,r) = ((p**2)%n,(j/2),(r%n))
        if j%2 == 1:
            (p,j,r) = ((p**2)%n,(j-1)/2,(r*p)%n)
    return r
            
def give_r(n):#returns r when n-1 written as 2^r * q
    q = n-1
    r = 0
    while q%2 == 0:
        q /=2
        r+=1
    return r
    
def primality_test(p,a):
    r = give_r(p)
    q = (p-1)/2**r
    if modexp(a,q,p) == 1 or modexp(a,q,p) == p-1:
        return True
    for i in range(r):
        b = (2**i)*q
        if modexp(a,b,p) == p-1:
            return True
    return False

p = 1234567891
bases = [2,13,23,1662803]

if primality_test(p,bases[0]) and primality_test(p,bases[1]) and primality_test(p,bases[2]) and primality_test(p,bases[3]):
    print(f'{p} is prime')
else:
    print(f'{p} is not prime')


