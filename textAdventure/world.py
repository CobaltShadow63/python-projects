# world.py

from room import Room, Puzzle
from item import Item, StrengthPotion, InvisibilityCloak, Backpack
from enemy import Enemy

def create_world():
    foyer = Room("Foyer", "A grand entryway with a dusty chandelier.")
    library = Room("Library", "Shelves line the walls, filled with old books.")
    kitchen = Room("Kitchen", "The smell of stale food fills the air.")
    treasure_room = Room("Treasure Room", "You've found the legendary treasure!", locked=True)
    pitfall = Room("Pitfall", "A dark room with a hidden trap.", trap_damage=5)
    forest = Room("Forest", "A dense forest with hidden traps. Be careful!", trap_damage=3)
    cave = Room("Cave", "A dark cave with a strange marking on the wall. Perhaps there's more here than meets the eye.")
    
    # Puzzle in the treasure room
    puzzle = Puzzle("What has keys but can't open locks?", "piano")
    treasure_room.puzzle = puzzle
    
    foyer.connect_room(library, "north")
    foyer.connect_room(kitchen, "east")
    library.connect_room(treasure_room, "north", locked=True)
    kitchen.connect_room(pitfall, "west")
    library.connect_room(forest, "east")
    forest.connect_room(cave, "north", locked=True)

    # Place items
    key = Item("key", "A small rusty key. Wonder what it unlocks?", weight=1)
    backpack = Item("backpack", "A sturdy backpack that increases carrying capacity.", weight=2, effect=Backpack())
    invisibility_cloak = Item("invisibility cloak", "Makes you invisible for one turn.", weight=3, effect=InvisibilityCloak())

    library.items.append(key)
    forest.items.append(backpack)
    foyer.items.append(invisibility_cloak)

    # Enemies
    goblin = Enemy("Goblin", 10, 3, experience_reward=10)
    ogre = Enemy("Ogre", 20, 5, experience_reward=20)
    library.enemy = goblin
    pitfall.enemy = ogre

    return foyer, treasure_room
