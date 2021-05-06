#defining my fibonacci function
def fibo(z):
    if z <= 1:
        return z
    else:
        return(fibo(z-1) + fibo(z-2))

#using loops

for z in range(20):
    print(str(fibo(z)), end=" ")
