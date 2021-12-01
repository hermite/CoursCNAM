def TransfBase10VersHexa(x):
    vBase10 = int(x)
    baseResult = 16
    result= ""
    pMax = 0
    while vBase10 > baseResult ** pMax:
        pMax = pMax + 1
    for i in range(pMax):
        if vBase10 >= baseResult ** (pMax - i):
