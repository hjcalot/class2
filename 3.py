# 逢猜必输

times=0
rt=["石头","剪刀","布"]
while times<2:
    usr=input()
    times+=1
    for i,j in enumerate(rt):
        if usr==j:
            print(f"bot出{rt[i-1]}，你输了")