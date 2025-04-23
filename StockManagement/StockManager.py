"""
1.View Product
2.Buy Product
2.Exit App
"""
laptops =[["Product","Brand","Stock","Price"],["Macbook", "Apple",   200,  450000], ["Zenbook","Asus",100,350000],["Swift","Acer",200,350000]]
print("------------1.Buy Product-------------------")
print("------------2.View Product-----------------")
print("----------------3.Exit--------------------")
purchased = False
while True:
    try:
        a = int(input("Enter '1' to 'View product', '2' to 'Buy Product', '3' to 'Exit': "))
        if a == 3:
            print("-------------------------------")
            print("--------------Exit-------------")
            print("-------------------------------")
            break
        elif a == 2:
            print("------------------------------")
            productName = input("Enter the product you want to buy")
            for laptop in laptops:
                if productName.lower() == laptop[0].lower():
                    quantity=int(input("Enter the quantity you want to buy"))
                    laptop[2] -= quantity
                    print("You succesfullt bought",quantity,productName)
                    print("Stock available", laptop[2])
                    purchased = True
            if not purchased:
                print("Product not found")
        elif a == 1:
            print("-------------------------------")
            for row in laptops:
                for cell in row:
                    print(cell, end="\t")
                print(end="\n")
                print("-------------------------------")

        else:
            print("Please, enter either  '1' or '2' or '3' ")

    except ValueError:
        print("Please enter a valid number")
    except Exception :
        print("An error occurred:")



