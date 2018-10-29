from tkinter import *
from tkinter import messagebox
import json
import webbrowser
import math
import random
from PIL import Image, ImageTk
from os import path as checkpath

checkver = False
CL = "3 7's = 1000 Credits \n3 Ban Hammers = Credits get slotted credits * 5 added to them."
root = Tk()
size = 128, 128
root.title("Casino game")
CurrentStatus = StringVar()
CurrentStatus.set("Retrieving version.")
proVer = 1.4
notfound = []
images = ["peanut.png", "7.png", "banned.png", "donute.png"]
try:
    import requests
except:
    pass
else:
    checkver = True


def writeToJSONFile(data, filename):
    f = open(filename + '.json', 'w')
    json.dump(data, f)


if checkver:
    ver = requests.get("https://pastebin.com/raw/qPMD0jUW")
    ver = json.loads(ver.text)
    if proVer != ver[0]["CasinoVer"]:
        res = messagebox.askyesno("New version available!", "There is a new version available, would you like to go to the github page?")
        if res == True:
            CurrentStatus.set("Redirecting to github")
            webbrowser.open_new_tab("https://github.com/yeeter1/python-casino")
    else:
        CurrentStatus.set("Up to date.")


if checkpath.isfile("donute.png") != True:
    notfound.append("donut")

if checkpath.isfile("banned.png") != True:
    notfound.append("banhammer")

if checkpath.isfile("peanut.png") != True:
    notfound.append("peanut")

if checkpath.isfile("7.png") != True:
    notfound.append("7")


if len(notfound) >= 1:
    notfoundstr = ""
    for i in notfound:
        notfoundstr = notfoundstr + i + ","
    messagebox.showwarning("Images not found", "The following images weren't found: " + notfoundstr)

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
    global paydaycount, credits
    if paydaycount >= 1:
        messagebox.showinfo("Slot more!", "You haven't received your payday yet!")
    else:
        CurrentStatus.set("Giving payday...")
        paydaycount = 5
        listData[0]["Payday"] = paydaycount
        credits = credits + 150
        listData[0]["Credits"] = credits
        CurrentStatus.set("Writing to json...")
        writeToJSONFile(listData, "data")
        CurrentStatus.set("Credits: "+ str(credits) + ", payday in: 5 slots.")


def updateListData():
    global credits, paydaycount, listData
    listData[0]["Payday"] = paydaycount
    listData[0]["Credits"] = credits


def showlist():
    messagebox.showinfo("Combo list", CL)


def updatestatus():
    global credits, paydaycount
    if paydaycount == 0:
        CurrentStatus.set("Credits: " + str(credits) + ", ready for payday!")
    else:
        CurrentStatus.set("Credits: " + str(credits) + ", payday in: " + str(paydaycount) + " slots.")


def getcombo(i1, i2, i3):
    if i1 == "7.png" and i2 == "7.png" and i3 == "7.png":
        return "7 Streak"
    elif i1 == "banned.png" and i2 == "banned.png" and i3 == "banned.png":
        return "Ban Streak"


def openshop():
    messagebox.showinfo("Shop not complete", "Shop is currently WIP, and is hoped to be released in version 2 or earlier.")


def slot():
    global credits
    global paydaycount
    creditsslot = math.ceil(int(CreditsToSlotE.get()))
    if creditsslot > credits:
        messagebox.showinfo("Insufficient credits", "You don't have enough credits to slot!")
    else:
        if str(creditsslot).find("-") != -1:
            messagebox.showinfo("Wrong case int", "Please only slot positive integers!")
        else:
            credits = credits - creditsslot
            if paydaycount >= 1:
                paydaycount = paydaycount - 1
            updateListData()
            writeToJSONFile(listData, "data")
            updatestatus()
            nam1 = images[random.randint(0, 3)]
            nam2 = images[random.randint(0, 3)]
            nam3 = images[random.randint(0, 3)]
            img1 = Image.open(nam1)
            pic1 = ImageTk.PhotoImage(img1)
            Slot1.config(image=pic1)
            Slot1.image = pic1
            img2 = Image.open(nam2)
            pic2 = ImageTk.PhotoImage(img2)
            Slot2.config(image=pic2)
            Slot2.image = pic2
            img3 = Image.open(nam3)
            pic3 = ImageTk.PhotoImage(img3)
            Slot3.config(image=pic3)
            Slot3.image = pic3
            combo = getcombo(nam1, nam2, nam3)
            if combo == "7 Streak":
                messagebox.showinfo("Got combo!", "Achieved combo: 7 Streak! 1000 Credits earned!")
                credits = credits + 1000
                updateListData()
                updatestatus()
                writeToJSONFile(listData, "data")
            elif combo == "Ban Streak":
                messagebox.showinfo("Got combo!", "Achieved combo: Ban Streak! Credits slotted multiplied by 5!")
                credits = creditsslot * 5 + credits
                updateListData()
                updatestatus()
                writeToJSONFile(listData, "data")

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Stuff", menu=subMenu)
subMenu.add_command(label="Payday", command=givePayday)
subMenu.add_command(label="Shop(WIP:Ver:2)", command=openshop)
subMenu.add_command(label="Combo list", command=showlist)
subMenu.add_separator()

CreditsToSlotL = Label(root, text="Enter how many credits you want to slot.")
CreditsToSlotL.grid(row=0, column=1)

CreditsToSlotE = Entry(root)
CreditsToSlotE.grid(row=1, column=1, sticky=W)

Slot = Button(root, text="Slot", command=slot)
Slot.place(x=25, y=41)

status = Label(root, textvariable=CurrentStatus, bd=1, relief=SUNKEN, anchor=W)
status.place(x=0, y=480)
status.config(width=500)

Slot1 = Label(root)
Slot1.place(x=50, y=200)

Slot2 = Label(root)
Slot2.place(x=200, y=200)

Slot3 = Label(root)
Slot3.place(x=375, y=200)

root.resizable(width=False, height=False)
root.minsize(width=750, height=500)
root.maxsize(width=750, height=500)
root.mainloop()
