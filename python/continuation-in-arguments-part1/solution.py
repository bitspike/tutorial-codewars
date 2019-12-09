# functions should not return any values
# (: Happy coding! :)

def mult(a,b,k):
    k(a*b)

def add(a,b,k):
    k(a+b)

def show(a,k):
    k(a)

def f(x, k):
    mult(x,2,k)

def g(x,k):
    mult(10,x, lambda m: add(m,1,k))

def main(k):
    s = lambda m: show(m, k)
    g(2,lambda m: f(m, s))