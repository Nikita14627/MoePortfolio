for n in range(150):
    for k in range(150):
        for m in range(150):
            for a in range(150):
                for t in range(150):
                    if n**5+k**5+m**5+a**5 == t**5:
                        print(n+k+m+a+t)