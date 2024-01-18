''' file.open()
lines = file.readlines()
file.write("Hi! this is siddharth")
file.close()

# if you use WITH statement then it will automatically closes once block exits.
content = file.read()

'''
#Reading
try:
    with open("text.txt", "r") as file:
        content = file.read()
        print("Details Inside my file: ")
        for i in content:
            print(i,end="")
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"An error occured : {e}")

#Writing
try:
    with open("text.txt", "r+") as file:
        file.write("Hi! I'm Siddharth.")
        content = file.read()
        print("\nDetails Inside my file: ")
        for i in content:
            print(i,end="")
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"An error occured : {e}")
    

