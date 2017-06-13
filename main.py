#import multiprocessing, time, pika, json, traceback, logging, sys, os, itertools, urllib, urllib2, cStringIO, mysql.connector, shutil, hashlib, socket, urllib2, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from PIL import Image
from os import listdir
from os.path import isfile, join
#from bs4 import BeautifulSoup
from pprint import pprint
import webdriver_class


wdc = webdriver_class
wdc.appointment_search()import webdriver_class
from tkinter import *
import threading

root = Tk()
root.geometry("600x300")
frame = Frame(root)
root.resizable(width=False, height=False)
wdc = webdriver_class

def logIn():
    try:
        t = threading.Thread(target=wdc.appointment_search, args=(email.get("1.0",'end-1c'), pw.get("1.0",'end-1c')))
        t.daemon = True
        t.start()
    except:
        print
        "Error: unable to start thread"



button1 = Button(frame, text="Log In", height=2, width=15, command=logIn)
email = Text(frame, height=2, width=30)
pw = Text(frame, height=2, width=30)

frame.bind("<Key>", logIn)
frame.grid(column=0, row=7, padx=20, pady=40)

frame.pack()
email.pack()
pw.pack()
button1.pack()



root.mainloop()




