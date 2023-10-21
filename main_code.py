"""
Created on Sun Aug 13 13:38:14 2023

Author: PierreNedellec
"""
import random

def modexp(a,b,n): #computes a^b mod n
    (p,j,r) = (a,b,1)
    while j != 0:
        if j%2 == 0:
            p = (p**2)%n
            j = j//2
            r = r%n
        else:
            p = (p**2)%n
            j = (j-1)//2
            r = (r*p)%n
    return r
            
def give_rq(n):#returns r when n-1 written as 2^r * q
    q = n-1
    r = 0
    while q%2 == 0:
        q = divmod(q,2)[0]
        r+=1
    return (r,q)
    
def primality_test(p,a):
    r,b = give_rq(p)
    if modexp(a,b,p) == 1 or modexp(a,b,p) == p-1:
        return True
    for i in range(r):
        b *= 2
        if modexp(a,b,p) == p-1:
            return True
    return False
    
def give_bases(m):
    fbases = []
    a = 2
    if m<=23:
        for k in range(2,m):
            fbases.append(k)
        return fbases
    for l in range(9):
        while a in fbases:
            a = random.randint(2,m-1)       
        fbases.append(a)
    return fbases

def test(p):
    if p < 2:
        return False
    w = give_bases(p)
    for j in w:
        if not primality_test(p,j):
            return False
    return True

def testresult(w):
    if test(w):
        return 'This number is PRIME'
    else:
        return 'This number is not prime'
