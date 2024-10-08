class Quest:
    def __init__(self, description, reward, objectives):
        self.description = description
        self.reward = reward
        self.objectives = objectives  # List of objectives
        self.completed_objectives = 0  # Track completed objectives
        self.completed = False

    def complete_objective(self):
        if self.completed:
            print("Quest is already completed.")
            return
        
        if self.completed_objectives < len(self.objectives):
            self.completed_objectives += 1
            print(f"You completed the objective: {self.objectives[self.completed_objectives - 1]}.")
        else:
            print("All objectives already completed.")

        # Check if all objectives are completed
        if self.completed_objectives == len(self.objectives):
            self.complete_quest()

    def complete_quest(self, player):
        if not self.completed:
            print(f"You completed the quest: {self.description}!")
            player.gold += self.reward
            print(f"You received {self.reward} gold as a reward.")
            self.completed = True
        else:
            print("You have already completed this quest.")

    def get_status(self):
        status = f"Quest: {self.description}\n"
        status += f"Objectives completed: {self.completed_objectives}/{len(self.objectives)}\n"
        status += "Objectives:\n"
        for idx, objective in enumerate(self.objectives):
            status += f"  {idx + 1}. {objective} - {'Completed' if idx < self.completed_objectives else 'Not completed'}\n"
        return status

# Function to create multiple quests with objectives
def create_quests():
    quests = [
        Quest("Find the hidden treasure!", reward=10, objectives=["Locate the treasure map", "Reach the treasure location"]),
        Quest("Defeat the Goblin King!", reward=15, objectives=["Find the Goblin King's lair", "Defeat the Goblin King"]),
        Quest("Rescue the captured villager!", reward=20, objectives=["Locate the villager's location", "Defeat the captors"]),
        Quest("Collect 5 herbs for the healer.", reward=5, objectives=["Collect 5 healing herbs"]),
        Quest("Retrieve the lost amulet from the cave.", reward=25, objectives=["Find the cave", "Retrieve the amulet"])
    ]
    return quests
