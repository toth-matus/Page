def Prime_Factorization(x):
    z=x
    primes=[]
    exponents=[]
    i=2
    while z>1:
        print(i)
        while z%i==0:
            if i in primes:
                exponents[primes.index(i)]+=1
            else: 
                primes.append(i)
                exponents.append(1)
            z=z//i
        z,i=check(primes, exponents,z,i)
    return(primes, exponents)

def check(primes, exponents,z,i):
    x=i
    prime=True
    while x**2 <=z:       
        if z%x==0:
            prime=False
            return(z,x)
        x+=1
    if prime==True and z>1:
        primes.append(z)
        exponents.append(1)
        return(1,z)
    else:
        return(z,i)

x=int(input())
primes, exponents = Prime_Factorization(x)

print(primes)
print(exponents)
