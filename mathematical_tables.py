#!/usr/bin/python3

num	=int(input("which table you want to see")) #Number which you want to see table of
a = 21 # Table till the nth no -1
n,n1 = 1,num

if num	<=0: 			#error code if someone enters 0
	print("enter a positive no")
elif num	==1: 		#you know what will happen if you multiply 1
	print("you are too weak")
else:  					#The actual program
	print ("Table of " +str(num) +" is")
	while n < a:
		
		n1 = num * n					#operation command
		print (num," X ", n, " = ", n1) #output in the proper format
		n += 1							# Changing the multiplier
		