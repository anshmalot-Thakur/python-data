quiz=[]
def input_value(prompt):
 while True:
   o= input(prompt).strip()
   if o:
      return o
   print("it can't be empty")
 
def input_data(prompt):
  while True:
       try:
               p=int(input(prompt))
       except:
        ("enter a valid option in number")
while True:

 print("choose a option\n")
 print("welcome to quiz") 
 print("[a], to add quiz")
 print("[u], to update quiz")
 print("[p], play quiz")
 print("[d], to delete quiz")
 print("[q], to quit quiz")

 choose=input("choose a option").lower()

 if choose=="q":
     print('goodbye bitch')
     break

if choose =='a':
   add=input_value("enter the question")
   opt=input_data('enter option') 
   for i in range (opt(1,4)):
     quiz.append({add:opt})
                 









                 