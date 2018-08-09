lower=int(input("enter the range:"))
higher=int(input("enter the range:"))
print("prime numbers between",x,"and",y,"are")
for n in range(lower,higher+1):
     if n>1:
         for i in range(2,n):
	if(i%n)==0:
                break
       else:
	  print("n")
