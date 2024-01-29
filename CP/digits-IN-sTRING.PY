s=input()
c=0
avrg=0
sum_a=0
string=""

for i in range(len(s)):
    if s[i].isdigit():
        string=string+s[i]
        if i+1 == len(s):
            sum_a += int(string)
            c += 1
            string = ""
            continue
        if s[i+1]==" ":
            sum_a += int(string)
            c += 1
            string = ""
        
        
         
         
avrg=(sum_a/c)
print(sum_a)
print(round(avrg,2))
        
    


    