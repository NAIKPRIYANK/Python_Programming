PlayerList=["Rohit","Shubhaman","Virat","Iyyer","KLRahul"]

PlayerName=input("Enter player name: ")
for player in PlayerList:
    if player==PlayerName:
        print(PlayerName," is present in List")
        break
else:
    print(PlayerName," is present in List")

