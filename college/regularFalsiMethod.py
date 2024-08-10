
x0 = None
x1=None

equation = input("Enter equation , ex:- x^2+6*2+5 -->  ")
equation = equation.replace("^","**")


def fun(x):
  m =equation.replace("x",str(x))
  return eval(m)


def findX0AndX1():
  global x0,x1
  ite =0
  while x0==None or x1 == None:
    value = fun(ite)
    if value <0:
      x0 =ite
    else:
      x1 =ite
    ite+=1


def calculate():
  return x1 - (fun(x1) * (x1 - x0)) / (fun(x1) - fun(x0))


def main():
  findX0AndX1()
  global x1,x0
  print(x0,x1)
  k=1
  value =None
  .
  
  while k!=11:
    value = calculate()
    isPositeiveORNegative =fun(value)
    if isPositeiveORNegative <0:
      x0 =value
    else:
      x1 = value
    k+=1
  print("Roots is : ", value)



if __name__ == "__main__":
  main()