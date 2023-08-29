cube = lambda x: x*x*x 

def fibonacci(n):
    a=0
    b=1
    l=[a,b]
    if n==0:
        return []
    if n==1:
        return [0]
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        l.append(c)
    return l 

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))