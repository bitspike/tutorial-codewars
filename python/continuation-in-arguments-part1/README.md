Link
=========================
[]()

Description
=========================
In continuation passing style programming, the functions, instead of returning a value, take an extra argument which is a continuation function, taking the value that would have been returned as its argument.

Even the basic operations must take an extra argument. For that end, we defined `add(x,y,k)` and `mult(x,y,k)` functions, which should be used in the solution.
Task
Rewrite the following two simple functions in continuation style:

```
def f(x):
    return x*2

def g(x):
    return 10*x+1
```

So that, the rewritten functions `f` and `g` take an extra parameter, `k`, and don't return any value, else the tests will fail.
Also, usage of `add` and `mult` will be checked.

Finally, use the prepared function `show(x,k)` in place of `print(x)` to produce the following code snippet translated into continuation passing style:

```
def main():
    print( f(g(2)) )
```

For testing, we introduced the `expect_value` method which can retrieve the final value to be returned, using the identity function `id` as the final continuation function.
Usage of `id` in this kata means the end of the continuation process. (See the example test cases.)
