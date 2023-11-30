# input numerator as n and denominator as d

# if d == 0 display error

# else
    # q = n / d
    # display q

n = int(input("Input the numerator: "))
d = int(input("Input the denominator: "))

if d == 0:
    print("Denominator cannot be 0")

else:
    q = n / d
    print(q)