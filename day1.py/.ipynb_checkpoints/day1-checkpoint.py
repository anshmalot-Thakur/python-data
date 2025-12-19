# 

# a=int(input("enter the first integer"));
# b=int(input("enter the secand integer"));
# c=int(input("enter the third integer"));
# print("Addition of integers are: ",a+b+c);
# print("subtraction of integers are: ",a-b-c);
# print("divison of integers are: ",a/b/c);
# print("multiplication of integers are: ",a*b*c);

# next question square of number

# a=int(input("enter the number:"))
# print(a**2);

# next question , take temp in celcious as input

# celcious=input("enter the temprature:");
# celcious=float(celcious);
# fahrenheit=(celcious*9/5)+32;
# # print(type(fahrenheit));
# print(celcious,fahrenheit);

# next question sum of numebrs

# a=int(input("enter the divident integer:"));
# b=int(input("enter the divisor integer:"));

# quotient=a//b;
# remainder=a%b;

# print("quotient:",quotient);
# print("remainder",remainder);

# next question sum of numebrs

# p=int(input("enter the value-p:"));
# r=int(input("enter the value-r:"));
# t=int(input("enter the value-t:"));

# si=(p*r*t)/100;
# print(si)

numbers=sum(map(float,input("enter 3 numbers:").replace(',',' ').split()))
print("the sum of numbers is",numbers)
12