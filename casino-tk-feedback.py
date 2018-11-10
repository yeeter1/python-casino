from tkinter import *
from tkinter import messagebox
import requests
import getpass
import json
user = getpass.getuser()
webhook = "https://discordapp.com/api/webhooks/510607855200632862/xS_UZLWK50hLD5bTl9H5PMFLoALN8yU78F9uuYGSiXFsqNp5yQJIbrrO2DU-7izTmS4S"
blacklist = "https://pastebin.com/raw/mnWzRpxi"
blacklist = requests.get(blacklist)
blacklist = json.loads(blacklist.text)
BL_ID = open("C:/Users/%s/AppData/Local/python-casino/id.txt" % user, "r")
BL_ID = BL_ID.read()

def sendfb():
    for i in blacklist[0]:
        if str(i) == str(BL_ID):
            messagebox.showwarning("Blacklisted.=", "It appears that you have been blacklisted from sending feedback.")
            root.destroy()
    feedback = message.get()
    r = requests.post(webhook, data={"content":str(feedback), "username":str(BL_ID[3:7])})
    if str(r.status_code)[0] == "2": #since all "SUCCESS" HTTP codes start with a 2, we want to look for the 2 at the beginning since some also have a 2 at the end.
        messagebox.showinfo("Success", "Successfully sent your feedback!")
        root.destroy()
    else:
        messagebox.showerror("Error", "Unable to send your feedback! Reason: " + r.reason)


root = Tk()
root.title("Feedback")
message = Entry(root)
message.place(x=125, y=125)
info = Label(root, text="Have any ideas or feedback that you would like to send? Use this to do it!")
info.place(x=0, y=25)
send = Button(root, text="Send", command=sendfb)
send.place(x=150, y=150)

root.minsize(width=400,height=300)
root.mainloop()
