import requests
import matplotlib.pyplot as plt
import csv

gameIDs = []

# Men's IDs

# gameIDs.append(401638645) 2024
# gameIDs.append(401522202) 2023
# gameIDs.append(401408636) 2022
# gameIDs.append(401310865) 2021
# gameIDs.append(401123374) 2020
# gameIDs.append(401025888) 2019
# gameIDs.append(400949246) 2018
# gameIDs.append(400873651) 2017
# gameIDs.append(400788981) 2016
# gameIDs.append(400551234) 2015

# Women's IDs

# gameIDs.append(401637613) 2024
# gameIDs.append(401528028) 2023
# gameIDs.append(401414529) 2022



data = []

totalGames = 0
for sId in gameIDs:
    games = 0
    gs = 0
    while (games < 67 and gs < 200):
        id = sId - gs
        gs += 1
        g = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/summary?event=" + str(id))
        
        text = g.content.decode('UTF-8')

        if (len(text) < 1000):
            continue
        
        si = text.find('"plays":') + 9
        game = text[si:]
        ei = game.find('End Game')
        game = game[:ei]
    

        level = 0
        plays = []
        index = 0
        for i in range(len(game)):
            if (game[i] == '{'):
                level += 1
            elif (game[i] == '}'):
                level -= 1
                if (level == 0):
                    plays.append(game[index:i])
                    index = i + 2

        
        bd = len(data)
        for p in plays:
            if ('"x":' not in game):
                    continue
            if ('"shootingPlay":true' in p and "Free Throw" not in p):
                m1 = p[p.find('"scoringPlay":') + 14:p.find('"scoreValue":') - 1]
                
                if (m1 == 'true'):
                    m = True
                else:
                    m = False
                x = int(p[p.find('"x":') + 4:p.find('"y":')-1])
                y = int(p[p.find('"y":') + 4:len(p)-1])
                val = int(p[p.find('"scoreValue":') + 13:p.find('"scoreValue":')+14])
                if (abs(x) < 60 and abs(y) < 150):
                    data.append([m,x,y, val])
        if (len(data) > bd):
            games += 1
    totalGames += games

with open("filename.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
    
        writer.writerow(["made", 'x', 'y', 'val'])
    
        # writing data rows
        for r in data:
            writer.writerow(r)

xPoints = []
yPoints = []
color = []

print(totalGames)