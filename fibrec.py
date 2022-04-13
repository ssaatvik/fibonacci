def fibrec(n):
    if n <= 1:
        return 1
    else:
        return (fibrec(n-1) + fibrec(n-2))

n = int(input("enter no of terms "))

if n <= 0:
       print("Plese enter a positive integer")
else:
   print("fibonacci sequence  ")
   for i in range(n):
       print(fibrec(i))
