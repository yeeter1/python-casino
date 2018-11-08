from tkinter import *
from tkinter import messagebox
import requests
webhook = "https://discordapp.com/api/webhooks/510175661478903814/mb6e0Y6cvedSIx89yyJMaZrFY5PwkJ_mPu2R_53V9xo7rOA9EPAYutXdg5blbgFMO6-H"

def test():
    print("K")


def sendfb():
    feedback = message.get()
    usern = user.get()
    r = requests.post(webhook, data={"content":str(feedback), "username":str(usern)})
    if str(r.status_code)[0] == "2": #since all "SUCCESS" HTTP codes start with a 2, we want to look for the 2 at the beginning since some also have a 2 at the end.
        messagebox.showinfo("Success", "Successfully sent your feedback!")
        root.destroy()
    else:
        messagebox.showerror("Error", "Unable to send your feedback! Reason: " + r.reason)


root = Tk()
root.title("Feedback")
message = Entry(root)
message.place(x=125, y=150)
user = Entry(root, text="What would you like your name to be?")
user.place(x=125, y=100)
userL = Label(root, text="What would you like your name to be?")
userL.place(x=125, y=75)
info = Label(root, text="Have any ideas or feedback that you would like to send? Use this to do it!")
info.place(x=0,y=25)
send = Button(root, text="Send", command=sendfb)
send.place(x=125, y=175)

root.minsize(width=400,height=300)
root.mainloop()