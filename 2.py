# 三角形判断

a=float(input("请输入第一条边的长度："))
b=float(input("请输入第二条边的长度："))
c=float(input("请输入第三条边的长度："))   
if a+b<=c or a+c<=b or b+c<=a:
    print("不能构成三角形")
elif a==b==c:
    print("是等边三角形")
elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
    if a==b or b==c or c==a:
        print("是等腰直角三角形")
    else:
        print("是直角三角形")
elif a**2+b**2>c**2 or b**2+c**2>a**2 or a**2+c**2>b**2:
    if a==b or b==c or c==a:
        print("是等腰锐角三角形")
    else:
        print("是锐角三角形")
elif a**2+b**2<c**2 or b**2+c**2<a**2 or a**2+c**2<b**2:
    if a==b or b==c or c==a:
        print("是等腰钝角三角形")
    else:
        print("是钝角三角形")