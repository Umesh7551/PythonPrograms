# Program to evaluate Square root

x=float(input("Enter Value to cal Squareroot:"))
a=float(input("Enter First Exponent value:"))
b=float(input("Enter Second Exponent value:"))
#xn/xm=xn−m
res = (x**(a-b))**0.5
#res=((x**a)/(x**b))**0.5
print("Square root of {}**{}/{}**{}={}".format(x,a,x,b,res))