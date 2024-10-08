# player.py

from random import randint
from item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.inventory = []
        self.current_room = None
        self.max_weight = 15
        self.experience = 0
        self.level = 1
        self.invisible = False
        self.attack_power = 5  # Initial attack power
        self.gold = 0

    def level_up(self):
        self.level += 1
        self.health += 5  # Increase max health each level
        self.attack_power += 1  # Increase attack power each level
        print(f"Congratulations! You've leveled up to level {self.level}.")
        print(f"Your health is now {self.health}, and your attack power is now {self.attack_power}.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"You gained {amount} experience points.")
        if self.experience >= self.level * 10:
            self.level_up()

    def calculate_inventory_weight(self):
        return sum(item.weight for item in self.inventory)

    def attack(self, enemy):
        if self.invisible:
            print(f"You catch the {enemy.name} off guard!")
            self.invisible = False  # Invisibility only lasts one attack
        damage = randint(1, self.attack_power)
        print(f"You attack the {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)
        if enemy.health > 0:
            self.take_damage(enemy.attack_damage)
        else:
            self.gain_experience(enemy.experience_reward)

    def move(self, direction):
        exit_info = self.current_room.get_exit(direction)
        if exit_info:
            next_room, is_locked = exit_info
            if is_locked and not any(item.name == "key" for item in self.inventory):
                print("The door is locked! You need a key.")
            else:
                self.current_room = next_room
                print(f"You move {direction}.")
                self.current_room.enter(self)
        else:
            print("You can't go that way.")

    def pick_up(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                if self.calculate_inventory_weight() + item.weight <= self.max_weight:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    print(f"You picked up {item.name}.")
                else:
                    print("It's too heavy! You need to drop something first.")
                return
        print("There's no such item here.")

    def drop(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                print(f"You dropped {item.name}.")
                return
        print("You don't have that item.")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use(self)
                return
        print("You don't have that item.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You have been defeated. Game over!")
            exit()
        else:
            print(f"You have {self.health} HP left.")

    def heal(self):
        healing_potion = next((item for item in self.inventory if item.name == "healing potion"), None)
        if healing_potion:
            self.health += 10
            self.inventory.remove(healing_potion)
            print("You used a healing potion! Health restored to", self.health)
        else:
            print("You don't have any healing items.")
