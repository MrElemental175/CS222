def FahToCel(Fahrenheit):
    celcius = (Fahrenheit - 32) * 5.0 / 9.0
    return celcius

def sum(a, b):
    return a + b
#print(FahToCel(50))
#print(sum(2,3))


def foo(z, x = 10, y = 5):
    return x + y + z

#print(foo(3, 7 ))

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))