# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
#Sample Dictionary ( n = 5) : 
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("Enter a no.: "))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)