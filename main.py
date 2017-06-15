import webdriver_class
from tkinter import *
import threading
import traceback

root = Tk()
root.geometry("440x180")
frame = Frame(root)
root.resizable(width=False, height=False)
wdc = webdriver_class

def logIn():
    try:
        t = threading.Thread(target=wdc.appointment_search, args=(email_entry.get(), pw_entry.get()))
        t.daemon = True
        t.start()
    except:
        traceback.print_exc()
        #print("Error: unable to start thread")


email_label = Label( text='Email: ')
pw_label = Label(text='Password: ')
email_entry = Entry()
pw_entry = Entry()
button1 = Button(text="Log In", height=2, width=15, command=logIn)

email_label.grid(row=0, column=2)
pw_label.grid(row=1, column=2)
email_entry.grid(row=0, column=3)
pw_entry.grid(row=1, column=3)
button1.grid(row=4, column=3, columnspan=3)

frame.bind("<Key>", logIn)






root.mainloop()



