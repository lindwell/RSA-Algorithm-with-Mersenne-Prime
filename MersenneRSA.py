import random

def IsPrime(p):
    for i in range(2,p):
        if p%i==0:
            return False
    else:
        return True

def PrimeBetween(a,b):
    primes=[]
    for i in range(a,b+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=1
        if c==0:
            primes.append(i)
    return primes

def MersennePrime(a,b):
    primes=PrimeBetween(a, b)
    MnPrimes=[]
    for prime in primes:
        mn=2**prime-1
        if IsPrime(mn)==True:
            MnPrimes.append(mn)
    return MnPrimes

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def ExtEA(a,b):
    r1,r2=a,b
    s1,s2=1,0
    t1,t2=0,1

    while(r2>0):
        q=r1//r2
        r=r1-q*r2
        r1,r2=r2,r

        s=s1-q*s2
        s1,s2=s2,s

        t=t1-q*t2
        t1,t2=t2,t
    return r1, s1, t1

    

def ModuloInverse(a,b):
    gcd,x,y = ExtEA(a, b)
    if x<0:
        x+=b
    return x

#work on this you bozo    
def GenEncKey(phi):
    keys=[]
    for e in range(1,phi):
        if IsPrime(e) == True:
            keys.append(e)
    for key in keys:
        if gcd(e,phi)!=1:
            keys.remove(e)
    return random.choice(keys)


def encrypt(e,n,msg):
    cipher=""
    for c in msg:
        m=ord(c)
        cipher+=str(pow(m,e,n))+" "
    return cipher

def decrypt(d,n,cipher):
    msg=""

    parts=cipher.split(" ")
    for part in parts:
        if part:
            c=int(part)
            msg+=chr(pow(c,d,n))
    return msg

def main():
    
    print("Developed by:")
    
    print(" _____  __   _____ _   _  _____  __   _   _ _____  _____ ")
    print("/  __ \/  | |____ | | | |/ __  \/  | | \ | |  _  ||____ |")
    print("| /  \/`| |     / / |_| |`' / /'`| | |  \| | | | |    / /")
    print("| |     | |     \ \  _  |  / /   | | | . ` | | | |    \ \ ")
    print("| \__/\_| |_.___/ / | | |./ /____| |_| |\  \ \_/ /.___/ /")
    print(" \____/\___/\____/\_| |_/\_____/\___/\_| \_/\___/ \____/ ")
                                                         
                                                         

    print("You will have to provide the minimum and maximum of exponent that will be used for generating a Mersenne Prime")
    a=int(input("Minimum:"))
    b=int(input("Maximum:"))
    mn=MersennePrime(a, b)
    p=random.choice(mn)
    mn.remove(p)
    q=random.choice(mn)
    
    n=p*q
    phi=(p-1)*(q-1)

    msg=input("Message:")

    e=GenEncKey(phi)
    d=ModuloInverse(e,phi)

    enc=encrypt(e,n,msg)
    dec=decrypt(d,n,enc)

    print(f"메시지:{msg}")
    print(f"e:{e}")
    print(f"d:{d}")
    print(f"n:{n}")
    print(f"enc:{enc}")
    print(f"dec:{dec}")

main()
