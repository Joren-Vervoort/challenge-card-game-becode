from utils.player import Player


List_of_players = []
Amount_of_players = int(input("Please enter the amount of players: ")) 
Player_input = str(input("Please enter your first player name: "))
List_of_players.append(Player_input)

while len(List_of_players) != Amount_of_players:
    Player_input = str(input("Please enter the next player name: "))
    List_of_players.append(Player_input) 

#Creating the players

print(List_of_players)

#Connecting the players to the class Player(self.name)

for i in List_of_players:
    (Player(List_of_players[i]))
    print(i)







