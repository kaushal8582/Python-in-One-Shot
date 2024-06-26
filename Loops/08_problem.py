number  =134
k=2
check = False

while  k<=number/2:
  if number%k==0:
    check=True
    break
  k+=1

if check==True:
  print("Number is Prime ")
else:
  print("Number is not Prime ")


