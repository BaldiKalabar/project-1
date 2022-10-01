s=int(input('бщая суммы покупки'))
if s >= 1000:
    b= (30 * s) / 100
    print(s-b)
else:
    print(s)