products = []

while True:

    print(  
        f"===== INVENTORY MANAGER =====\n"
        "1 - Add product\n"
        "2 - Show products\n"
        "3 - Search product\n"
        "4 - Update stock\n"
        "5 - Remove product\n"
        "6 - Exit"
        )
    
    option = int(input("choose an option: "))

    if option == 1:
        print("Add Product")
        product = {

        "name": input(f"name: ").lower(),
        "price": float(input(f"price: ")),
        "stock": int(input(f"stock: "))
        }

        products.append(product)
        print("Product added successfully!")

    elif option == 2:
        if len(products) == 0:
            print("No products Registered.")
        
        else:
            print (f"Products:")
           
            for product in products:
                print("=" * 25)

                for key, value in product.items():
                    print (f"{key.capitalize():<8}: {value}")

                print("=" * 25)

    elif option == 3:
        if len(products) == 0:
            print("No products Registered.")
        
        else:
            print("Search Products")
            search_product = input("which product do you want to look for? ").lower()
            found = False
            for product in products:
                
                if search_product == product["name"]:
                    print("\nProduct Found!")
                    print("=" * 25)
                    

                    for key,value in product.items():
                        print(f"{key}: {value}")
                    print("=" * 25)
                
                found = True
                break

    elif option == 4:
        if len(products) == 0:
            print("No products Registered.")
        
        else:
            print("Updade products")
            product_update = input("Product name")
            product_found = False


            for product in products:
                
                if (product_update == str(product.get("name", "")).lower() or
                    product_update == str(product.get("price", "")) or
                    product_update == str(product.get("stock", ""))):
                    print("\nProduct Found!")
                    
                    product_found = True
                    
                update_line = input("What field do you want to update? ")
                field_found = False
            
                for value in product:
                    if update_line == value:
                        print("Found")
                        new_value = input("New value for update")
                        product[update_line] = new_value
                        field_found = True
                        break

                if not field_found:
                    print("Field not found.")
                
                break

            if not product_found:
                print("Product not found.")