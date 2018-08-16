h1,m1=map(int,raw_input().split())
h2,m2=map(int,raw_input().split())
x1=h1*60+m1
x2=h2*60+m2
diff=abs(x1-x2)
time=diff%60
time1=(diff-time)//60
print time1,time
