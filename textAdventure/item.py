# item.py

class Item:
    def __init__(self, name, price, description, effect=None, weight=1):
        self.name = name
        self.price = price
        self.description = description
        self.effect = effect  # Effect can be a dict for complex effects
        self.weight = weight

    def use(self, player):
        if self.effect:
            print(f"You used {self.name}. Effect: {self.effect.get('description', 'No specific effect')}")
            # Implement specific effects based on item
            effect_type = self.effect.get("type")

            if effect_type == "heal":
                heal_amount = self.effect.get("amount", 10)
                player.health += heal_amount
                print(f"Your health has been restored by {heal_amount}. Current health: {player.health}.")
            elif effect_type == "increase_attack":
                increase_amount = self.effect.get("amount", 1)
                player.attack_power += increase_amount
                print(f"Your attack power has been increased by {increase_amount}. Current attack power: {player.attack_power}.")
            elif effect_type == "increase_inventory":
                additional_weight = self.effect.get("amount", 5)
                player.max_weight += additional_weight
                print(f"Your inventory capacity has been increased by {additional_weight}. New max weight: {player.max_weight}.")
            # Add more effects as needed
            else:
                print("Unknown effect type.")
        else:
            print("This item has no effect.")

# Example item definitions
healing_potion = Item(
    name="Healing Potion",
    price=5,
    description="Heals 10 HP",
    effect={"type": "heal", "amount": 10},  # 10 HP healing
)

strength_potion = Item(
    name="Strength Potion",
    price=10,
    description="Increases attack power by 5 for one battle.",
    effect={"type": "increase_attack", "amount": 5},  # Increases attack power
)

backpack = Item(
    name="Backpack",
    price=15,
    description="Increases your carrying capacity by 5.",
    effect={"type": "increase_inventory", "amount": 5},  # Increases max weight
    weight=3  # Weight of the backpack itself
)

# You can create instances of these items when needed in your game logic.
