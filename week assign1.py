# for i in range(1,51):
#   if i%3==0 & i%5==0:
#    print("fizzbuzz")
#   elif i%3==0:
#    print("fizz")
#   elif i%5==0:
#    print("buzz")
#   else:
#    print(i)

# x=['abc','xyz','aba','1221']
# count=0
# for s in x:
#   if len(s)>=2 and s[0]==s[-1]:
#    count+=1
# print(count)

# a,b=list(map(int,input('enter two numbers').split()))
# print(a+b,a-b,a*b,a**b)
print("[a]dd","[l]ist","[s]earch","[v]iew","[d]elete","[e]xit")
name=input("movie name").lower()
year=input('movie release year').lower()
duration=input('movie run time in minutes').lower()
genres=input(("enter genres(comma separated):").split(",")).lower()
print('welcome')
l=[{ "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action","Adventure", "Drama"] },
{ "name": "Back to the Future", "year": 1985, "duration": 114,"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
choice=input('enter choice').lower()
l1=[]
l1=l.append({"name":name,"year":year,'duration':duration,'genres':genres})
if choice=="a":
 l1=l.append({"name":name,"year":year,'duration':duration,'genres':genres})
print(l1)
if choice=="l":
 for items in l:
    count=0
    count=+1
 print(l.items())
if choice=='s':
 if l1 in l:
  print('movie is there')