import json
import math
import sys

def writeToJSONFile(data, filename):
    f = open(filename + '.json', 'w')
    json.dump(data, f)


try:
    open("data.json")
except:
    input("Failed to load data.json! Make sure its in the same directory as casino.py")
else:
    data = open("data.json")
    data = json.load(data)
    listData = data
    data = data[0]
    if not data['credits']:
        data['credits'] = 10
        listData[0]['credits'] = 10
    credits = data['credits']
finally:
    print("Current credit balance: " + str(credits))
    doing = input("What would you like to do? (slot: x, claim, slot) ")
if doing.find("slot") != 1:
    creditsslot = doing[5:]
    credits = credits - int(creditsslot)
    listData[0]['credits'] = credits
    print("You now have " + str(credits) + " credits.")
    writeToJSONFile(listData, "data")
