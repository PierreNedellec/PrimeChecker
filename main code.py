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
    
