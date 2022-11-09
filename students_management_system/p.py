import functools

t =tuple('100')
print(type(t))
t=functools.reduce(lambda sub,ele: sub*10+ele,t)
print(t)
i =50
s =t - i
print(type(t))
print(s)