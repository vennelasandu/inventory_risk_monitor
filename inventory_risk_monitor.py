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
        if len(products) == 0:
            print("No products in the inventory.")
        else:
            print("\nAll products in store")
        print("ID \tName \tQty \tThreshold \tStatus")
        print("-" * 50)
        for pid in products:
            if products[pid]["qty"]<=products[pid]["threshold"]:
                status="Low stock please reorder"
            else:
                status="Stock is enough"
            print(pid," ",products[pid]["name"]," ",products[pid]["qty"]," ",products[pid]["threshold"]," ",status)
    
    
    #---Add new product in store---
    
    elif option=="2":
        pid=input("Enter product id:").strip()
        if pid=="":
            print("**Product id cannot be empty**")
        elif pid in products:
            print("**Product id must be unique to add the product,please enter new product id**")
        else:   
            name=input("Enter product name:").strip()
            
            if name=="":
                print("**Product name cannot be empty**")
            
            else:
                duplicate_name=False

                for existing_id in products:
                    if products[existing_id]["name"].lower() == name.lower():
                        duplicate_name=True
                        break
                if duplicate_name:
                    print("**Product name already exists, please enter a different product name**")
                    break
            qty=int(input("Enter product qty:"))
            threshold=int(input("Enter product threshold:"))
                    
        
        
        products[pid]={"name":name,"qty":qty,"threshold":threshold}

       
        print("Product added successfully")


    #---Update product qty or Restock---
    elif option=="3":
        pid=input("Enter product id to restock :")
        if pid not in products:
            print("**Product not found**")
            
        else:
            print("Product found:",products[pid]["name"])
            qty=int(input("Enter new qty to restock:"))
            products[pid]["qty"]+=qty
            print("Product qty restocked successfully")

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
        print("\nId\tName\tQty\tThreshold\trisk_ratio\tStatus")

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
        for item in  ranked_products:
            print(
                item[0],"\t",
                  item[1],"\t",
                  item[2],"\t",
                  item[3],"\t",
                  item[4],"\t",
                  item[5]
            )


    #---Exit---
    elif option=="6":
        print("Exiting Inventory Risk Monitor")
        break
    else:
        print("**Invalid option, please try again**")
