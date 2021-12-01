def TransNb10VersHexa(x):
    vBase10 = x
    pMax = 0
    vBase16 = ""
    while vBase10 > 16**pMax:
        pMax = pMax + 1
    while pMax >= 0:
        if 16**pMax <= vBase10:
            mMax = 0
            while vBase10 >= mMax * (16 ** pMax):
                mMax = mMax + 1
            mMax = mMax - 1
            if mMax < 10:
                vBase16 = vBase16 + str(mMax)
                vBase10 = vBase10 - (mMax * (16 ** pMax))
            else:
                vBase16 = chr(mMax + 55)
                vBase10 = vBase10 - (mMax * (16 ** pMax))
        else:
            vBase16 = vBase16 + "0"
        pMax = pMax - 1
    print(vBase16)
    return (vBase16)


TransNb10VersHexa(2)
TransNb10VersHexa(2609)
TransNb10VersHexa(10)
TransNb10VersHexa(15)
