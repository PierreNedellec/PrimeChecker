"""
Created on Sun Aug 13 13:38:14 2023

Author: Pierre Nedellec
"""
import random
import time
start_time = time.time()
def modexp(a,b,n): #computes a^b mod n
    (p,j,r) = (a,b,1)
    while j != 0:
        if j%2 == 0:
            (p,j,r) = ((p**2)%n,(divmod(j,2)[0]),(r%n))
        if j%2 == 1:
            (p,j,r) = ((p**2)%n,(divmod(j-1,2)[0]),(r*p)%n)
    return r
            
def give_rq(n):#returns r when n-1 written as 2^r * q
    q = n-1
    r = 0
    while int(str(q)[-1])%2 == 0:
        q = divmod(q,2)[0]
        r+=1
    return (r,q)
    
def primality_test(p,a):
    r = give_rq(p)[0]
    b = give_rq(p)[1]
    if modexp(a,b,p) == 1 or modexp(a,b,p) == p-1:
        return True
    for i in range(r):
        b *= 2
        if modexp(a,b,p) == p-1 or modexp(a,b,p) == 1:
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
    
p = '''25600128006400320016008004002001'''
p = int(''.join(p.split()))
bases = give_bases(p)
prime = True
        
for j in bases:
    if not primality_test(p,j):
        print(f'{p} is not prime')
        prime = False
        break
if prime:
    print(f'{p} is prime')
print("--- %s seconds ---" % (time.time() - start_time))