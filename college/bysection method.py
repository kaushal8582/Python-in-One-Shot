neg = None
pos = None

equation = input("Enter equation, ex: x^2-6*x+5 --> ")
equation = equation.replace("^", "**")

def fun(x):
    m = equation.replace("x", str(x))
    return eval(m)

ite = 0
while neg is None or pos is None:
    value = fun(ite)
    if value < 0 and neg is None:
        neg = ite
    elif value > 0 and pos is None:
        pos = ite
    ite += 1

k = 1
mid = 0
while k != 11:
    mid = (neg + pos) / 2
    value = fun(mid)
    if value < 0:
        neg = mid
    else:
        pos = mid
    k += 1

print("The root is:", mid)
