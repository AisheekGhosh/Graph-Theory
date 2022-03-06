import matplotlib
import numpy as np
import matplotlib.pyplot as plt


numberOfNodes = 0
isLineOne = True
listOfLines = []
frequencyDict = dict()

# ***************
n_nodes = 10000
dxDict = {
    1: 3.0/72,
    10: 8.0/72,
    100: 16.0/72,
    1000: 8.0/72,
    10000: 4.0/72

}


f_name = "n{}.txt".format(n_nodes)
graphName = "graphs/n{}_histogram_directed_out.png".format(n_nodes)
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

print(frequencyDict)
for (k,v) in frequencyDict.items():
    print(k,len(v))
    keyNew = len(v)
    valNew = k
    degreeToNodes[keyNew].append(valNew)

print(degreeToNodes)
for (a, b) in degreeToNodes.items():
    print(a, len(b))

actualDegreeToNodes = dict()
for (a, b) in degreeToNodes.items():
    actualDegreeToNodes[a] = len(b)

print(actualDegreeToNodes)

degreeNumber = list(actualDegreeToNodes.keys())
numberOfNodesWithDegree = list(actualDegreeToNodes.values())
fig, ax = plt.subplots(figsize = (10, 5))

plt.bar(degreeNumber, numberOfNodesWithDegree, color ='green', width = 0.35)
plt.xlabel('Degrees')
plt.ylabel('Number of Nodes')
plt.title('Degrees vs Number of Nodes')
plt.bar(degreeNumber, numberOfNodesWithDegree, width = 0.35, label='Degree Numbers')

# plt.xticks(np.arange(min(degreeNumber), max(degreeNumber)+1, 1))
# Uncomment above and below for n_nodes = 10
# plt.yticks(np.arange(min(numberOfNodesWithDegree), max(numberOfNodesWithDegree)+1, 1))

dx = dxDict[n_nodes]; dy = 0/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)



for label in ax.xaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)
plt.savefig(graphName)


f.close()

print(sum(actualDegreeToNodes.values()))