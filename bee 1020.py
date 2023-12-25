day = int(input())
a = day/365 #years
b= day%365
c= b/30  #months
d= b%30  #days
print((f"{int(a)} ano(s)"))
print((f"{int(c)} mes(es)"))
print((f"{int(d)} dia(s)"))