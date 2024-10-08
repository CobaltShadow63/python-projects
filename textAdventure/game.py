# game.py

from colorama import Fore, Style, init
from player import Player
from enemy import Enemy
from shop import Shop
from quest import Quest, create_quests
from world import create_world
import json
import os

# Initialize Colorama
init(autoreset=True)

def display_status(player):
    print("\n" + "-" * 40)
    print(f"{Fore.CYAN}Player: {player.name}")
    print(f"{Fore.GREEN}Health: {player.health} | Gold: {player.gold} | Level: {player.level}")
    print(f"{Fore.YELLOW}Inventory: " + ", ".join(item.name for item in player.inventory) if player.inventory else "Empty")
    print("-" * 40 + "\n")

def move_player(player, direction):
    player.move(direction)
    random_event(player)  # Call random_event function after moving

def save_game(player):
    save_data = {
        "name": player.name,
        "health": player.health,
        "gold": player.gold,
        "level": player.level,
        "inventory": [item.name for item in player.inventory],
        "quests": [{"description": quest.description, "completed": quest.completed} for quest in quests]
    }

    with open("save_game.json", "w") as f:
        json.dump(save_data, f)
    print(f"{Fore.GREEN}Game saved successfully!")

def load_game():
    if os.path.exists("save_game.json"):
        with open("save_game.json", "r") as f:
            save_data = json.load(f)
            player = Player(save_data["name"])
            player.health = save_data["health"]
            player.gold = save_data["gold"]
            player.level = save_data["level"]
            # Rebuild inventory and quests from save data
            player.inventory = [Item(item_name) for item_name in save_data["inventory"]]
            for quest_data in save_data["quests"]:
                quest = Quest(quest_data["description"], reward=0)  # Set reward to 0 for loading
                quest.completed = quest_data["completed"]
            print(f"{Fore.GREEN}Game loaded successfully!")
            return player
    else:
        return None

def start_game():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    starting_room, treasure_room = create_world()
    player.current_room = starting_room
    shop = Shop()  # Create a shop instance
    global quests
    quests = create_quests()  # Create multiple quests

    print("\nWelcome to the adventure game!")
    print("Commands: move <direction>, pick up <item>, use <item>, attack <enemy>, shop, quest, complete quest, inventory, quit")

    while True:
        display_status(player)
        command = input(f"{Fore.MAGENTA}> ").lower().strip()
        
        if command == "quit":
            save_game(player)
            print(f"{Fore.BLUE}Thanks for playing!")
            break
        elif command.startswith("move"):
            direction = command.split()[1]
            move_player(player, direction)
        elif command.startswith("pick up"):
            item_name = command.replace("pick up ", "")
            player.pick_up(item_name)
        elif command == "shop":
            shop.display_items()
        elif command.startswith("buy"):
            item_name = command.replace("buy ", "")
            shop.sell_item(player, item_name)
        elif command.startswith("quest"):
            for quest in quests:
                print(f"{Fore.YELLOW}- {quest.description} (Reward: {quest.reward} gold) - {'Completed' if quest.completed else 'Not completed'}")
        elif command.startswith("complete quest"):
            quest_name = command.replace("complete quest ", "")
            for quest in quests:
                if quest_name in quest.description:
                    quest.complete_quest(player)
                    break
            else:
                print(f"{Fore.RED}No such quest found.")
        elif command == "inventory":
            if player.inventory:
                print(f"{Fore.GREEN}You have the following items:")
                for item in player.inventory:
                    print(f"{Fore.YELLOW}- {item.name}")
            else:
                print(f"{Fore.YELLOW}Your inventory is empty.")
            print(f"{Fore.GREEN}You have {player.gold} gold.")
        elif command.startswith("use"):
            item_name = command.replace("use ", "")
            player.use_item(item_name)
        elif command.startswith("attack"):
            enemy_name = command.replace("attack ", "")
            if player.current_room.enemy:
                player.attack(player.current_room.enemy)
            else:
                print(f"{Fore.RED}There's nothing here to attack.")
        else:
            print(f"{Fore.RED}Unknown command. Try 'move <direction>', 'pick up <item>', 'use <item>', 'attack <enemy>', 'shop', 'quest', or 'inventory'.")

if __name__ == "__main__":
    player = load_game()
    if player is None:
        start_game()
