
def dynamic_fib(n,lookup):
    if n<=2:
        lookup[n] =1
    if lookup[n] is None:
            lookup[n] = dynamic_fib(n-1,lookup) + dynamic_fib(n-2,lookup)
    return lookup
map_set=[None]*(6)
print map_set
print dynamic_fib(5,map_set)
