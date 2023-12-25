class Player:
    teamName="India"

    def __init__(self):
        self.jerseyNo=7
        self.pName="MSD"
    #Instance Method
    def playerInfo(self):
        print(self.jerseyNo)
        print(self.pName)
        print(self.teamName)
        print(id(self))
play1=Player()
play1.playerInfo()
print(id(play1))
