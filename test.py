for a in range(1, 10):
    for b in range(1, a+1):
        if b < a:
            print(a, "*", b, "=", (a*b), end="   ")
        else:
            print(a, "*", b, "=", (a*b))
