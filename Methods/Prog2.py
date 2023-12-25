class Player:
    teamName= "India"
    def __init__(self):
    
        print("In Cons")
        self.jerNo=7
        self.pName="MSD"
        print(id(self),"Id of Self")
        print(self)
    @classmethod
    def playerInfo(cls):
        #print(cls.jerNo)
        #print(cls.pName)
        print(cls.teamName)
        print(id(cls),"Id of Cls")
        print(cls,"onlycls")
play1=Player()
play1.playerInfo()
print(id(play1))
print(Player,"Only player")
print(id(Player))
