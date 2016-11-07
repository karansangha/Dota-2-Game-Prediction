# Open the file and read in data from that.
liopen = open("trainingdata.txt")
theList = []
for entry in liopen:
    entry = entry.strip()
    theList.append(entry)
liopen.close()

# Initialize a dictionary
db= dict()

#Iterate through each line in theList
i = 0
count = 0

"""
    Each champion is assigned a unique id
"""
while (i<len(theList)):
    if '1' in theList[i]: #If team 1 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 0
        while (j<5):
            if champions[j] not in db:
                db[champions[j]] = count
                count+=1
            j+=1

    else: #If team 2 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 5
        while (j<10):
            if champions[j] not in db:
                db[champions[j]] = count
                count+=1
            j+=1
    i+=1

# print db

i = 0
dataChampions = []
dataWinners = []
print theList[i].split(',')

while (i<len(theList)):
    data = []
    champions = theList[i].split(',')
    winner = champions.pop()
    dataWinners.append(winner)
    j=0
    while(j<len(champions)):
        data.append(db[champions[j]])
        j+=1
    dataChampions.append(data)
    i+=1

print dataChampions

#### BEGIN TESTING THE ALGORITHM ####

# inp = int(raw_input())
# k = 0
# inputList = []
# while (k<inp):
#     line = raw_input()
#     inputList.append(line)
#     k+=1
#
# team1Score = 0
# team2Score = 0
#
# j = 0
# while (j<len(inputList)):
#     teamChampions = inputList[j].split(',')
#     z = 0
#     while (z<5):
#         team1Score+=db[teamChampions[z]]
#         z+=1
#     z = 5
#     while (z<10):
#         team2Score+=db[teamChampions[z]]
#         z+=1
#     if (team1Score>team2Score):
#         print "1"
#     else:
#         print "2"
#     team1score = 0
#     team2score = 0
#     j+=1
