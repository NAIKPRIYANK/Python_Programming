class Player():
    teamName="India"

    def __new__(cls):
        print("Memory Allocator")
        return super().__new__(cls)
    def __init__(self):
        print("In constructor")
        self.pName="MSD"
        self.JerNo=7

    def playerInfo(self):
        print("Player Info:")
        print(self.pName)
        print(self.JerNo)
        print(Player.teamName)

obj1=Player()
obj1.playerInfo()

