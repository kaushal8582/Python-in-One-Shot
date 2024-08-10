
n = int (input("Enter number : "))
l1 =[]     
for i in range(n+1):
    l2=[]
    for j in range(i+1):
        if i==j or j==0:
            l2.append(1)
        else:
            sum = l1[i-1][j-1]+ l1[i-1][j]
            l2.append(sum)
    l1.append(l2)

for row in l1:
    print(row)


# step1 ->  first to get input like n
# first empty list lo , then ek loop lagao n tak ok, 
# then ek or second list do jisme her iterate ke baad sum store karenge ,
# then second loop lagao jo chalega 0 to i tak uske or jo second list hai l2 usme agar i==j or j==0 ho to usme 1 store karenge or eske alava kuch bhi ho to hum sum karenge previous row (i-1) row ke under matrix ke under ke  l1array ke under i-1 or j-1 l1[i-1][j-1] index ke value or l1 ke under i-1 or j  l1[i-1][j] index pe jo value ho usko sum karenge then l2 me append kar denge ok 