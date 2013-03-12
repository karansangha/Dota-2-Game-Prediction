# Open the file and read in data from that.
liopen = open("trainingdata.txt")
theList = []
for entry in liopen:
    entry = entry.strip()
    theList.append(entry)
liopen.close()

# Initialize a dictionary 
db= dict()

i = 0
##print len(theList)

#Iterate through each line in theList
while (i<len(theList)):
    if '1' in theList[i]: #If team 1 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 0
        while (j<5):
            if champions[j] in db:
               db[champions[j]]+=1
            else:
                db[champions[j]] = 1
            j+=1
    else: #If team 2 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 5
        while (j<10):
            if champions[j] in db:
               db[champions[j]]+=1
            else:
                db[champions[j]] = 1
            j+=1
    i+=1

##### DATABASE CREATION COMPLETED ####

#### BEGIN TESTING THE ALGORITHM ####
        
inp = int(raw_input())
k = 0
inputList = []
while (k<inp):
    line = raw_input()
    inputList.append(line)
    k+=1

team1Score = 0
team2Score = 0

j = 0
while (j<len(inputList)):
    teamChampions = inputList[j].split(',')
    z = 0
    while (z<5):
        team1Score+=db[teamChampions[z]]
        z+=1
    z = 5
    while (z<10):
        team2Score+=db[teamChampions[z]]
        z+=1    
    if (team1Score>team2Score):
        print "1"
    else:
        print "2"
    team1score = 0
    team2score = 0
    j+=1

    


    
   
    
    
