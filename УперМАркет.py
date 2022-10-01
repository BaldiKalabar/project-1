s=int(input('бщая суммы покупки'))
if s >= 1000:
    b= (5 * s) / 100
    print(s-b)
elif s <=5000:
    b= (5 * s) / 100
    print(s-b)
elif s >= 999:
    print(s)
elif s >=5001:
    b= (10 * s) / 100
    print(s-b)
elif s >=10000:
    b= (10 * s) / 100
    print(s-b)
elif s >=10001:
    b= (15 * s) / 100
    print(s-b)
