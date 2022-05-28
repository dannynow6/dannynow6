""" 
Note: Classes can be anything - nouns, something I might put 'the' in front of: the event, the idea, the mug, etc. 
"""

""" 
'Defeat All Monsters!' (need title) - A Battle/Adventure Game - User must defeat all monsters to save the land...
"""
""" 
Notes/To Do: Create a 'Title Screen' - a main game message that displays when game starts with first input prompt - it will look better... 



--  check out: from art import tprint  --

-- Also, see workshop 5 user_choice() function and use it as a model for Battle Code - make code more concise and readable. 
"""
from a_game_pkg.characters import GameCharacter
from a_game_pkg.characters import Player
from a_game_pkg.characters import Enemy
from a_game_pkg.a_game_mod import check_list


while True:
    """
    Main Game Loop:
    - first display title and initial prompt which allows user to quit program or play game;
    - If play game, user then selects a character from playable character options;
    - playable character selected determines user's stats for game session;
    - User then selects first enemy/monster to battle (gives user ability to experience game in different ways during different game sessions);
    - if enemy/monster already has been defeated during current game session, message displayed and user prompted to select a different enemy/monster to battle;
    - User plays until user's character defeated (hp reduced to 0 or below) or until all enemies/monsters defeated (each enemy's hp reduced to 0 or below);
    - when game ends for either above reason - User prompted to play again or quit program.
    """
    main_prompt = input(
        "\n--------------------------------\n ---- DEFEAT ALL MONSTERS! ---- \n--------------------------------\n\nTo quit game type 'quit' or 'q'\nTo Play Game type any key: "
    )
    if main_prompt.lower() == "q" or main_prompt.lower() == "quit":
        break
    else:
        # User has chosen to play game and must now select a character:
        while True:
            """Loop for user to select a playable character from available options
            List of options for playable characters and function for initial game while loop wherein user able to select character info/traits for playable character in game-session
            """
            playable = {
                "mage": {
                    "name": "Mage",
                    "hp": 175,
                    "damage_1": 25,
                    "damage_2": 80,
                    "potions": 2,
                },
                "warrior": {
                    "name": "Warrior",
                    "hp": 225,
                    "damage_1": 40,
                    "damage_2": 125,
                    "potions": 1,
                },
                "thief": {
                    "name": "Thief",
                    "hp": 180,
                    "damage_1": 25,
                    "damage_2": 85,
                    "potions": 2,
                },
            }
            """ 
            Create the Enemy objects - monsters user will battle during game session;
            - Can easily add new enemies - simply create/copy and paste battle code/enter new enemy's name in relevant spots. 
            """
            goblin = Enemy("Goblin", 140, 15, 40)
            ogre = Enemy("Ogre", 200, 25, 80)
            orc = Enemy("Orc", 250, 30, 100)
            dragon = Enemy("Dragon", 300, 35, 110)
            """completed_quests is empty list created. After enemy defeated by user in a given game session its name is added to completed_quests. List checked so user fights each enemy only once and to determine when user has won the game"""
            completed_quests = []
            # Create empty player-object to assign stats to after user selects:
            player = Player("", 0, 0, 0, 0)

            """
            User selects character and info displayed after selection: 
            """
            user = Player.user_select(player)
            if user == "1" or user.lower() == "mage":
                player.name = playable["mage"]["name"]
                player.hp += playable["mage"]["hp"]
                player.damage_1 += playable["mage"]["damage_1"]
                player.damage_2 += playable["mage"]["damage_2"]
                player.potions += playable["mage"]["potions"]
                break
            if user == "2" or user.lower() == "warrior":
                player.name = playable["warrior"]["name"]
                player.hp += playable["warrior"]["hp"]
                player.damage_1 += playable["warrior"]["damage_1"]
                player.damage_2 += playable["warrior"]["damage_2"]
                player.potions += playable["warrior"]["potions"]
                break
            if user == "3" or user.lower() == "thief":
                player.name = playable["thief"]["name"]
                player.hp += playable["thief"]["hp"]
                player.damage_1 += playable["thief"]["damage_1"]
                player.damage_2 += playable["thief"]["damage_2"]
                player.potions += playable["thief"]["potions"]
                break
            # Simple message printed if no character selected:
            print("\nUnknown/Invalid Character Selection...")
            # A print message displays the character info/stats for user's character after selection:
        Player.player_select_msg(player)

    while True:
        """
        User now selects an enemy/Monster to fight;
        - User and monster engage in turn-based battle;
        - battle ends when either user/monster HP reduced to 0 or below;
        - If user defeated: message displayed and user can quit game or play again;
        - If monster defeated: user character awarded stats boost and user prompted to select the next monster they want to battle;
        -- monster name added to 'completed_quests' list;
        -- completed_quests is checked each time to determine whether user battled given enemy in current game-session;
        -- user Wins when completed_quests contains the names of all monsters...
        - If user defeats all monsters in current game-session - Game is Won! - message displayed that user won and prompted to quit game or play again...
        """
        # Check to see if enemy in 'completed_quests'
        game_fin = check_list(completed_quests)
        if game_fin == True:
            Player.game_won_msg(player)
            break
        elif player.hp <= 0:
            Player.game_over_msg(player)
            break
        else:
            select_quest = Player.quest_select(player)
            if select_quest == "1" or select_quest.lower() == "goblin":
                check = Enemy.check_if_defeated(goblin, completed_quests)
                if check == True:
                    Player.already_defeated_msg(player, goblin)
                    continue
                elif check == False:
                    completed_quests.append("goblin")
                    """ 
                    User Battles the Goblin: 
                    """
                    while True:
                        # Display enemy stats/info:
                        Enemy.monster_stats_msg(goblin)
                        # Message displayed each time it is User's turn in battle:
                        Player.player_turn_msg(player)
                        # User selects action to perform this turn:
                        player_turn = Player.user_turn(player)
                        player_roll = GameCharacter.roll(player)
                        if player_turn == "1" or player_turn.lower() == "basic":
                            # User has selected basic attack:
                            Player.basic_attack_msg(player)
                            if player_roll > 3 and player_roll < 18:
                                # Decrease Monster's HP by player damage_1
                                goblin.hp = GameCharacter.successful_attack(
                                    goblin, player.damage_1
                                )
                                Player.player_basic_attack_msg(
                                    player, player_roll, goblin
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "2" or player_turn.lower() == "strong":
                            # User has selected Strong attack:
                            Player.strong_attack_msg(player)
                            if player_roll >= 5 and player_roll < 10:
                                # decrease Monster's HP by player damage_2
                                goblin.hp = GameCharacter.successful_attack(
                                    goblin, player.damage_2
                                )
                                Player.player_strong_attack_msg(
                                    player, player_roll, goblin
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "3" or player_turn.lower() == "potion":
                            # User opts to use a health potion:
                            if player.potions > 0:
                                # user has health potion remaining
                                player.potions -= 1
                                player.hp += 20
                                Player.health_potion_msg(player)
                            if player.potions <= 0:
                                Player.no_potion_msg(player)
                        """ 
                        Check monster's HP before moving to Monster's turn; 
                        -- if monster HP <=0, user wins and is awarded stats boost;
                        -- else, monster's turn. 
                        """
                        if goblin.hp <= 0:
                            # Monster's HP <= 0 during player's turn:
                            Player.monster_defeated_msg(player, goblin)
                            # User's character awarded boost to stats
                            player.hp = Player.hp_boost(player)
                            player.damage_1 = Player.basic_boost(player)
                            player.damage_2 = Player.strong_boost(player)
                            # Display user's current stats:
                            Player.stats_boost_msg(player)
                            break
                        # If monster HP > 0; Monster attacks player:
                        # monster_roll determines whether attack successful:
                        monster_roll = GameCharacter.roll(goblin)

                        if goblin.hp > goblin.choice:
                            # monster's health at greater than 50%; monster uses basic attack:
                            if monster_roll >= 4 and monster_roll < 18:
                                # Monster lands successful basic attack:
                                # User's HP reduced by attack damage:
                                player_hp = GameCharacter.successful_attack(
                                    player, goblin.damage_1
                                )
                                Enemy.monster_basic_attack_msg(goblin, player)
                            elif monster_roll < 4 or monster_roll >= 18:
                                # Monster's attack misses:
                                GameCharacter.failed_attack_msg(goblin)

                        if goblin.hp <= goblin.choice:
                            # Monster's total HP at 50% or less; strong attack possible:
                            """
                            Note: Fuck!!! I think I did this wrong (or not as efficient as it could be) - need to make a 'battle' class and then 'player turn class/monster turn class' - would make all this code easier...but such is life, already here...maybe finish then try again.
                            """
                            attack = Enemy.attack_choice(goblin)
                            if attack == "basic":
                                if monster_roll >= 4 and monster_roll < 18:
                                    # Monster lands successful basic attack:
                                    # User's HP reduced by attack damage:
                                    player_hp = GameCharacter.successful_attack(
                                        player, goblin.damage_1
                                    )
                                    Enemy.monster_basic_attack_msg(goblin, player)
                                elif monster_roll < 4 or monster_roll >= 18:
                                    # Monster's attack misses:
                                    GameCharacter.failed_attack_msg(goblin)
                            if attack == "strong":
                                if monster_roll >= 5 and monster_roll < 10:
                                    # Monster lands successful strong attack:
                                    player.hp = GameCharacter.successful_attack(
                                        player, goblin.damage_2
                                    )
                                    Enemy.monster_strong_attack_msg(goblin, player)
                                elif monster_roll < 5 or monster_roll >= 10:
                                    GameCharacter.failed_attack_msg(goblin)

                        # Check to see if User's HP <= 0:
                        if player.hp <= 0:
                            Player.player_defeated_msg(player, goblin)
                            break

            if select_quest == "2" or select_quest.lower() == "ogre":
                check = Enemy.check_if_defeated(ogre, completed_quests)
                if check == True:
                    Player.already_defeated_msg(player, ogre)
                    continue
                elif check == False:
                    completed_quests.append("ogre")
                    """ 
                    User Battles the Ogre 
                    """
                    while True:
                        # Display enemy stats/info:
                        Enemy.monster_stats_msg(ogre)
                        # Message displayed each time it is User's turn in battle:
                        Player.player_turn_msg(player)
                        # User selects action to perform this turn:
                        player_turn = Player.user_turn(player)
                        player_roll = GameCharacter.roll(player)
                        if player_turn == "1" or player_turn.lower() == "basic":
                            # User has selected basic attack:
                            Player.basic_attack_msg(player)
                            if player_roll > 3 and player_roll < 18:
                                # Decrease Monster's HP by player damage_1
                                ogre.hp = GameCharacter.successful_attack(
                                    ogre, player.damage_1
                                )
                                Player.player_basic_attack_msg(
                                    player, player_roll, ogre
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "2" or player_turn.lower() == "strong":
                            # User has selected Strong attack:
                            Player.strong_attack_msg(player)
                            if player_roll >= 5 and player_roll < 10:
                                # decrease Monster's HP by player damage_2
                                ogre.hp = GameCharacter.successful_attack(
                                    ogre, player.damage_2
                                )
                                Player.player_strong_attack_msg(
                                    player, player_roll, ogre
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "3" or player_turn.lower() == "potion":
                            # User opts to use a health potion:
                            if player.potions > 0:
                                # user has health potion remaining
                                player.potions -= 1
                                player.hp += 20
                                Player.health_potion_msg(player)
                            if player.potions <= 0:
                                Player.no_potion_msg(player)
                        """ 
                        Check monster's HP before moving to Monster's turn; 
                        -- if monster HP <=0, user wins and is awarded stats boost;
                        -- else, monster's turn. 
                        """
                        if ogre.hp <= 0:
                            # Monster's HP <= 0 during player's turn:
                            Player.monster_defeated_msg(player, ogre)
                            # User's character awarded boost to stats
                            player.hp = Player.hp_boost(player)
                            player.damage_1 = Player.basic_boost(player)
                            player.damage_2 = Player.strong_boost(player)
                            # Display user's current stats:
                            Player.stats_boost_msg(player)
                            break
                        # If monster HP > 0; Monster attacks player:
                        # monster_roll determines whether attack successful:
                        monster_roll = GameCharacter.roll(ogre)

                        if ogre.hp > ogre.choice:
                            # monster's health at greater than 50%; monster uses basic attack:
                            if monster_roll >= 4 and monster_roll < 18:
                                # Monster lands successful basic attack:
                                # User's HP reduced by attack damage:
                                player_hp = GameCharacter.successful_attack(
                                    player, ogre.damage_1
                                )
                                Enemy.monster_basic_attack_msg(ogre, player)
                            elif monster_roll < 4 or monster_roll >= 18:
                                # Monster's attack misses:
                                GameCharacter.failed_attack_msg(ogre)

                        if ogre.hp <= ogre.choice:
                            # Monster's total HP at 50% or less; strong attack possible:

                            attack = Enemy.attack_choice(ogre)
                            if attack == "basic":
                                if monster_roll >= 4 and monster_roll < 18:
                                    # Monster lands successful basic attack:
                                    # User's HP reduced by attack damage:
                                    player_hp = GameCharacter.successful_attack(
                                        player, ogre.damage_1
                                    )
                                    Enemy.monster_basic_attack_msg(ogre, player)
                                elif monster_roll < 4 or monster_roll >= 18:
                                    # Monster's attack misses:
                                    GameCharacter.failed_attack_msg(ogre)
                            if attack == "strong":
                                if monster_roll >= 5 and monster_roll < 10:
                                    # Monster lands successful strong attack:
                                    player.hp = GameCharacter.successful_attack(
                                        player, ogre.damage_2
                                    )
                                    Enemy.monster_strong_attack_msg(ogre, player)
                                elif monster_roll < 5 or monster_roll >= 10:
                                    GameCharacter.failed_attack_msg(ogre)

                        # Check to see if User's HP <= 0:
                        if player.hp <= 0:
                            Player.player_defeated_msg(player, ogre)
                            break

            if select_quest == "3" or select_quest.lower() == "orc":
                check = Enemy.check_if_defeated(orc, completed_quests)
                if check == True:
                    Player.already_defeated_msg(player, orc)
                    continue
                elif check == False:
                    completed_quests.append("orc")
                    """ 
                    User Battles the Orc
                    """
                    while True:
                        # Display enemy stats/info:
                        Enemy.monster_stats_msg(orc)
                        # Message displayed each time it is User's turn in battle:
                        Player.player_turn_msg(player)
                        # User selects action to perform this turn:
                        player_turn = Player.user_turn(player)
                        player_roll = GameCharacter.roll(player)
                        if player_turn == "1" or player_turn.lower() == "basic":
                            # User has selected basic attack:
                            Player.basic_attack_msg(player)
                            if player_roll > 3 and player_roll < 18:
                                # Decrease Monster's HP by player damage_1
                                orc.hp = GameCharacter.successful_attack(
                                    orc, player.damage_1
                                )
                                Player.player_basic_attack_msg(player, player_roll, orc)
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "2" or player_turn.lower() == "strong":
                            # User has selected Strong attack:
                            Player.strong_attack_msg(player)
                            if player_roll >= 5 and player_roll < 10:
                                # decrease Monster's HP by player damage_2
                                orc.hp = GameCharacter.successful_attack(
                                    orc, player.damage_2
                                )
                                Player.player_strong_attack_msg(
                                    player, player_roll, orc
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "3" or player_turn.lower() == "potion":
                            # User opts to use a health potion:
                            if player.potions > 0:
                                # user has health potion remaining
                                player.potions -= 1
                                player.hp += 20
                                Player.health_potion_msg(player)
                            if player.potions <= 0:
                                Player.no_potion_msg(player)
                        """ 
                        Check monster's HP before moving to Monster's turn; 
                        -- if monster HP <=0, user wins and is awarded stats boost;
                        -- else, monster's turn. 
                        """
                        if orc.hp <= 0:
                            # Monster's HP <= 0 during player's turn:
                            Player.monster_defeated_msg(player, orc)
                            # User's character awarded boost to stats
                            player.hp = Player.hp_boost(player)
                            player.damage_1 = Player.basic_boost(player)
                            player.damage_2 = Player.strong_boost(player)
                            # Display user's current stats:
                            Player.stats_boost_msg(player)
                            break
                        # If monster HP > 0; Monster attacks player:
                        # monster_roll determines whether attack successful:
                        monster_roll = GameCharacter.roll(orc)

                        if orc.hp > orc.choice:
                            # monster's health at greater than 50%; monster uses basic attack:
                            if monster_roll >= 4 and monster_roll < 18:
                                # Monster lands successful basic attack:
                                # User's HP reduced by attack damage:
                                player_hp = GameCharacter.successful_attack(
                                    player, orc.damage_1
                                )
                                Enemy.monster_basic_attack_msg(orc, player)
                            elif monster_roll < 4 or monster_roll >= 18:
                                # Monster's attack misses:
                                GameCharacter.failed_attack_msg(orc)

                        if orc.hp <= orc.choice:
                            # Monster's total HP at 50% or less; strong attack possible:

                            attack = Enemy.attack_choice(orc)
                            if attack == "basic":
                                if monster_roll >= 4 and monster_roll < 18:
                                    # Monster lands successful basic attack:
                                    # User's HP reduced by attack damage:
                                    player_hp = GameCharacter.successful_attack(
                                        player, orc.damage_1
                                    )
                                    Enemy.monster_basic_attack_msg(orc, player)
                                elif monster_roll < 4 or monster_roll >= 18:
                                    # Monster's attack misses:
                                    GameCharacter.failed_attack_msg(orc)
                            if attack == "strong":
                                if monster_roll >= 5 and monster_roll < 10:
                                    # Monster lands successful strong attack:
                                    player.hp = GameCharacter.successful_attack(
                                        player, orc.damage_2
                                    )
                                    Enemy.monster_strong_attack_msg(orc, player)
                                elif monster_roll < 5 or monster_roll >= 10:
                                    GameCharacter.failed_attack_msg(orc)

                        # Check to see if User's HP <= 0:
                        if player.hp <= 0:
                            Player.player_defeated_msg(player, orc)
                            break

            if select_quest == "4" or select_quest.lower() == "dragon":
                check = Enemy.check_if_defeated(dragon, completed_quests)
                if check == True:
                    Player.already_defeated_msg(player, dragon)
                    continue
                elif check == False:
                    completed_quests.append("dragon")
                    """ 
                    User Battles the Dragon
                    """
                    while True:
                        # Display enemy stats/info:
                        Enemy.monster_stats_msg(dragon)
                        # Message displayed each time it is User's turn in battle:
                        Player.player_turn_msg(player)
                        # User selects action to perform this turn:
                        player_turn = Player.user_turn(player)
                        player_roll = GameCharacter.roll(player)
                        if player_turn == "1" or player_turn.lower() == "basic":
                            # User has selected basic attack:
                            Player.basic_attack_msg(player)
                            if player_roll > 3 and player_roll < 18:
                                # Decrease Monster's HP by player damage_1
                                dragon.hp = GameCharacter.successful_attack(
                                    dragon, player.damage_1
                                )
                                Player.player_basic_attack_msg(
                                    player, player_roll, dragon
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "2" or player_turn.lower() == "strong":
                            # User has selected Strong attack:
                            Player.strong_attack_msg(player)
                            if player_roll >= 5 and player_roll < 10:
                                # decrease Monster's HP by player damage_2
                                dragon.hp = GameCharacter.successful_attack(
                                    dragon, player.damage_2
                                )
                                Player.player_strong_attack_msg(
                                    player, player_roll, dragon
                                )
                            else:
                                # User does not land attack
                                GameCharacter.failed_attack_msg(player)
                        if player_turn == "3" or player_turn.lower() == "potion":
                            # User opts to use a health potion:
                            if player.potions > 0:
                                # user has health potion remaining
                                player.potions -= 1
                                player.hp += 20
                                Player.health_potion_msg(player)
                            if player.potions <= 0:
                                Player.no_potion_msg(player)
                        """ 
                        Check monster's HP before moving to Monster's turn; 
                        -- if monster HP <=0, user wins and is awarded stats boost;
                        -- else, monster's turn. 
                        """
                        if dragon.hp <= 0:
                            # Monster's HP <= 0 during player's turn:
                            Player.monster_defeated_msg(player, dragon)
                            # User's character awarded boost to stats
                            player.hp = Player.hp_boost(player)
                            player.damage_1 = Player.basic_boost(player)
                            player.damage_2 = Player.strong_boost(player)
                            # Display user's current stats:
                            Player.stats_boost_msg(player)
                            break
                        # If monster HP > 0; Monster attacks player:
                        # monster_roll determines whether attack successful:
                        monster_roll = GameCharacter.roll(dragon)

                        if dragon.hp > dragon.choice:
                            # monster's health at greater than 50%; monster uses basic attack:
                            if monster_roll >= 4 and monster_roll < 18:
                                # Monster lands successful basic attack:
                                # User's HP reduced by attack damage:
                                player_hp = GameCharacter.successful_attack(
                                    player, dragon.damage_1
                                )
                                Enemy.monster_basic_attack_msg(dragon, player)
                            elif monster_roll < 4 or monster_roll >= 18:
                                # Monster's attack misses:
                                GameCharacter.failed_attack_msg(dragon)

                        if dragon.hp <= dragon.choice:
                            # Monster's total HP at 50% or less; strong attack possible:

                            attack = Enemy.attack_choice(dragon)
                            if attack == "basic":
                                if monster_roll >= 4 and monster_roll < 18:
                                    # Monster lands successful basic attack:
                                    # User's HP reduced by attack damage:
                                    player_hp = GameCharacter.successful_attack(
                                        player, dragon.damage_1
                                    )
                                    Enemy.monster_basic_attack_msg(dragon, player)
                                elif monster_roll < 4 or monster_roll >= 18:
                                    # Monster's attack misses:
                                    GameCharacter.failed_attack_msg(dragon)
                            if attack == "strong":
                                if monster_roll >= 5 and monster_roll < 10:
                                    # Monster lands successful strong attack:
                                    player.hp = GameCharacter.successful_attack(
                                        player, dragon.damage_2
                                    )
                                    Enemy.monster_strong_attack_msg(dragon, player)
                                elif monster_roll < 5 or monster_roll >= 10:
                                    GameCharacter.failed_attack_msg(dragon)

                        # Check to see if User's HP <= 0:
                        if player.hp <= 0:
                            Player.player_defeated_msg(player, dragon)
                            break
