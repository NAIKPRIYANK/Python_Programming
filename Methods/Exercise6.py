class IPL:
    Country="India"
    Organizer="BCCI"

    def __init__(self):
        self.totalTeams=10
        self.Prize="50 cr"


    def IPL_info(self):
        print("IPL Short Intro:")
        print(IPL.Country)
        print(IPL.Organizer)
        print(self.totalTeams)
        print(self.Prize)

obj1=IPL()
obj1.IPL_info()

