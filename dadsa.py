for i in range(1,100):
    a = 1
    for k in range(1, i + 1):
        a *= k

    print(i,str((a + 1)))
