# main.py

from player import Player
from world import create_world

def main():
    print("Welcome to the Adventure!")
    player_name = input("Enter your name, brave adventurer: ")
    player = Player(player_name)
    
    # Initialize world and set player's starting room
    starting_room, treasure_room = create_world()
    player.current_room = starting_room
    player.current_room.enter(player)
    
    # Game loop
    while True:
        command = input("\nWhat would you like to do? (move [direction], pick up [item], drop [item], attack, heal, quit): ").lower().split()
        
        if command[0] == "move" and len(command) > 1:
            direction = command[1]
            player.move(direction)
            if player.current_room == treasure_room:
                print("Congratulations! You've found the treasure and won the game!")
                break
        elif command[0] == "pick" and command[1] == "up":
            item_name = " ".join(command[2:])
            player.pick_up(item_name)
        elif command[0] == "drop":
            item_name = " ".join(command[1:])
            player.drop(item_name)
        elif command[0] == "attack":
            if player.current_room.enemy:
                player.attack(player.current_room.enemy)
                if player.current_room.enemy.health <= 0:
                    player.current_room.enemy = None
            else:
                print("There's nothing to attack here.")
        elif command[0] == "heal":
            player.heal()
        elif command[0] == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

# Run the game
if __name__ == "__main__":
    main()
