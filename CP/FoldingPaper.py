
def folds(l,mb):
    bfold = 0
    while l != mb:
        if l//2 <= mb:
            l = mb
            bfold += 1
        else:
            l = l//2
            bfold += 1
    return bfold
l,b = 100,60
ml,mb = 2,2

print(folds(l,ml), folds(b,mb))


