n = int(input("Enter number "))
ans=0
k=n
while(n>0):
  r = n%10
  ans = ans*10+r
  n=int(n/10)
  



if k==ans:
  print("No is Palindrom ") 
else:
  print("No is not palindrom")