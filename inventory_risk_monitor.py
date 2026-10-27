products={
    "p1":{"name":"Candles","qty":20,"threshold":10},
    "p2":{"name":"pen","qty":30,"threshold":20},
    "p3":{"name":"pencils","qty":5,"threshold":10},
    "p4":{"name":"notebook","qty":20,"threshold":50},
    "p5":{"name":"bag","qty":15,"threshold":10},
    "p6":{"name":"papers","qty":20,"threshold":10},
    "p7":{"name":"toys","qty":25,"threshold":8},
    "p8":{"name":"cards","qty":10,"threshold":10},
    "p9":{"name":"chocolate","qty":50,"threshold":30},
    "p10":{"name":"pouch","qty":18,"threshold":20},
    "p11":{"name":"Candies","qty":5,"threshold":1},
    "p12":{"name":"chips","qty":5,"threshold":20},
    "p13":{"name":"watches","qty":2,"threshold":8},
    "p14":{"name":"bottles","qty":8,"threshold":15},
    "p12":{"name":"box","qty":2,"threshold":5},
}

while True:
    print("\n*******Inventory Risk Monitor*******")
    print("1.show all products")
    print("2.Add new product")
    print("3.Update product qty or Restock")
    print("4.Sale product")
    print("5.Risk ranking for threshold products")
    print("6.Exit")
    option=input("Enter your option:")
    #---show all products in store---
    if option=="1":
        print("All products in store")
        print("\nId  \tName \tQty  \tThreshold  \tStatus")
        for pid in products:
            if products[pid]["qty"]<=products[pid]["threshold"]:
                status="Low stock please reorder"
            else:
                status="Stock is enough"
            print(pid," ",products[pid]["name"]," ",products[pid]["qty"]," ",products[pid]["threshold"]," ",status)
    #---Add new product in store---
    elif option=="2":
        pid=input("Enter product id:")
        #uniqueness check for id
        if pid in products:
            print("**Product id must be unique,please enter new product id**")
            break
        
        name=input("Enter product name:")
        if name in products:
            print("**Check Product name again to avoid duplicate product name**")
            break
        qty=int(input("Enter product qty:"))
        threshold=int(input("Enter product threshold:"))
        products[pid]={"name":name,"qty":qty,"threshold":threshold}

       
        print("Product added successfully")


    #---Update product qty or Restock---
    elif option=="3":
        pid=input("Enter product id to update:")
        if pid in products:
            print("Product found:",products[pid]["name"])
            qty=int(input("Enter new qty to update:"))
            products[pid]["qty"]+=qty
            print("Product qty updated successfully")
        else:
            print("**Product not found**")

    #---Sale product---
    elif option=="4":
        pid=input("Enter product id to sale:")
        if pid in products:
            print("Product found:",products[pid]["name"])
            qty=int(input("Enter qty to sale:"))
            if qty>products[pid]["qty"]:
                print("**Insufficient stock for sale**")
            else:
                products[pid]["qty"]-=qty
                print("Product sold successfully")
        else:
            print("**Product not found**")

    #---Risk ranking for threshold products---
    elif option == "5":
        print("Risk ranking for threshold products")
        print("\nId  \tName \tQty  \tThreshold  \tStatus")

        if len(products)==0:
            print("No products in store")

        ranked_products=[]
        for pid in products:
            risk_ratio=round(products[pid]["qty"]/products[pid]["threshold"],2)
            if risk_ratio>1:
                status="Low risk"
            elif risk_ratio==1:
                status="Medium risk"
            else:
                status="High risk"
            ranked_products.append((pid, products[pid]["name"], products[pid]["qty"], products[pid]["threshold"], risk_ratio, status))
        ranked_products.sort()
        print(ranked_products)


    #---Exit---
    elif option=="6":
        print("Exiting Inventory Risk Monitor")
        break
    else:
        print("**Invalid option, please try again**")