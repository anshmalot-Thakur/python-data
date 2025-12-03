#type conversions
#int to float
#float to int
#int to str
 # a=11
 # print(float(a)
# a=11.8
# print(int (a))

# i='243' 
# print(int(i))

# j=77
# print(str(j))
# j=str(j)


# marks=int(input("enter the marks"))
# if(marks>90 & marks<100):
#     print("grade A")
# elif(marks<90&marks>80):
#    print("grade B")
# elif(marks<80&marks>70):
#    print("grade c")
# elif(marks<70&marks>60):
#    print("grade d")
# elif(marks>100):
#    print("not valid")
# else:
#    print("you are fail")
 
# naam=("ansh")
# (len(naam))
# for i in range(0,len(naam)):
#     print(i,naam)

# a,b=(input("enter two strings").split()+["", ""][:2])
# print("equal" if a==b else "not equal")
# print("same address" if a is b else"different address")

a,b=map(int,input("enter range of numbers for sum").split())
sum=0
for i in range(min(a,b),max(a,b)+1):
  sum+=i
  print(sum)