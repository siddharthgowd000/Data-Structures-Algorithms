class Canteen:
    items = ["Tea", "Coffee", "Poha"]
    prices = [10, 20, 30]
    stock = [100, 150, 200]
    def menu():
        print("---------------------")
        for i,j in zip(Canteen.items, Canteen.prices):
            print(i,j,sep=" - ")
        print("---------------------")
    def order(item,quantity):
        bill=0
        for i in Canteen.items:
            if i == item:
                if Canteen.stock[Canteen.items.index(i)] >= quantity:
                    print("Ordered Successfully")
                    bill= Canteen.prices[Canteen.items.index(i)] * quantity
                    Canteen.stock[Canteen.items.index(i)] = Canteen.stock[Canteen.items.index(i)] - quantity
                else:
                    print("Quantity Not Available")
        return bill


Canteen.menu()
i=1
bill=0
while i:
    item = input("Enter the Item: ")
    quantity = int(input("Enter the Qunatity: "))
    bill += Canteen.order(item, quantity)
    print("Do you want order more: (0/1)")
    i = int(input())
print("Bill - "+ str(bill))
print("Thank You Visit Again !")

