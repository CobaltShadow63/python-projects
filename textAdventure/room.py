# room.py

class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def solve(self, response):
        """Checks if the response solves the puzzle."""
        return response.lower() == self.answer.lower()


class Room:
    def __init__(self, name, description, locked=False, trap_damage=0, puzzle=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.locked = locked
        self.enemy = None
        self.trap_damage = trap_damage
        self.puzzle = puzzle  # Added puzzle attribute

    def connect_room(self, other_room, direction, locked=False):
        self.exits[direction] = (other_room, locked)

    def get_exit(self, direction):
        return self.exits.get(direction, None)

    def enter(self, player):
        print(f"\n{self.name}")
        print(self.description)
        if self.trap_damage > 0:
            print("It's a trap! You take damage.")
            player.take_damage(self.trap_damage)
        if self.puzzle and self.locked:
            print(f"There's a puzzle here to solve:\n{self.puzzle.question}")
            response = input("Your answer: ")
            if self.puzzle.solve(response):
                print("Correct! The door unlocks.")
                self.locked = False
            else:
                print("That's not correct. The door remains locked.")
        for item in self.items:
            print(f"You see a {item.name} here.")
        if self.enemy:
            print(f"An enemy is here: {self.enemy.name} with {self.enemy.health} HP!")
