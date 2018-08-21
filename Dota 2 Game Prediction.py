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
for item in theList:
    if '1' in item:
        champions = item.split(',')
        champions.pop()
        for j in range(5):
            if champions[j] not in db:
                db[champions[j]] = count
                count += 1

    else:
        champions = item.split(',')
        champions.pop()
        j = 5
        for j in range(5, 10):
            if champions[j] not in db:
                db[champions[j]] = count
                count += 1

dataChampions = []
dataWinners = []

for item in theList:
    data = []
    champions = item.split(',')
    winner = champions.pop()
    dataWinners.append(winner)
    j = 0
    for j in range(len(champions)):
        data.append(db[champions[j]])
        j += 1
    dataChampions.append(data)

# Import the classifier
my_classifier = tree.DecisionTreeClassifier()

# Train the classifier
my_classifier.fit(dataChampions, dataWinners)

# Test the algorithm
inp = int(input())
inputList = []

for k in range(inp):
    line = input()
    inputList.append(line)

testChampions = []

for item in inputList:
    stringChampions = item.split(',')
    intChampions = []
    for z in range(10):
        intChampions.append(db[stringChampions[z]])
    testChampions.append(intChampions)

predictions = my_classifier.predict(testChampions)

# Print the results
for prediction in predictions:
    print(prediction)
