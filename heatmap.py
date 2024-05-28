import csv
import matplotlib.pyplot as plt
import numpy as np
from  matplotlib.colors import LinearSegmentedColormap

mensData = []
with open('mens2024_census.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        mensData.append(''.join(row).split(','))

mensData.pop(0)
mensXPoints = []
mensYPoints = []


for d in mensData:
    mensXPoints.append(int(d[1]))
    mensYPoints.append(int(d[2]))


minX = 0
minY = -5
maxX = 50
maxY = 45
mensHeatmap1 = [[[0,0] for i in range(51)] for k in range(51)]


for i in range(len(mensXPoints)):
    xCor = mensXPoints[i] - minX
    yCor = mensYPoints[i] - minY
    if (xCor > 50 or yCor > 50):
        continue
    if (mensData[i][0] == 'True'):
        mensHeatmap1[xCor][yCor][0] = mensHeatmap1[xCor][yCor][0] + 1 #int(mensData[i][3])
        mensHeatmap1[xCor][yCor][1] = mensHeatmap1[xCor][yCor][1] + 1
    else:
        mensHeatmap1[xCor][yCor][1] = mensHeatmap1[xCor][yCor][1] + 1




womensData = []
with open('womens2024_census.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        womensData.append(''.join(row).split(','))

womensData.pop(0)
womensXPoints = []
womensYPoints = []


for d in womensData:
    womensXPoints.append(int(d[1]))
    womensYPoints.append(int(d[2]))


minX = 0
minY = -5
maxX = 50
maxY = 45
womensHeatmap1 = [[[0,0] for i in range(51)] for k in range(51)]


for i in range(len(womensXPoints)):
    xCor = womensXPoints[i] - minX
    yCor = womensYPoints[i] - minY
    if (xCor > 50 or yCor > 50):
        continue
    if (womensData[i][0] == 'True'):
        womensHeatmap1[xCor][yCor][0] = womensHeatmap1[xCor][yCor][0] + 1 #int(womensData[i][3])
        womensHeatmap1[xCor][yCor][1] = womensHeatmap1[xCor][yCor][1] + 1
    else:
        womensHeatmap1[xCor][yCor][1] = womensHeatmap1[xCor][yCor][1] + 1


heatmap2 = [[0 for i in range(51)] for k in range(51)]
maxVal = 0
minVal = 0
for x in range (len(heatmap2)):
    for y in range(len(heatmap2[0])):
        
        if (mensHeatmap1[x][y][1] > 1 and womensHeatmap1[x][y][1] > 1):
            
            heatmap2[x][y] = (mensHeatmap1[x][y][0]/(len(mensXPoints)))

            if (heatmap2[x][y] > maxVal):
                maxVal = heatmap2[x][y]
            if (heatmap2[x][y] < minVal):
                minVal = heatmap2[x][y]

x, y = np.mgrid[slice(0, 51, 1),
                slice(minY, minY + 51, 1)]
# LinearSegmentedColormap.from_list('rg',["g", "w", "r"], N=256) cmap for comparisons
c = plt.pcolormesh(x, y, heatmap2, cmap = "hot", vmin = -max([abs(minVal), maxVal]), vmax = max([abs(minVal), maxVal]), shading="gouraud")
plt.colorbar(c)
plt.xticks(np.arange(0, 51, step = 5))
plt.yticks(np.arange(-5, 46, step = 5))
plt.plot(25,0, "go")
plt.plot(np.array([24,26,26,24,24]), np.array([0,0,2,2,0]))
plt.xlabel("x location(ft)")
plt.ylabel("y location(ft)")
plt.title("title")
plt.savefig("graphs/name.png")

mSum = 0
wSum = 0
for x in range(24,27):
    for y in range(5,8):
        mSum += mensHeatmap1[x][y][1]
        wSum += womensHeatmap1[x][y][1]

print(mSum, len(mensXPoints))
print(wSum, len(womensXPoints))

