from tkinter import *
from tkinter import messagebox
import json
import requests
import webbrowser
root = Tk()
CurrentStatus = StringVar()
CurrentStatus.set("Retrieving version.")
proVer = "1.0"


def writeToJSONFile(data, filename):
    f = open(filename + '.json', 'w')
    json.dump(data, f)


credits = 0
paydaycount = 0
ver = requests.get("https://pastebin.com/raw/qPMD0jUW")
ver = json.loads(ver.text)
print(ver[0]["CasinoVer"])
if ver[0]["CasinoVer"] != proVer:
    res = messagebox.askyesno("New version available!", "There is a new version available, would you like to go to the github page?")
    if res == True:
        CurrentStatus.set("Redirecting to github")
        webbrowser.open_new_tab("https://github.com/yeeter1/python-casino")

try:
    open("data.json")
except:
    messagebox.showwarning("Data not found!", "Unable to find data! Make sure 'data.json' is in the same directory.")
else:
    CurrentStatus.set("Grabbing data")
    data = open("data.json")
    data = json.load(data)
    listData = data
    data = data[0]
    if not data['Credits']:
        data['Credits'] = 10
        data['Payday'] = 0
        listData[0]["Credits"] = 10
        listData[0]["Payday"] = 0
    credits = data["Credits"]
    paydaycount = data['Payday']
finally:
    if paydaycount <= 0:
        CurrentStatus.set("Credits: " + str(credits) + ", ready for payday!")
    else:
        CurrentStatus.set("Credits: "+ str(credits) + ", payday in: "+ str(paydaycount) + " slots.")

def givePayday():
    CurrentStatus.set("Giving payday...")
    paydaycount = 5
    listData[0]["Payday"] = paydaycount
    credits = + 150
    listData[0]["Payday"] = credits
    CurrentStatus.set("Writing to json...")
    writeToJSONFile(listData, "data")
    CurrentStatus.set("Credits: "+ str(credits) + ", payday in: 5 slots.")


status = Label(root, textvariable=CurrentStatus, bd =1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Method", menu=subMenu)
subMenu.add_command(label="Payday", command=givePayday)
subMenu.add_separator()


root.resizable(width=False, height=False)
root.minsize(width=500,height=500)
root.maxsize(width=500, height=500)
root.mainloop()
