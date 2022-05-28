""" 
GameCharacter is parent-class and represents any in-game character (player/enemy);
Player class is child-class that inherits from GameCharacter and represents user's character;
Enemy class is child-class that inherits from GameCharacter and represents enemies that player battles in the game. 
"""
import random


class GameCharacter:
    """A basic class representing an in-game character (player or enemy)"""

    def __init__(self, name: str, hp: int, damage_1: int, damage_2: int):
        """initialize basic attributes of game's characters"""
        self.name = name
        self.hp = hp
        self.damage_1 = damage_1
        self.damage_2 = damage_2

    def successful_attack(self, y: int) -> int:
        """
        Deducts attack damage from character HP and returns new character HP value:
        self.hp = successful_attack(self.hp, character_attack)
        """
        self.hp -= y
        return self.hp

    def failed_attack_msg(self):
        """return a simple message to report that attack missed and caused no damage"""
        print(f"\nThe {self.name}'s attack missed...")

    def roll(self) -> int:
        """returns a random number to mimic a single roll of a 20-sided game-die"""
        roll = random.randint(1, 20)
        return roll


class Player(GameCharacter):
    """
    class representing User's character in a given game session;
    - at present, one player object will be initialized at start of each game session with all attributes set to zero or none (i.e., name = '', hp = 0, damage_1 = 0...);
    - when user selects playable character the traits/info of character selected will determine values of player-object's attributes.
    """

    def __init__(self, name: str, hp: int, damage_1: int, damage_2: int, potions: int):
        """initialize the attributes for child-class - Player - inherit attributes from parent-class GameCharacter"""
        super().__init__(name, hp, damage_1, damage_2)
        self.potions = potions

    def user_select(self):
        """user selects playable character"""
        select = input("\n1) Mage\n2) Warrior\n3) Thief\nChoose Your Character: ")
        """User's choice for user applies relevant character info/stats to player's character for game session"""
        return select

    def hp_boost(self) -> int:
        """An increase to self.hp awarded when enemy defeated"""
        self.hp += 100
        return self.hp

    def basic_boost(self) -> int:
        """An increase to self.damage_1 awarded when enemy defeated"""
        self.damage_1 += 5
        return self.damage_1

    def strong_boost(self) -> int:
        """An increase to self.damage_2 awarded when enemy defeated"""
        self.damage_2 += 5
        return self.damage_2

    def player_select_msg(self):
        """a message displayed after user selects character from list of playable characters - displays player's stats/info"""
        print(
            f"\nYou have selected to play as the {self.name}\nHP: {self.hp}\nBasic Attack Damage: {self.damage_1}\nStrong Attack Damage: {self.damage_2}\nHealth Potions: {self.potions}\n\nBrave {self.name}, you must defeat the monsters that plague this land and free the people from their torment!"
        )

    def game_over_msg(self):
        """A simple message displayed if user's character HP <= 0"""
        print(
            f"\nThe {self.name} has been killed...Evil still persists in the land...\nGame Over"
        )

    def game_won_msg(self):
        """a simple message displayed when all monsters defeated"""
        print(
            f"\nThank you, brave {self.name}, for you have eliminated the evil that has plagued this land..."
        )

    def quest_select(self) -> str:
        """a prompt to select quest/enemy the user wants to battle next; returns user's selection"""
        quest = input(
            f"\n1) Goblin\n2) Ogre\n3) Orc\n4) Dragon\n\nBrave {self.name}, select your next foe: "
        )
        return quest

    def already_defeated_msg(self, monster):
        """A simple message when user selects enemy already in completed_quests list"""
        print(
            f"\nBrave {self.name}, you have already defeated the {monster.name}. Please select a monster you have not fought."
        )

    def player_turn_msg(self):
        """Message displayed to user at start of User turn during battle"""
        print(
            f"\nBrave {self.name}, your basic attack causes {self.damage_1} damage and has a 70% success rate\nYour strong attack causes {self.damage_2} damage and has a 25% success rate\nYou have {self.potions} health potions remaining"
        )

    def user_turn(self) -> str:
        """prompt user for action to perform on current turn in battle; return selection"""
        turn = input(
            f"\n1) Basic Attack\n2) Strong Attack\n3) Use Health Potion\n\n{self.name}, what action will you perform: "
        )
        return turn

    def basic_attack_msg(self):
        """a message that displays if user chooses basic attack"""
        print(
            f"\nBrave {self.name}, you have chosen to perform a Basic Attack.\nAttack successful if you roll between 3 and 18..."
        )

    def strong_attack_msg(self):
        """a message displayed when user chooses strong attack"""
        print(
            f"\nBrave {self.name}, you have chosen to perform a Strong Attack.\nAttack successful if you roll between a 4 and 10..."
        )

    def player_basic_attack_msg(self, player_roll: int, monster):
        """A message that displays results of player's successful basic attack; includes current hp for monster and player"""
        print(
            f"\n{self.name} rolled {player_roll}\nAttack Successful!\n{self.name} caused {self.damage_1} damage to {monster.name}\n{monster.name}'s HP: {monster.hp}\n{self.name}'s HP: {self.hp}"
        )

    def player_strong_attack_msg(self, player_roll: int, monster):
        """A message that displays the results of player's successful strong attack; includes current hp for monster and player"""
        print(
            f"\n{self.name} rolled {player_roll}\nAttack Successful!\n{self.name} caused {self.damage_2} damage to {monster.name}\n{monster.name}'s HP: {monster.hp}\n{self.name}'s HP: {self.hp}"
        )

    def health_potion_msg(self):
        """a message displayed when user opts to use health potion and has > 0 remaining"""
        print(
            f"\n{self.name} used a health potion. You now have {self.potions} health potions left\n20 HP added to {self.name}'s HP. Current HP: {self.hp}"
        )

    def no_potion_msg(self):
        """a message displayed when user has 0 health potions remaining"""
        print(f"\nThe {self.name} is out of health potions...")

    def monster_defeated_msg(self, monster):
        """a message displayed if monster's HP <= 0 during player's turn"""
        print(f"\nBrave {self.name}, you have defeated the {monster.name}!")

    def stats_boost_msg(self):
        """a message displaying player stats after with stats-boost applied after defeating a monster"""
        print(
            f"\n{self.name} awarded stats boost:\n{self.name} HP: {self.hp}\n{self.name} basic attack damage: {self.damage_1}\n{self.name} strong attack damage: {self.damage_2}"
        )

    def player_defeated_msg(self, monster):
        """a message displayed if player's HP <= 0 during monster turn"""
        print(f"\nThe {self.name} has been killed. The {monster.name} has won...")


class Enemy(GameCharacter):
    """class representing game enemies/monsters - Enemy is a child-class that inherits from parent-class GameCharacter; currently, 4 objects created in-game from Enemy class: goblin, ogre, orc, and dragon"""

    def __init__(self, name: str, hp: int, damage_1: int, damage_2: int):
        """initialize the attributes for Enemy class and inherit from parent-class GameCharacter"""
        super().__init__(name, hp, damage_1, damage_2)
        self.choice = hp * 0.5

    def attack_choice(self) -> str:
        """when a monster's hp <= percentage of starting HP, monster is able to utilize strong attack. Each turn monster attack determined randomly by program"""
        choices = ["basic", "strong"]
        attack = random.choice(choices)
        return attack

    def monster_stats_msg(self):
        """Print message about enemy user will face at outset of battle"""
        print(
            f"\n{self.name} HP: {self.hp}\nBasic Attack Damage: {self.damage_1}\nStrong Attack Damage: {self.damage_2}"
        )

    def monster_basic_attack_msg(self, player):
        """a simple message displayed when monster lands successful basic attack - informs user of relevant information and damage caused to player"""
        print(
            f"\nThe {self.name} attacked and you've been hit!\n{self.name}'s attack causes {self.damage_1} to {player.name}\n{player.name}'s HP: {player.hp}\n{self.name}'s HP: {self.hp}"
        )

    def monster_strong_attack_msg(self, player):
        """a simply message displayed when monster lands successful strong attack - informs user of relevant information and damage caused to player"""
        print(
            f"\nThe {self.name} attacked and you've been hit!\n{self.name}'s attack causes {self.damage_2} to {player.name}\n{player.name}'s HP: {player.hp}\n{self.name}'s HP: {self.hp}"
        )

    def check_if_defeated(self, quest_list: list) -> bool:
        """check to see if monster's name in list of enemies that have already been defeated - disallows user from battling monster more than once in a given game session"""
        if self.name.lower() in quest_list:
            return True
        else:
            return False
