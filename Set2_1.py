day=20
y=int(day/360)
r1=day%360
m=int(r1/30)
r2=r1%30
w=int(r2/7)
d=r2%7
print("Year=",y)
print("Month=",m)
print("Week=",w)
print("Day=",d)