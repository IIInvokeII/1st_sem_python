stock={'1. Crocin':50,'2. Paracetomol':40,'3. Amrutanjan':20,'4. Energy Drink':30,'5. Dairy Milk':60,'6.Toothpaste':70}
def sell():
    print()
    print(list(stock.items()))
    a=list(stock.keys())
    print("Which product do you want to sell ?(1-",len(stock),"): ",end="")
    p=int(input())
    if p>=1 and p<=(len(a)+1):
        n=int(input("Enter the amount you want to sell: "))
        val=stock.get(a[p-1])
        if(val<=10 or val-n<10):
            print("Please buy more stocks.")
        else:
            stock.update({a[p-1]:val-n})
    else:
        print("Invalid.")

def buy():
    print()
    print(list(stock.items()))
    a=list(stock.keys())
    print("Which product do you want to buy ?(1-",len(stock),"): ")
    p=int(input())
    if p>=1 and p<=(len(a)+1):
        n=int(input("Enter the amount you want to buy: "))
        val=stock.get(a[p-1])
        stock.update({a[p-1]:val+n})
    else:
        print("Invalid.")

def add():
    print()
    print(list(stock.items()))
    a=list(stock.keys())
    p=str(input("Enter the name of the product: "))
    n=int(input("Enter the amount: "))
    stock.update({p:n})
    
def menu():
    c=0
    print()
    while(c!=5):
        print("Stock Program")
        print("1. Add Stocks")
        print("2. Buy Stocks")
        print("3. Sell Stocks")
        print("4. Check Stocks")
        print("5. Exit")
        c=int(input("Enter your choice(1-4): "))
        if(c==1):
            add()
        elif(c==2):
            buy()
        elif(c==3):
            sell()
        elif(c==4):
            print(stock)
        else:
            print("Invalid Choice.")

menu()

    
