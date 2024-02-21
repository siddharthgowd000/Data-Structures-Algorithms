strr = "bbbbggggbbbbgggggggggbgggggggbbbgggg"
d = 2
listt = []
for i in strr:
    listt.append([i,0])

for i in range(len(strr)-d):
    for j in range(i+1,d+i+1):
        if strr[i]!=strr[j] and listt[j][1] == 0 and listt[i][1] == 0:
            listt[i] = [strr[i],1]
            listt[j] = [strr[j],1]
            break
c = 0
print(listt)
for i in listt:
    if i[1] == 1:
        c += 1
print(c//2)
