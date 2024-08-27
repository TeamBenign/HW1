def divide(x=1,y=1):
    return x/y 
def largest(lst):
    very_large = -11111111
    for num in lst:
        if num>very_large:
            very_large = num
    return very_large
print(divide(5,2))
print(largest(list(range(0,10))))