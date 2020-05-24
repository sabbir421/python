print("*****if you want even value then take f=1 and if you want odd number then f=0 *******")
i=int(input("starting value:"))
n=int(input("ending value"))
f=int(input("f"))
while i<=n:
    i=i+1
    if i %2==f:
        continue
    print(i)