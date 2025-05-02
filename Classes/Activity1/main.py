from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

player_list = [Player('Gregor', 'Knight', 'Protector', 20, 240), 
               Player('Ebor', 'Wizard', 'Protector', 25, 150), 
               Player('Loern', 'Witch', 'Protector', 30, 120), 
               Player('Lebron', 'King', 'Protector', 50, 500)]

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapon_sword = Weapon('Sword', 'Melee', random.randint(12, 15))

weapon_list = [Weapon(), 
               Weapon(), 
               Weapon(), 
               Weapon()]
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy_chief = Enemy('Chief', 'Goblin', random.randint(15, 18), random.randint(80, 140))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {weapon_sword.name}")
print(f"Weapon Category: {weapon_sword.category}")
print(f"Weapon Damage: {weapon_sword.dmg}")

# TODO: Print the enemy character details
print(f"Enemy Name: {enemy_chief.name}")
print(f"Enemy Race: {enemy_chief.race}")
print(f"Enemy Damage: {enemy_chief.dmg}")
print(f"Enemy Health: {enemy_chief.health}")