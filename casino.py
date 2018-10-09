import json
import math
import sys
import random
payday = True
import json

def writeToJSONFile(writing, filename):
    with open(filename + '.json', 'w') as output:
        json.dump(data,  output)

try:
    open("data.json")
except:
    input(".json data file not found! Aborting!")
    sys.exit(1)
else:
    data = open("data.json", "r")
    listData = data
    data = json.load(data)[0]
    if not data['credits']:
        data['credits'] = 10
    credits = data['credits']
finally:
    print("Your current credit balance is: " + str(credits))
    whattodo = input("What would you like to do? (slot: x, claim, shop) ")
if whattodo.find("slot") != -1:
    creditsslot = whattodo[5:]
    credits = credits - int(creditsslot)
    writeToJSONFile({"credits": credits}, "data")
    input("You now have " + str(credits) + " credits")
if whattodo.find("claim") != -1:
   if payday != True:
       print("Come back later for your payday.")
   else:
       credits = credits + 150
       payday = False
       print("You now have " + str(credits) + " credits.")
if whattodo.find("shop") != -1:
    print("Shop is currently WIP")