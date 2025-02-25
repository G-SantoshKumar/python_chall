a=10
b=5

def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    return(x,y)

print(swap(a,b))