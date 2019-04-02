######### Program to cheak prime number ##########
# n=int(input("Enter the number:"))
# if (n == 1):
#     print("1 is not a prime number")
# else:
#     for i in range(2,n//2):
#         if (n%i==0):
#             print(f"{n} is not a prime number")
#             break
#         else:
#             print(f"{n} is a prime number")
#             break




######## Program for palindrome Number   #########

# org=int(input("Enter a number:"))
# num=org;sum=0
# while(num!=0):
#     r=num%10
#     sum=int(str(sum)+str(r))
#     num=num//10
# if(org==sum):
#     print("Number is palindrome number.")
# else:
#     print("Number is not a palindrome number.")



######### Program for Reverse Number ##########
# org=int(input("Enter a number"))
# num=org;sum=0
# while(num!=0):
#     r=num%10
#     sum=int(str(sum)+str(r))
#     num=num//10
# print("Reverse of the number %d is %d"%(org,sum))


########## Program for Armstrong Number ########

# import math
# org=int(input("Enter a number"))
# num=org;sum=0;count=0
# while(org>0):
#     org=org//10
#     count=count+1
# num=org
# while(num!=0):
#     r=num%10
#     sum=sum+pow(r,count)
#     num=num//10
#
# if(org==sum):
#     print("Number is Armstrong number")
# else:
#     print("Number is not a Armstrong number")



#####  Program for Reverse a string  ########

# s=str(input("Enter the string:"))
# a=s[::-1]
# print(a)


###### Program for factorial of a number ######

# n=int(input("Enter a number:"))
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# a=fact(n)
# print(a)


########  program to print fibbonacci series #######
#
# def fibbo(n):
#     if n<=1:
#         return n
#     else:
#         return fibbo(n-1)+fibbo(n-2)
#
# n=int(input("Enter a number:"))
# if n<=0:
#     print("Please enter positive integer.")
# else:
#     for i in range(n+1):
#         print(fibbo(i))


