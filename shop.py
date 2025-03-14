def shop(shop):
    import pandas as pd
    print(f'''Avalile Items List Of Store
      {shop}
      ''')

    total = 0
    total_quantity = 0
    products_purchased = set()
    products_purchased_count = 0
    purchased_items = []

    while True:
        item = input("Enter product name : ").lower()
        if item in shop['products'].values:
            index = shop[shop['products'] == item].index[0]   
            print(f"{item} is of RS {shop.loc[index,"price"]}")
            quantity = int(input("How much do you want : "))       
            if quantity<= shop.loc[index,"quantity"]:
                total += quantity*shop.loc[index,"price"]
                total_quantity += quantity

                if item not in products_purchased:
                    products_purchased_count += 1
                    products_purchased.add(item)

                purchased_items.append({
                    "Product": item,
                    "Quantity": quantity,
                    "Price": shop.loc[index, "price"],
                    "Total Price": quantity * shop.loc[index, "price"]
                })
                    
                if total>=50000:
                    discount = total*0.02
                elif total>=25000:
                    discount = total*0.01
                else:
                    discount = total*0

                shop.loc[index,"quantity"]-=quantity

                while True:
                    more = input("Do you need anything more (y/n): ").lower()
                    if more in ['y', 'n']:
                        break
                    else:
                        print("Invalid input! Please enter only 'y' or 'n'.")

                if more=='y':
                    continue
                elif more =='n':
                    print(f"\nThe total amount of {total_quantity} products is {total}") 
                    break
                
            else:
                print("There are not that many")
        
        else:
            print("Sorry It isn't Avalible")

    print("\n\t--- Purchased Items Recipt ---")
    if purchased_items:
        purchased_df = pd.DataFrame(purchased_items)
        print(purchased_df)


    print(f'''
        ------Shopping Summery------
        Total Item purchased {products_purchased_count}
        Total Quantity purchased {total_quantity}
        Total purchased amount: {total}
        Discount amt: {discount}
        Amount payable: {total-discount}
        ''')
    print("\t\tThanks For Shopping")

import pandas as pd 

tech_shop =pd.DataFrame( {'products' : ['handfree','charger','data_cable','powerbank','usb','air_buds',
                           'mobile_cover','protecter','mouse','ketboard','monitor','mouse_pad',
                           'cooler','smart_watch','smart_box'],
            'price' :  [300,500,200,5000,1000,3000,500,200,300,1000,5000,150,200,5000,5000],
            'quantity' : [100,100,150,50,100,50,300,500,150,100,50,200,100,100,50]
            })


shop(tech_shop)