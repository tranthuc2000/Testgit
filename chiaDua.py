n=int(input())
def Check(n):
    i=2
    while(i<=n/2):
        if((n-i)%2==0):
            return True
            i+=2
    return False

if(n%2==0 and Check(n)==True):
    print("YES")
else:
    print("NO")
