import calendar
dd = int(input("enter Date: "))
mm = int(input("Enter Month: "))
yy = int(input("Enter Year: "))

listt = calendar.monthcalendar(yy,mm)

if dd <= max(max(listt)) and dd > 0:
    print("valid")
else:
    print("Invalid")
