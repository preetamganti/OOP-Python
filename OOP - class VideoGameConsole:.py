class VideoGameConsole:
    def __init__(self, console_name):
        self.console_name = console_name
        self.game = None

    def set_game(self, game):
        self.game = game

    def get_console_details(self):
        return f"Console Name: {self.console_name}\nGame: {self.game}"


class PS5(VideoGameConsole):
    def __init__(self):
        super().__init__("PS5")


class NintendoSwitch(VideoGameConsole):
    def __init__(self):
        super().__init__("Nintendo Switch")


class XboxSeriesS(VideoGameConsole):
    def __init__(self):
        super().__init__("Xbox Series S")


# Example usage:
console1 = PS5()
console1.set_game("Hogwarts Legacy")
print(console1.get_console_details())

console2 = NintendoSwitch()
console2.set_game("Pokemon Sword and Shield")
print(console2.get_console_details())

console3 = XboxSeriesS()
console3.set_game("GTA V")
print(console3.get_console_details())


#My base class for this code is 'VideoGameConsole' with an attribute called 'console_name' and an additional game attribute called 'game'. 
#The classes 'PS5', 'NintendoSwitch', and 'XboxSeriesS' add specific console names.
#Each of the three consoles has a 'set_game()' method to set the game that is associated with each console, and 'get_console_details()' method is used to display the console details and the game.
#I created three classes and usedthe set_game() method to set the each game to its console.
#Last, I called on get_console_details() method to display the console details, and the associated game as well to look like this:

#Console Name: PS5
#Game: Hogwarts Legacy
#Console Name: Nintendo Switch
#Game: Pokemon Sword and Shield
#Console Name: Xbox Series S
#Game: GTA V
