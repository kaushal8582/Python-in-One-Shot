n = int(input("Enter a number "))

l1 =[]
k =1
for i in range(n+1):
    l2 =[]
    for j in range(i+1):
        if i==0 or j==0:
            l2.append(k)
        else:
            k= k+l1[i-1][j-1]
            l2.append(k)
    l1.append(l2)

for row in l1:
    print(row)

#  esme bhi hum first me input lege or n me store karenge 
#  then hum ek empty list lenge l1=[]
# and ek k variable lenge initial value 1 rahega
# then hum ek loop lagaenge n tak and uske under ek or list lenge l2=[] empty 
#  then under me hi ek or loop lagayenge  jo chalega i tak  or uske under i==0 ho j==0 ho to hum jo k ka value ho usko le me append kar denge or dusra ho to hum l1 me previous row me jake ek value lenge jisko k me store karenge  like previous row ke previous column me i-1 or j-1 me jake jo value ho usko leke l1[i-1][j-1] ka value k me plus karke l2 me append kar denge that's done.