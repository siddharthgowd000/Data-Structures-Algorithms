def printStr(*vargs):
    print(len(vargs))
    for i in vargs:
        print(i)
    return

printStr(1,2,3)
printStr(1,2,3,4,5,6,7,8,9)