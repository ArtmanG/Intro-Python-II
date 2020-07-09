# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        
    def try_direction(self, command):
        attribute = command + '_to'

        # see if the current room has the attribute
        # we can use a Python function called 'hasattr'
        if hasattr(self.currentRoom, attribute):
            # use 'getattr' to actually move to the room
            self.currentRoom = getattr(self.currentRoom, attribute)
        else:
            print("You can't go that way!\n")