hr1,min1=map(int,raw_input().split())
hr2,min2=map(int,raw_input().split())
n1=hr1*60+min1
n2=hr2*60+min2
diff=abs(n1-n2)
time=diff%60
time1=(diff-time)//60
print time1,time
