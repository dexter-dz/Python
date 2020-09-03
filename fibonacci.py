#!/usr/bin/python3
# Program to display the Fibonacci sequence up to n-th term

term = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
i = 0

# check if the number of terms is valid
if term <= 0:
   print("Please enter a positive integer")
elif term == 1:
   print("Fibonacci sequence upto",term,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while i < term:
       print(n1)
       nth = n1 + n2
						# updating values values
       n1 = n2
       n2 = nth
       i += 1