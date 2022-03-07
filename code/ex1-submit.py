import matplotlib
import numpy as np
import matplotlib.pyplot as plt


numberOfNodes = 0
isLineOne = True
listOfLines = []
frequencyDict = dict()

# ***************
n_nodes = 1
dxDict = {
    1: 3.0/72,
    10: 8.0/72,
    100: 16.0/72,
    1000: 8.0/72,
    10000: 4.0/72

}


f_name = "s{}.txt".format(n_nodes)
graphName = "graphs/s{}_histogram_directed.png".format(n_nodes)
# ****************

f = open(f_name, 'r')
for line in f:
    if isLineOne:
        numberOfNodes = int(line.strip())
        for i in range(numberOfNodes):
            frequencyDict[i] = []
    else:
        listTemp = line.strip().split(' ')
        v1 = listTemp[0]
        v2 = listTemp[1]
        listOfLines.append(v1 + '-' + v2) # toggle for undirected or directed in
        listOfLines.append(v2 + '-' + v1) # toggle for undirected or directed out 
    isLineOne = False
f.close()
listOfLines = sorted(listOfLines)
for i in range(len(listOfLines)-1, 0, -1):
    if listOfLines[i] == listOfLines[i-1]:
        listOfLines.pop(i-1)

for item in listOfLines:
    temp = item.split('-')
    key = int(temp[0])
    val = int(temp[1])
    frequencyDict[key].append(val)




degreeToNodes = dict()
for i in range(numberOfNodes):
    degreeToNodes[i] = []

for (k,v) in frequencyDict.items():
    keyNew = len(v)
    valNew = k
    degreeToNodes[keyNew].append(valNew)


actualDegreeToNodes = dict()
for (a, b) in degreeToNodes.items():
    actualDegreeToNodes[a] = len(b)


degreeNumber = list(actualDegreeToNodes.keys())
numberOfNodesWithDegree = list(actualDegreeToNodes.values())
fig, ax = plt.subplots(figsize = (10, 5))

nullList = []
for i in range(numberOfNodes):
    if len(frequencyDict[i]) == 0:
        nullList.append(i)
        frequencyDict.pop(i)

frequencyDictInitial = frequencyDict

regionsList = []
while len(frequencyDict) > 0:

    k,v = list(frequencyDict.items())[0]
    tempList = [k] + v
    tempSet = set(tempList)
    
    colonySet = set()
    colonySet.update(tempList)
    frequencyDict.pop(k)

    for i in range(numberOfNodes):
        for k,v in frequencyDict.items():
            tempList = [k] + v
            tempSet = set(tempList)
            z = colonySet.intersection(tempSet)

            if len(z) > 0:
                colonySet.update(tempSet)
                frequencyDict.pop(k)



    if len(colonySet) > 0:
        regionsList.append(colonySet)


print(len(regionsList) + len(nullList))
