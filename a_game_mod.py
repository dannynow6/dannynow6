""" 
Additional functions for adventure game: 
"""

def check_list(list) -> bool:
    """Checks to see if all enemies are in 'defeated' list (completed_quests). If so, player has won; if not, player still must battle enemies"""
    if "goblin" in list and "ogre" in list and "orc" in list and "dragon" in list:
        return True
    else:
        return False
