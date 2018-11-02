from tkinter import *
from tkinter import messagebox
import json
import webbrowser
import math
import random
import os
import pip
import getpass  # i hate this module name because of how suspicious it looks
from os import path as checkpath

github = "https://github.com/yeeter1/python-casino"
hasgit = False
checkver = False
haspil = False
user = getpass.getuser()
CL = "3 7's = 1000 Credits \n3 Ban Hammers = Credits get slotted credits * 5 added to them.\n3 Gnomes = Lose 1500 credits."
root = Tk()
size = 128, 128
root.title("Casino game")
CurrentStatus = StringVar()
CurrentStatus.set("Retrieving version.")
proVer = "1.7"
notfound = []


def checkupdate():
    if checkver and hasgit:
        if proVer != ver[0]["CasinoVer"]:
            res = messagebox.askyesno("Update available!",
                                      "There is a new update available, would you like to update now?")
            if res == True:
                os.system("git clone %s" % (github))
                print("done")
                newpath = 'python-casino'
                newjsondata = newpath + "/data"
                abspath = os.path.abspath(newpath)
                updateListData()
                writeToJSONFile(listData, newjsondata)
                messagebox.showinfo("Updated successfully", "Update saved to: %s, please restart!" % abspath)
        else:
            messagebox.showinfo("Up to date", "You're on the latest version!")
    elif not checkver:
        messagebox.showinfo("No requests module", "You don't have the requests module installed!")
    elif not hasgit:
        messagebox.showerror("Git not installed", "You don't have git installed!")


images = ["peanut.png", "7.png", "banned.png", "donute.png", "gnome.png"]
try:
    import requests
except:
    pass
else:
    checkver = True

try:
    from PIL import Image, ImageTk
except:
    pass
else:
    haspil = True

try:
    gitcheck = os.system("git")
except:
    messagebox.showerror("Unexpected error", "An unexepected error occured when trying to check for git.")
else:
    if gitcheck == 1:
        hasgit = True

if not checkver:
    res = messagebox.askyesno("Install requests? (requires admin privileges!)", "It seems that you don't have the requests module, would you like to install it? (requires pip!)")
    if res:
        os.system("pip install requests")

if not haspil:
    res = messagebox.askyesno("Install Pillow? (requires admin privileges!)", "It seems that you don't have the Pillow  module (imaging), would you like to install it? (requires pip!)")
    if res:
        os.system("pip install Pillow")


def writeToJSONFile(data, filename):
    f = open(filename + '.json', 'w')
    json.dump(data, f)


if checkver:
    ver = requests.get("https://pastebin.com/raw/qPMD0jUW")
    ver = json.loads(ver.text)
    if str(proVer) != str(ver[0]["CasinoVer"]):
        res = messagebox.askyesno("New version available!", "There is a new version available, would you like to update now?")
        if res == True:
            checkupdate()
    else:
        CurrentStatus.set("Up to date.")

# too lazy to figure out how to use a for loop with this

if checkpath.isfile("donute.png") != True:
    notfound.append("donut")

if checkpath.isfile("banned.png") != True:
    notfound.append("banhammer")

if checkpath.isfile("peanut.png") != True:
    notfound.append("peanut")

if checkpath.isfile("7.png") != True:
    notfound.append("7")

if checkpath.isfile("gnome.png") != True:
    notfound.append("gnome")

if len(notfound) >= 1:
    notfoundstr = ""
    for i in notfound: #even though i literally use one here lul
        notfoundstr = notfoundstr + i + ", "
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
        CurrentStatus.set("Credits: " + str(credits) + ", payday in: " + str(paydaycount) + " slots.")


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
        CurrentStatus.set("Credits: " + str(credits) + ", payday in: 5 slots.")


def showver():
    messagebox.showinfo("Current Version", "Current version: %s" % str(proVer))


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
    elif i1 == "gnome.png" and i2 == "gnome.png" and i3 == "gnome.png":
        return "Gnomed"
    elif i1 == "gnome.png" and i2 == "gnome.png" and i3 == "7.png":
        return "Lucky Gnome"
    elif i1 == "gnome.png" and i2 == "7.png" and i3 == "gnome.png":
        return "Lucky Gnome"
    elif i1 == "7.png" and i2 == "gnome.png" and i3 == "gnome.png":
        return "Lucky Gnome"


def gitredirect():
    webbrowser.open_new_tab(github)


def openshop():
    messagebox.showinfo("Shop not complete",
                        "Shop is currently WIP, and is hoped to be released in version 2 or earlier.")


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
            nam1 = images[random.randint(0, 4)]
            nam2 = images[random.randint(0, 4)]
            nam3 = images[random.randint(0, 4)]
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
            elif combo == "Gnomed":
                messagebox.showinfo("Got combo!", "Achieved combo: Gnomed! Lost 1500 Credits.")
                if credits > 1500:
                    credits = credits - 1500
                    updateListData()
                    updatestatus()
                    writeToJSONFile(listData, "data")
                else:
                    credits = credits - credits
                    updateListData()
                    updatestatus()
                    writeToJSONFile(listData, "data")
            elif combo == "Lucky Gnome":
                credits = credits + 750
                messagebox.showinfo("Got combo!", "Achieved combo: Lucky Gnome! Gained 750 credits.")
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
subMenu.add_command(label="Check update", command=checkupdate)
subMenu.add_command(label="Github page", command=gitredirect)
subMenu.add_command(label="Current version", command=showver)
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
