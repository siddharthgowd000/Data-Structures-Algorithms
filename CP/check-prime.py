n=int(input())
c=0
if n==1 or n==0:
  print('not prime')
else:
  for i in range(2,n):
    if n%i == 0:
      c=c+1
      break
  if c==0:
    print(str(n)+" is a Prime Number")
  else:
    print(str(n)+" is not a prime number")
