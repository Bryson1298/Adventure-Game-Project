import gamefunctions


gamefunctions.print_welcome()

shop_item1 = input("What is your first item? ")
item1_price = float(input("What is your first price? "))
shop_item2 = input("What is your second item? ")
item2_price = float(input("What is your second price? "))

gamefunctions.print_shop_menu(shop_item1, item1_price, shop_item2, item2_price)

starting_money = float(input('What is the starting money? '))
item_price = float(input('What is the item price? '))

gamefunctions.purchase_item(item_price, starting_money)

gamefunctions.new_random_monster()
