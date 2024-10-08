# shop.py

from item import Item  # Make sure to import the Item class

class Shop:
    def __init__(self):
        self.items_for_sale = [
            Item("Healing Potion", 5, "Heals 10 HP"),
            Item("Sword", 10, "Increases attack power"),
            Item("Armor", 15, "Reduces damage taken")
        ]

    def display_items(self):
        print("Items for sale:")
        for item in self.items_for_sale:
            print(f"{item.name} - {item.price} gold: {item.description}")

    def sell_item(self, player, item_name):
        for item in self.items_for_sale:
            if item.name == item_name and player.gold >= item.price:
                player.inventory.append(item)
                player.gold -= item.price
                self.items_for_sale.remove(item)
                print(f"You bought {item.name}!")
                return
        print("You can't buy that!")

