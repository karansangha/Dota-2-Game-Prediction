from sklearn import tree

# Open the file and read in data from that.
training_data_file = open("trainingdata.txt")
theList = []
for entry in training_data_file:
    entry = entry.strip()
    theList.append(entry)
training_data_file.close()

# Initialize a dictionary
db = dict()

# Iterate through each line in theList
i = 0
count = 0

# Each champion is assigned a unique id
while i < len(theList):
    if '1' in theList[i]:  # If team 1 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 0
        while j < 5:
            if champions[j] not in db:
                db[champions[j]] = count
                count += 1
            j += 1

    else:  # If team 2 wins
        champions = theList[i].split(',')
        champions.pop()
        j = 5
        while j < 10:
            if champions[j] not in db:
                db[champions[j]] = count
                count += 1
            j += 1
    i += 1

i = 0
dataChampions = []
dataWinners = []

while i < len(theList):
    data = []
    champions = theList[i].split(',')
    winner = champions.pop()
    dataWinners.append(winner)
    j = 0
    while j < len(champions):
        data.append(db[champions[j]])
        j += 1
    dataChampions.append(data)
    i += 1

# Import the classifier

my_classifier = tree.DecisionTreeClassifier()

# Train the classifier
my_classifier.fit(dataChampions, dataWinners)

# Test the algorithm
inp = int(input())
k = 0
inputList = []
while k < inp:
    line = input()
    inputList.append(line)
    k += 1

j = 0
testChampions = []

while j < len(inputList):
    stringChampions = inputList[j].split(',')
    intChampions = []
    z = 0
    while z < 10:
        intChampions.append(db[stringChampions[z]])
        z += 1
    testChampions.append(intChampions)
    j += 1

predictions = my_classifier.predict(testChampions)

# Print the results
for prediction in predictions:
    print(prediction)
