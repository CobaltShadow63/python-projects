# enemy.py

class Enemy:
    def __init__(self, name, health, attack_damage, experience_reward=0):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.experience_reward = experience_reward

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} HP left.")
