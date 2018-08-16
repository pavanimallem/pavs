size=int(input())
list1=[int(i) for i in raw_input().split()]
list1.sort()
print " ". join(map(str,list1))
