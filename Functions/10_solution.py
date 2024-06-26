# factorial number 

def factorial_recur(num):
  if(num==1):
    return 1
  return num * factorial_recur(num=num-1)  


result = factorial_recur(5);
print(result)
  
